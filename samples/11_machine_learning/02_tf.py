# %%

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

np.set_printoptions(precision=3,
                    suppress=True)

print(tf.__version__)

mnist = tf.keras.datasets.mnist

class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print(x_train.shape)
print(len(y_train))
print(y_train)
print(x_test.shape)
print(len(y_test))
print(y_test)

plt.figure()
plt.imshow(x_train[0])
plt.colorbar()
plt.grid(False)
plt.show()

plt.figure(figsize=(10, 10))
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[y_train[i]])

# %%

model = tf.keras.Sequential()

model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(10))

# %%

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

opt = tf.keras.optimizers.Adam()

model.compile(optimizer=opt, loss=loss_fn, metrics=['accuracy'])

# %%

model.fit(x=x_train, y=y_train, epochs=5)

# %%

model.evaluate(x_test, y_test, verbose=2)

# %%

prediction = model(x_test[:5])

print("prediction:\n{}".format(prediction))

labels = y_test[:5]
predicted_labels = np.argmax(prediction, axis=1)

plt.figure()
plt.xticks([])
plt.yticks([])
plt.grid(False)
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.xlabel("Label: {}, Prediction: {}".format(
    class_names[labels[0]], class_names[predicted_labels[0]]))

# %%

p_model = tf.keras.Sequential()

p_model.add(model)
p_model.add(tf.keras.layers.Softmax())

prediction = p_model(x_test[:5])

print("prediction:\n{}".format(prediction))

labels = y_test[:5]
predicted_labels = np.argmax(prediction, axis=1)

plt.figure()
plt.xticks([])
plt.yticks([])
plt.grid(False)
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.xlabel("Label: {}, Prediction: {}, %: {:.3f}".format(
    class_names[labels[0]], class_names[predicted_labels[0]], prediction[0][predicted_labels[0]]))

# %%

