import cv2 as cv
import numpy as np

from absl import app
from pathlib import Path


def main(argv):

    image = np.zeros((480, 640, 1), dtype=np.uint8)

    image = cv.circle(image, (320, 240), 50, (125), -1)

    canny_image = cv.Canny(image, 124, 255)

    cv.imshow("canny_image", canny_image)
    
    cv.waitKey(0)

    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":

    app.run(main)
