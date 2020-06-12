import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

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

    # Generate histogram

    plt.hist(img.ravel(), 256, [0, 256])
    plt.savefig("data/threshold_histogram.png")
    plt.show()

    thresholds = [0, 100, 150, 255]

    thresholded_img = np.zeros((rows, cols), dtype=np.uint8)
    result_img = np.zeros((rows, cols), dtype=np.uint8)
    
    for i in range(len(thresholds) - 1):

        thresholded_img = cv.inRange(img, thresholds[i], thresholds[i+1])
        thresholded_img = np.uint8(thresholded_img / 255) * thresholds[i + 1]

        cv.imshow("Thresholded Image", thresholded_img)
        cv.waitKey(0)

        result_img = result_img + thresholded_img

    cv.imshow("Result Image", result_img)
    cv.waitKey(0)
    cv.imwrite("data/threshold_segemented_image.png", result_img)

    cv.destroyAllWindows()   

    return


if __name__ == "__main__":

    main()