import cv2 as cv
import numpy as np

from absl import app
from pathlib import Path


def main(argv):

    image = (255, 255, 255) * np.ones((200, 600, 3))

    image = cv.putText(image, "OpenCV is Great!", (50, 100), cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

    cv.imshow("image", image)

    cv.waitKey(0)

    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":

    app.run(main)
