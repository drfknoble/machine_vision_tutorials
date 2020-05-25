import cv2 as cv
import IPython.display as display
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import tensorflow as tf

from absl import app, flags
from networks import unet

FLAGS = flags.FLAGS

flags.DEFINE_string("dataset", "data/", "")
flags.DEFINE_integer("batch_size", 8, "")
flags.DEFINE_integer("epochs", 1, "")
flags.DEFINE_integer("image_height", 224, "")
flags.DEFINE_integer("image_width", 224, "")


def main(argv):

    np.set_printoptions(precision=3,
                        suppress=True)

    print(tf.__version__)

    path = pathlib.Path("data")

    training_path = path.joinpath("training")
    validation_path = path.joinpath("validation")

    training_features_path = training_path.joinpath("features")
    training_labels_path = training_path.joinpath("labels")
    validation_features_path = validation_path.joinpath("features")
    validation_labels_path = validation_path.joinpath("labels")

    num_training_features = len(list(training_features_path.glob('*.png')))
    num_training_labels = len(list(training_labels_path.glob('*.png')))
    num_validation_features = len(list(validation_features_path.glob('*.png')))
    num_validation_labels = len(list(validation_labels_path.glob('*.png')))

    batch_size = FLAGS.batch_size
    img_height = FLAGS.image_height
    img_width = FLAGS.image_width
    epochs = FLAGS.epochs
    steps_per_epoch = np.ceil(num_training_features / batch_size)

    def preprocess_label(label):

        shape = label.shape

        classes = 2

        palette = np.array( [[0.0, 0.0, 0.0],
                             [1.0, 1.0, 1.0]])

        labels = np.zeros([shape[0], shape[1], classes])

        for i in range(classes):
            mask = np.float32(label[:, :, :] == palette[i])
            labels[:, :, i] = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)

        return labels

    training_preprocessing = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1.0/255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

    training_feature_generator = training_preprocessing.flow_from_directory(directory=str(training_path),
                                                            batch_size=batch_size,
                                                            seed=1,
                                                            shuffle=True,
                                                            target_size=(img_height, img_width),
                                                            class_mode=None,
                                                            classes=["features"])

    training_label_generator = training_preprocessing.flow_from_directory(directory=str(training_path),
                                                            batch_size=batch_size,
                                                            seed=1,
                                                            shuffle=True,
                                                            target_size=(img_height, img_width),
                                                            class_mode=None,
                                                            classes=["labels"])

    validation_preprocessing = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1.0/255)

    validation_feature_generator = validation_preprocessing.flow_from_directory(directory=str(validation_path),
                                                               batch_size=batch_size,
                                                               seed=1,
                                                               shuffle=True,
                                                               target_size=(img_height, img_width),
                                                               class_mode=None,
                                                               classes=["features"])

    validation_label_generator = validation_preprocessing.flow_from_directory(directory=str(validation_path),
                                                               batch_size=batch_size,
                                                               seed=1,
                                                               shuffle=True,
                                                               target_size=(img_height, img_width),
                                                               class_mode=None,
                                                               classes=["labels"])

    def training_generator(feature_generator, label_generator):

        while True:

            X = next(feature_generator)
            y = next(label_generator)

            y_processed = np.array([preprocess_label(l) for l in y])

            yield X, y_processed

    model = unet.network(img_height=img_height, img_width=img_width)

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
        metrics=['accuracy']
    )

    model.summary()

    checkpoint_path = "checkpoints/cp-{epoch:04d}.ckpt"
    checkpoint_dir = pathlib.Path(checkpoint_path).parent

    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                     save_weights_only=True,
                                                     verbose=1,
                                                     save_freq=int(steps_per_epoch // 2))

    latest = tf.train.latest_checkpoint(checkpoint_dir)

    if latest is not None:
        print(latest)
        model.load_weights(latest)
    else:
        model.save_weights(checkpoint_path.format(epoch=0))

    history = model.fit(
        x=training_generator(training_feature_generator, training_label_generator),
        steps_per_epoch=num_training_features // batch_size,
        epochs=epochs,
        validation_data=training_generator(validation_feature_generator, validation_label_generator),
        validation_steps=num_validation_features // batch_size,
        callbacks=[cp_callback])

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
    plt.savefig("training_history.png")
    # plt.show()

    model.evaluate(x=training_generator(validation_feature_generator, validation_label_generator), batch_size=batch_size, steps=10)

    model.save("saved_models/unet")
  
    return


if __name__ == "__main__":

    app.run(main)
