import cv2 as cv
import numpy as np

from absl import app
from pathlib import Path

def main(argv):

    image = (255, 0, 0)*np.ones((480, 640, 3))

    cv.imshow("image", image)

    cv.waitKey(0)

    executable_path = Path(argv[0])

    output_path = (executable_path.parent).joinpath("data")

    if (not Path.exists(output_path)):

        Path.mkdir(output_path)

    output_file = output_path.joinpath("image.png")

    print(str(output_file))

    cv.imwrite(str(output_file), image)

    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":

    app.run(main)