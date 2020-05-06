import cv2 as cv
import numpy as np

from absl import app
from pathlib import Path


def main(argv):

    image = np.zeros((480, 640, 1))

    image = cv.circle(image, (320, 240), 50, (125), -1)

    cv.imshow("image", image)

    cv.waitKey(1)

    ret, image_threshold = cv.threshold(image, 124, 255, cv.THRESH_BINARY)

    cv.imshow("image_threshold", image_threshold)

    cv.waitKey(0)

    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":

    app.run(main)
