import cv2 as cv
import numpy as np


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

    # k-means

    data = np.reshape(img, (-1, channels))
    data = np.float32(data)    

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    
    for K in range(2, 14, 2):

        ret, label, center = cv.kmeans(data, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

        center = np.uint8(center)

        quantized = center[label.flatten()]
        quantized = quantized.reshape((rows, cols, channels))

        cv.imshow("Quantized Image, K = {}".format(K), quantized)
        cv.waitKey(0)
        cv.imwrite("data/quantized_image_{}.png".format(K), quantized)
        cv.imwrite('../images/02/0{}.PNG'.format(int(K/2 + 1)), quantized)

    cv.destroyAllWindows()

    return


if __name__ == "__main__":

    main()