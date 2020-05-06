import cv2 as cv

from absl import app
from pathlib import Path

def main(argv):

    executable_path = Path(argv[0])

    input_file = (executable_path.parent).joinpath("data/image.png")

    print(input_file)

    image = cv.imread(str(input_file), cv.IMREAD_COLOR)

    if image is None:

        print("Error: 'image' is empty")

        return 1

    cv.imshow("image", image)

    cv.waitKey(0)

    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":

    app.run(main)