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
    cv.waitKey(1)
    cv.imwrite('../images/02/01.PNG', img)

    # Convert image from BGR to grayscale

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Apply gaussian noise to img

    noisy_img = noise(img, Noise.GAUSSIAN)

    cv.imshow("noisy_img", noisy_img)
    cv.waitKey(1)
    cv.imwrite("data/gaussian_noise_apples.png", noisy_img)
    cv.imwrite('../images/02/02.PNG', noisy_img)
    
    # Use a gaussian filter to remove noise

    filtered_img = cv.GaussianBlur(noisy_img, (3, 3), 0)

    cv.imshow("gaussian_filtered_img", filtered_img)
    cv.waitKey(0)
    cv.imwrite("data/gaussian_filtered_apples.png", filtered_img)
    cv.imwrite('../images/02/03.PNG', filtered_img)

    cv.destroyAllWindows()
   
    return


if __name__ == "__main__":

    main()
