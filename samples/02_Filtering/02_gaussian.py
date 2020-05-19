import cv2 as cv
import numpy as np

from utils import noise, Noise


def main():

    # Load image

    img = cv.imread("data/apples.png")

    if img is None:
        print("ERROR::CV::Could not read image.")
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

    # Apply gaussian noise to img

    img = noise(img, Noise.GAUSSIAN)

    cv.imshow("img", img)
    cv.waitKey(0)
    cv.imwrite("data/gaussian_noise_apples.png", img)
    
    # Use a gaussian filter to remove noise

    filtered_img = cv.GaussianBlur(img, (3, 3), 0)

    cv.imshow("gaussian_filtered_img", filtered_img)
    cv.waitKey(0)
    cv.imwrite("data/gaussian_filtered_apples.png", filtered_img)

    cv.destroyAllWindows()
   
    return


if __name__ == "__main__":

    main()
