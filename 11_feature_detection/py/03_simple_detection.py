import cv2 as cv
import json
import numpy as np
import time


def main():

    # Simple

    img = cv.imread('data/red_circles.PNG')

    if img is None:
        print('ERROR::CV::Could not read image.')
        return 1

    rows, cols, channels = img.shape

    rows = rows // 2
    cols = cols // 2

    img = cv.resize(img, (cols, rows))

    cv.imshow('img', img)
    cv.waitKey(1)
    cv.imwrite('../images/03/01.PNG', img)

    # Get red pixels

    red_ub = cv.inRange(img, (0, 20, 20), (50, 255, 255))
    red_lb = cv.inRange(img, (130, 20, 20), (180, 255, 255))
    red = cv.bitwise_or(red_ub, red_lb)

    cv.imshow('red', red)
    cv.waitKey(1)
    cv.imwrite('data/red.PNG', red)
    cv.imwrite('../images/03/02.PNG', red)

    # Define properties

    params = cv.SimpleBlobDetector_Params()
    
    params.filterByColor = True
    params.blobColor = 255

    simple = cv.SimpleBlobDetector_create(parameters=params)
    kp = simple.detect(red, None)

    simple_img = cv.drawKeypoints(img, kp, None, color=[255, 0, 0])

    cv.imshow("simple_img", simple_img)
    cv.waitKey(0)
    cv.imwrite("data/simple_img.PNG", simple_img)
    cv.imwrite('../images/03/03.PNG', simple_img)

    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":

    main()
