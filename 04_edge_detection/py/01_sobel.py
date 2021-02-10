import cv2 as cv
import numpy as np


def main():

    # Load image

    img = cv.imread("data/apples.PNG")

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
    cv.imwrite('../images/01/01.PNG', img)

    # Convert image from BGR to grayscale

    img_blur = cv.GaussianBlur(img, (3, 3), 0)

    img_gray = cv.cvtColor(img_blur, cv.COLOR_BGR2GRAY)

    cv.imshow('img_gray', img_gray)
    cv.waitKey(1)
    cv.imwrite('data/img_gray.PNG', img_gray)
    cv.imwrite('../images/01/02.PNG', img_gray)

    # Compute gradients

    vertical = np.float32([-1, 0, 1, -2, 0, 2, -1, 0, 1])
    vertical = vertical.reshape((3, 3))

    vertical_edges = cv.filter2D(img_gray, cv.CV_32FC1, vertical)
    vertical_edges = np.abs(vertical_edges)
    G_x = vertical_edges/vertical_edges.max() * 255
    G_x = np.uint8(G_x)

    # G_x = cv.Sobel(img_gray, cv.CV_32F, 1, 0, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)

    cv.imshow("Vertical Edges", G_x)
    cv.waitKey(1)
    cv.imwrite("data/sobel_vertical_edges.PNG", G_x)
    cv.imwrite('../images/01/03.PNG', G_x)

    horizontal = np.float32([-1, -2, -1, 0, 0, 0, 1, 2, 1])
    horizontal = horizontal.reshape((3, 3))

    horizontal_edges = cv.filter2D(img_gray, cv.CV_32FC1, horizontal)
    horizontal_edges = np.abs(horizontal_edges)
    G_y = horizontal_edges/horizontal_edges.max() * 255
    G_y = np.uint8(G_y)

    # G_y = cv.Sobel(img_gray, cv.CV_32F, 0, 1, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)

    cv.imshow("Horizontal Edges", G_y)
    cv.waitKey(1)
    cv.imwrite("data/sobel_horizontal_edges.PNG", G_y)
    cv.imwrite('../images/01/04.PNG', G_y)

    G = np.hypot(G_x, G_y)
    G = G/G.max() * 255
    G = np.uint8(G)

    # G_x = cv.convertScaleAbs(G_x)
    # G_y = cv.convertScaleAbs(G_y)
    # G = cv.addWeighted(G_x, 0.5, G_y, 0.5, 0)

    cv.imshow("Magnitude", G)
    cv.waitKey(0)
    cv.imwrite("data/sobel_edges.PNG", G)
    cv.imwrite('../images/01/05.PNG', G)

    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":

    main()
