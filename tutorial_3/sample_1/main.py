import cv2 as cv
import numpy as np

from absl import app
from pathlib import Path


def main(argv):

    image = (255, 255, 255) * np.ones((400, 400, 3))

    image = cv.line(image, (100, 50), (300, 50), (0, 0, 0), 10)
    image = cv.line(image, (350, 100), (350, 300), (0, 0, 0), 10)
    image = cv.line(image, (300, 350), (100, 350), (0, 0, 0), 10)
    image = cv.line(image, (50, 300), (50, 100), (0, 0, 0), 10)

    image = cv.ellipse(image, (100, 100), (50, 50), 0, 180, 270, (0, 0, 0), 10)
    image = cv.ellipse(image, (300, 100), (50, 50), 0, 270, 360, (0, 0, 0), 10)
    image = cv.ellipse(image, (100, 300), (50, 50), 0, 90, 180, (0, 0, 0), 10)
    image = cv.ellipse(image, (300, 300), (50, 50), 0, 0, 90, (0, 0, 0), 10)

    image = cv.circle(image, (200, 200), 75, (0, 0, 0), 10)
    image = cv.circle(image, (300, 100), 25, (0, 0, 0), -1)

    cv.imshow("image", image)

    cv.waitKey(0)

    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":

    app.run(main)
