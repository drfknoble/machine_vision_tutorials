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
    cv.imwrite('../images/01/01.PNG', img)

    # Get blue, green, and red channels

    B = img[:, :, 0]
    G = img[:, :, 1]
    R = img[:, :, 2]

    B_colorized = np.zeros((rows, cols, 3), dtype=np.uint8)
    B_colorized[:, :, 0] = B

    cv.imshow("B_colorized", B_colorized)
    cv.waitKey(1)
    cv.imwrite("data/BGR_B.png", B)
    cv.imwrite('../images/01/02.PNG', B)
    cv.imwrite("data/BGR_B_colorized.png", B_colorized)
    cv.imwrite('../images/01/03.PNG', B_colorized)

    G_colorized = np.zeros((rows, cols, 3), dtype=np.uint8)
    G_colorized[:, :, 1] = G

    cv.imshow("G_colorized", G_colorized)
    cv.waitKey(1)
    cv.imwrite("data/BGR_G.png", G)
    cv.imwrite('../images/01/04.PNG', G)
    cv.imwrite("data/BGR_G_colorized.png", G_colorized)
    cv.imwrite('../images/01/05.PNG', G_colorized)

    R_colorized = np.zeros((rows, cols, 3), dtype=np.uint8)
    R_colorized[:, :, 2] = R

    cv.imshow("R_colorized", R_colorized)
    cv.waitKey(0)
    cv.imwrite("data/BGR_R.png", R)
    cv.imwrite('../images/01/06.PNG', R)
    cv.imwrite("data/BGR_R_colorized.png", R_colorized)
    cv.imwrite('../images/01/07.PNG', R_colorized)

    cv.destroyAllWindows()

    return


if __name__ == "__main__":

    main()
