import cv2 as cv
import numpy as np


def main():

    # Load image

    img = cv.imread("data/line.png")

    if img is None:
        print("ERROR::CV::Could not read image.")
        return

    # Resize image

    rows, cols, channels = img.shape

    cv.imshow("img", img)
    cv.waitKey(1)
    cv.imwrite('../images/01/01.PNG', img)

    # Detect lines' edges

    edges = cv.Canny(img, 127, 255)

    lines = cv.HoughLines(edges, 1, np.pi / 180, 225, None, 0, 0)

    draw = np.zeros((rows, cols), dtype=np.uint8)

    if lines is not None:

        for i in range(0, len(lines)):

            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            p1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            p2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))

            cv.line(draw, p1, p2, [255], 1, cv.LINE_AA)

    cv.imshow("hough_lines", draw)
    cv.waitKey(0)
    cv.imwrite("data/hough_lines.png", draw)
    cv.imwrite('../images/01/02.PNG', draw)
    
    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":

    main()
