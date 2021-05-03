import cv2 as cv
import numpy as np
import random


def main():

    # Create image

    rows, cols = 480, 640
    img = np.zeros((rows, cols), dtype=np.uint8)

    # Draw circles at the centre

    cv.circle(img, (320, 240), 150, (255), 40)
    cv.circle(img, (320, 240), 100, (255), 40)

    # Generate random noise

    coordinates = [(int(random.random() * cols),
                    int(random.random() * rows)) for _ in range(100)]

    for c in coordinates:

        cv.circle(img, c, 2, (255), -1)

    cv.imshow("img", img)
    cv.waitKey(1)
    cv.imwrite("data/morph_img.png", img)
    cv.imwrite('../images/01/01.PNG', img)

    # Erode image using different shapes

    shapes = [cv.MORPH_RECT, cv.MORPH_CROSS, cv.MORPH_ELLIPSE]
    shapes_label = ["MORPH_RECT", "MORPH_CROSS", "MORPH_ELLIPSE"]

    for i, s in enumerate(shapes):

        kernel = cv.getStructuringElement(s, (20, 20))
        print("{}: \n{}\n".format(shapes_label[i], kernel))

        eroded = cv.erode(img, kernel)

        cv.imshow("Eroded + {}".format(shapes_label[i]), eroded)
        cv.waitKey(0)
        cv.imwrite("data/eroded_{}.png".format(shapes_label[i]), eroded)
        cv.imwrite('../images/01/0{}.PNG'.format(i+2), eroded)

    cv.destroyAllWindows()

    return


if __name__ == "__main__":

    main()
