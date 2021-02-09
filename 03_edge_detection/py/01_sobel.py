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
    cv.waitKey(0)

    # Convert image from BGR to grayscale

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    vertical = np.float32([-1, 0, 1, -2, 0, 2, -1, 0, 1])
    vertical = vertical.reshape((3, 3))

    vertical_edges = cv.filter2D(img, cv.CV_32FC1, vertical)
    vertical_edges = np.abs(vertical_edges)
    G_x = vertical_edges/vertical_edges.max() * 255
    G_x = np.uint8(G_x)

    cv.imshow("Vertical Edges", G_x)
    cv.waitKey(0)
    cv.imwrite("data/sobel_vertical_edges.png", G_x)

    horizontal = np.float32([-1, -2, -1, 0, 0, 0, 1, 2, 1])
    horizontal = horizontal.reshape((3, 3))

    horizontal_edges = cv.filter2D(img, cv.CV_32FC1, horizontal)
    horizontal_edges = np.abs(horizontal_edges)
    G_y = horizontal_edges/horizontal_edges.max() * 255
    G_y = np.uint8(G_y)

    cv.imshow("Horizontal Edges", G_y)
    cv.waitKey(0)
    cv.imwrite("data/sobel_horizontal_edges.png", G_y)

    G = np.hypot(G_x, G_y)
    G = G/G.max() * 255
    G = np.uint8(G)

    cv.imshow("Magnitude", G)
    cv.waitKey(0)
    cv.imwrite("data/sobel_edges.png", G)

    return


if __name__ == "__main__":

    main()