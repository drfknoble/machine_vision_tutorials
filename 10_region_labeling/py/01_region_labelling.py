import cv2 as cv
import numpy as np
import random


def main():

    # Create shapes

    rows, cols = 480, 640
    img = np.zeros((rows, cols, 1), np.uint8)

    coordinates = [(int(random.random() * cols), int(random.random() * rows))
                   for _ in range(40)]

    for c in coordinates:

        cv.circle(img, c, 10, (255), -1)

    cv.imshow("img", img)
    cv.waitKey(1)
    cv.imwrite("data/img.PNG", img)
    cv.imwrite('../images/01/01.PNG', img)

    #  Find contorus

    contours, hierarchy = cv.findContours(
        img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Draw each contour

    regions = np.zeros((rows, cols, 3), np.uint8)

    for i, c in enumerate(contours):

        colour = (random.random() * 255, random.random()
                  * 255, random.random() * 255)

        cv.drawContours(regions, contours, i, colour, -1)

    cv.imshow("regions", regions)
    cv.waitKey(0)
    cv.imwrite("data/regions.PNG", regions)
    cv.imwrite('../images/01/02.PNG', regions)

    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":

    main()
