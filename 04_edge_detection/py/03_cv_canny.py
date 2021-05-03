import cv2 as cv
import numpy as np


def main():

    # Load image

    img = cv.imread("data/apples.PNG")

    if img is None:
        print("ERROR::CV::Could not read image.")
        return

    # Resize image

    rows, cols, channels = img.shape

    img = cv.resize(img, (cols // 2, rows // 2))

    cv.imshow("img", img)
    cv.waitKey(1)
    cv.imwrite('../images/03/01.PNG', img)

    # Convert image from BGR to grayscale

    img_blur = cv.GaussianBlur(img, (3, 3), 0)

    img_gray = cv.cvtColor(img_blur, cv.COLOR_BGR2GRAY)

    cv.imshow('img_gray', img_gray)
    cv.waitKey(1)
    cv.imwrite('data/img_gray.PNG', img_gray)
    cv.imwrite('../images/03/02.PNG', img_gray)


    # OpenCV canny()

    canny = cv.Canny(img_gray, 20, 75)

    cv.imshow("OpenCV Canny()", canny)
    cv.waitKey(0)
    cv.imwrite("data/cv_canny.PNG", canny)
    cv.imwrite('../images/03/03.PNG', canny)

    cv.destroyAllWindows()

    return


if __name__ == "__main__":

    main()
