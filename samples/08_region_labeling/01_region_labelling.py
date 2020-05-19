import cv2 as cv
import numpy as np
import random

def main():

    # Create shapes

    image1 = np.zeros((480, 640, 1), np.uint8)

    coordinates = [(int(random.random() * 640), int(random.random() * 480)) for _ in range(40)]

    for c in coordinates:

        cv.circle(image1, c, 10, (255), -1)

    #  Find contorus

    contours, hierarchy = cv.findContours(image1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    image2 = np.zeros((480, 640, 3), np.uint8)

    # Colourize each contour

    for i, c in enumerate(contours):

        colour = (random.random() * 255, random.random() * 255, random.random() * 255)

        cv.drawContours(image2, contours, i, colour, -1)

    cv.imshow("image1", image1)
    cv.waitKey(0)
    cv.imwrite("data/image_1.png", image1)

    cv.imshow("image2", image2)
    cv.waitKey(0)
    cv.imwrite("data/image_2.png", image2)

    cv.destroyAllWindows()

    return


if __name__ == "__main__":

    main()