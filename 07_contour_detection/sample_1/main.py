import cv2 as cv
import numpy as np

from absl import app
from pathlib import Path


def main(argv):

    image = np.zeros((480, 640, 3), dtype=np.uint8)

    image = cv.circle(image, (320, 240), 50, (120, 0, 0), -1)

    cv.imshow("image", image)
    cv.waitKey(1)

    image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    thresholded_image = cv.inRange(image_hsv, (115, 0, 0), (125, 255, 255))

    cv.imshow("thresholded_image", thresholded_image)
    cv.waitKey(1)

    contours, hierarchy = cv.findContours(thresholded_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for i in range(len(contours)):

        image = cv.drawContours(image, contours, i, (0, 0, 255), 3)

    cv.imshow("image", image)
    cv.waitKey(1)
    
    cv.waitKey(0)

    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":

    app.run(main)
