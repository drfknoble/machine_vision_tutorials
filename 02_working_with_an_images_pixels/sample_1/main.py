import cv2 as cv

from absl import app
from pathlib import Path

def main(argv):

    executable_path = Path(argv[0])

    input_file = (executable_path.parent).joinpath("data/image.jpg")

    print(input_file)

    image = cv.imread(str(input_file), cv.IMREAD_COLOR)

    if image is None:

        print("Error: 'image' is empty")

        return 1

    intensity = image[100, 100]

    blue = intensity[0]
    red = intensity[1]
    green = intensity[2]

    print("{}, {}, {}, {}".format(intensity, blue, red, green))

    cv.imshow("image", image)

    cv.waitKey(0)

    image[100, 100] = (100, 0, 0)
    
    intensity = image[100, 100]

    blue = intensity[0]
    red = intensity[1]
    green = intensity[2]

    print("{}, {}, {}, {}".format(intensity, blue, red, green))
    
    cv.imshow("image", image)

    cv.waitKey(0)

    image[100, 100] = (100, 0, 0)

    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":

    app.run(main)