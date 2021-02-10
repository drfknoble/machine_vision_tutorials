# %%

import IPython.display as display
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import tensorflow as tf

from PIL import Image
from utils import show_batch

np.set_printoptions(precision=3,
                    suppress=True)

print(tf.__version__)

data_file = tf.keras.utils.get_file(origin='https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip',
                                    fname='cats_and_dogs_filtered.zip', extract=True)
data_file_path = pathlib.Path(data_file)

# %%

path = (data_file_path.parent).joinpath("cats_and_dogs_filtered")

print(path)

train_path = path.joinpath("train")
validation_path = path.joinpath("validation")

print(train_path)
print(validation_path)

train_cats_path = train_path.joinpath("cats")
train_dogs_path = train_path.joinpath("dogs")
validation_cats_path = validation_path.joinpath("cats")
validation_dogs_path = validation_path.joinpath("dogs")

print(train_cats_path)
print(train_dogs_path)
print(validation_cats_path)
print(validation_dogs_path)

# %%

tr_cat_images = len(list(train_cats_path.glob('*.jpg')))
tr_dog_images = len(list(train_dogs_path.glob('*.jpg')))
val_cat_images = len(list(validation_cats_path.glob('*.jpg')))
val_dog_images = len(list(validation_dogs_path.glob('*.jpg')))

total_train = tr_cat_images + tr_dog_images
total_validation = val_cat_images + val_dog_images

print(tr_cat_images)
print(tr_dog_images)
print(val_cat_images)
print(val_dog_images)

# %%

batch_size = 16
img_height = 150
img_width = 150
epochs = 3
steps_per_epoch = np.ceil(tr_cat_images / batch_size)

train_image_generator = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1.0/255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

train_data_gen = train_image_generator.flow_from_directory(directory=str(train_path),
                                                           batch_size=batch_size,
                                                           shuffle=True,
                                                           target_size=(
                                                               img_height, img_width),
                                                           class_mode='categorical')

validation_image_generator = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1.0/255)

validation_data_gen = validation_image_generator.flow_from_directory(directory=str(validation_path),
                                                                     batch_size=batch_size,
                                                                     shuffle=True,
                                                                     target_size=(
                                                                         img_height, img_width),
                                                                     class_mode='categorical')

image_batch, label_batch = next(train_data_gen)

print(image_batch.shape)
print(label_batch.shape)
print(label_batch)

show_batch(image_batch, label_batch, ['cat', 'dog'])

# %%

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu', input_shape=(
        img_height, img_width, 3)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(2)
], name="cats_and_dogs")

checkpoint_path = "checkpoints/cp-{epoch:04d}.ckpt"
checkpoint_dir = pathlib.Path(checkpoint_path).parent

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1,
                                                 save_freq=2 * int(steps_per_epoch))

model.compile(optimizer='sgd',
              loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.summary()

# %%

latest = tf.train.latest_checkpoint(checkpoint_dir)

print(latest)

if latest is not None:
    model.load_weights(latest)
else:
    model.save_weights(checkpoint_path.format(epoch=0))

# %%

history = model.fit(
    x=train_data_gen,
    steps_per_epoch=total_train // batch_size,
    epochs=epochs,
    validation_data=validation_data_gen,
    validation_steps=10,  # total_validation // batch_size,
    callbacks=[cp_callback]
)

# %%

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

# %%

model.evaluate(x=validation_data_gen, batch_size=batch_size, steps=10)

# %% 

image_batch, label_batch = next(validation_data_gen)

# show_batch(image_batch, label_batch, ['cat', 'dog'])

image = image_batch[0]
label = label_batch[0]

print(image.shape)
print(label.shape)

prediction = model.predict(np.array([image]))

print(prediction)

plt.figure()
plt.xticks([])
plt.yticks([])
plt.grid(False)
plt.imshow(image)
plt.title(str(prediction))
plt.show()

# %%

p_model = tf.keras.Sequential()

p_model.add(model)
p_model.add(tf.keras.layers.Softmax())

prediction = p_model.predict(np.array([image]))

print(prediction)

plt.figure()
plt.xticks([])
plt.yticks([])
plt.grid(False)
plt.imshow(image)
plt.title(str(prediction))
plt.show()

# %%

model.save("saved_models/cats_and_dogs")
