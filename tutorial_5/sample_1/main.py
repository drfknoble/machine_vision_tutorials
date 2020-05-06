import cv2 as cv
import numpy as np

from absl import app
from pathlib import Path


def main(argv):

    image = np.zeros((480, 640, 1))

    image = cv.circle(image, (320, 240), 50, (125), -1)

    ret, thresholded_image = cv.threshold(image, 124, 255, cv.THRESH_BINARY)

    cv.imshow("thresholded_image", thresholded_image)

    cv.waitKey(1)

    element_size = 10
    element = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2 * element_size + 1, 2 * element_size + 1), (element_size, element_size))

    eroded_image = cv.erode(thresholded_image, element)

    cv.imshow("eroded_image", eroded_image)
    cv.waitKey(1)

    dilated_image = cv.dilate(thresholded_image, element)

    cv.imshow("dilated_imagte", dilated_image)
    cv.waitKey(1)

    cv.waitKey(0)

    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":

    app.run(main)
