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

    # print(path)

    validation_path = path.joinpath("validation")

    # print(validation_path)

    validation_features_path = validation_path.joinpath("features")
    validation_labels_path = validation_path.joinpath("labels")

    # print(validation_features_path)
    # print(validation_labels_path)

    num_validation_features = len(list(validation_features_path.glob('*.png')))
    num_validation_labels = len(list(validation_labels_path.glob('*.png')))

    # print(num_validation_features)
    # print(num_validation_labels)

    batch_size = FLAGS.batch_size
    img_height = FLAGS.image_height
    img_width = FLAGS.image_width
    epochs = FLAGS.epochs
    steps_per_epoch = np.ceil(num_validation_features / batch_size)

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

    model_path = pathlib.Path("./saved_models/unet")

    if not model_path.exists():

        print("Model not found")
        
        return

    model = tf.keras.models.load_model(model_path)

    model.summary()

    model.evaluate(x=training_generator(validation_feature_generator, validation_label_generator), batch_size=batch_size, steps=1)
  
    feature_batch, label_batch = next(training_generator(validation_feature_generator, validation_label_generator))

    predicted_batch = model.predict(feature_batch)

    predictions_path = pathlib.Path("predictions")

    if not predictions_path.exists():
        pathlib.Path.mkdir(predictions_path)

    i = 0
    for f, l, p in zip(feature_batch, label_batch, predicted_batch):

        f = cv.cvtColor(f, cv.COLOR_RGB2BGR)
        
        f = np.uint8(255 * f)
        l_0 = l[:, :, 0]
        l_1 = l[:, :, 1]
        p_0 = p[:, :, 0]
        p_1 = p[:, :, 1]

        cv.imshow("feature", f)
        cv.imshow("label[0]", l_0)
        cv.imshow("label[1]", l_1)
        cv.imshow("predicted_label[0]", p_0)
        cv.imshow("predicted_label[1]", p_1)

        cv.waitKey(0)

        l_0 = np.uint8(255 * l_0)
        l_1 = np.uint8(255 * l_1)
        p_0 = np.uint8(255 * p_0)
        p_1 = np.uint8(255 * p_1)

        cv.imwrite("predictions/{}_feature.png".format(i), f)
        cv.imwrite("predictions/{}_label[0].png".format(i), l_0)
        cv.imwrite("predictions/{}_label[1].png".format(i), l_1)
        cv.imwrite("predictions/{}_predicted[0].png".format(i), p_0)
        cv.imwrite("predictions/{}_predicted[1].png".format(i), p_1)

        i = i + 1
        
    return

if __name__ == "__main__":

    app.run(main)
