import cv2 as cv
import numpy as np


def main():

    # Load image

    img = cv.imread("data/apples.png")

    if img is None:
        print("ERROR::CV::Could not read image.")
        return

    # Resize image

    rows, cols, channels = img.shape

    img = cv.resize(img, (cols // 2, rows // 2))

    cv.imshow("img", img)
    cv.waitKey(0)
    cv.imwrite('../images/03/01.PNG', img)

    # Convert image from BGR to grayscale

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # OpenCV canny()

    canny = cv.Canny(img, 25, 255)

    cv.imshow("OpenCV Canny()", canny)
    cv.waitKey(0)
    cv.imwrite("data/cv_canny.png", canny)
    cv.imwrite('../images/03/02.PNG', canny)

    cv.destroyAllWindows()

    return


if __name__ == "__main__":

    main()
