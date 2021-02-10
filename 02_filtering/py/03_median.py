import cv2 as cv
import numpy as np

from utils import noise, Noise


def main():

    # Load image

    img = cv.imread("data/apples.png")

    if img is None:
        print("ERROR::CV::Could not read image.")
        return 1

    # Resize image

    rows, cols, channels = img.shape
    
    rows = rows // 2
    cols = cols // 2

    img = cv.resize(img, (cols, rows))

    cv.imshow("img", img)
    cv.waitKey(1)
    cv.imwrite('../images/03/01.PNG', img)

    # Convert image from BGR to grayscale

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Apply salt and pepper noise to img

    salt_img = noise(img, Noise.SALT_PEPPER)

    cv.imshow("salt_img", salt_img)
    cv.waitKey(1)
    cv.imwrite("data/salt_noise_apples.png", salt_img)
    cv.imwrite('../images/03/02.PNG', salt_img)
    
    # Use a median filter to remove noise

    filtered_img = cv.medianBlur(salt_img, 3)

    cv.imshow("median_salt_filtered_img", filtered_img)
    cv.waitKey(0)
    cv.imwrite("data/median_filtered_apples.png", filtered_img)
    cv.imwrite('../images/03/03.PNG', filtered_img)

    cv.destroyAllWindows()
   
    return


if __name__ == "__main__":

    main()
