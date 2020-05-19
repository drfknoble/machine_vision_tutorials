import cv2 as cv
import numpy as np

from utils import noise, Noise



def main():

    # Load image

    img = cv.imread("data/apples.png")

    if img is None:
        return

    # Resize image

    rows, cols, channels = img.shape
    
    rows = rows // 2
    cols = cols // 2

    img = cv.resize(img, (cols, rows))

    cv.imshow("img", img)
    cv.waitKey(0)

    # Convert image from BGR to grayscale

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Apply salt and pepper noise to img

    img = noise(img, Noise.SALT_PEPPER)
    
    cv.imshow("gray_salt_image", img)
    cv.waitKey(0)
    cv.imwrite("data/gray_salt_noise_apples.png", img)

    # Erode using different shapes

    shapes = [cv.MORPH_RECT, cv.MORPH_CROSS, cv.MORPH_ELLIPSE]
    shapes_label = ["MORPH_RECT", "MORPH_CROSS", "MORPH_ELLIPSE"]

    for i, s in enumerate(shapes):

        kernel = cv.getStructuringElement(s, (5, 5))
        print("{}: \n{}\n".format(shapes_label[i], kernel))

        opened = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
        
        cv.imshow("Opened + {}".format(shapes_label[i]), opened)
        cv.waitKey(0)        
        cv.imwrite("data/gray_salt_opened_{}.png".format(shapes_label[i]), opened)

    return

    cv.destroyAllWindows()


if __name__ == "__main__":

    main()
