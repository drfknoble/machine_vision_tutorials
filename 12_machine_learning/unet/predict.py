import cv2 as cv
import numpy as np
import pathlib
import tensorflow as tf

from absl import app, flags

FLAGS = flags.FLAGS

flags.DEFINE_string("image", "./data/plant.png" , "")
flags.DEFINE_string("model_path", "saved_models/unet", "")

def main(argv):

    model_path = pathlib.Path(FLAGS.model_path)

    if not model_path.exists():

        print("Model not found")
        
        return -1

    model = tf.keras.models.load_model(model_path)

    model.summary()

    img_bgr = cv.imread(FLAGS.image, cv.IMREAD_COLOR)
    img_bgr = cv.resize(img_bgr, (224, 224))
    img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)

    feature = np.array([img_rgb])

    print(type(feature))
    print(feature.shape)

    predicted_label = model.predict(feature)

    print(type(predicted_label))
    print(predicted_label.shape)

    for i in range(0, 2, 1):

        c = predicted_label[0, :, :, i]

        cv.imshow("predicted_label[{}]".format(i), c)
        cv.waitKey(0)

    cv.destroyAllWindows()

    return


if __name__ == "__main__":

    app.run(main)

