import cv2 as cv
import numpy as np


def main():

    img = cv.imread("./line.png", cv.IMREAD_GRAYSCALE)

    if img is None:
        print("ERROR::CV::Could not read image.")
        return -1

    img = cv.resize(img, (640, 480))

    cv.imshow("Image", img)
    cv.waitKey(0)

    edges = cv.Canny(img, 127, 255)

    lines = cv.HoughLines(edges, 1, np.pi / 180, 225, None, 0, 0)

    draw = np.ones((480, 640), dtype=np.uint8)

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

    cv.imshow("Draw", draw)
    cv.waitKey(0)

    cv.imwrite("./houghlines.png", draw)

    lines = cv.HoughLinesP(edges, 1, np.pi/180, 225, None, 50, 3)

    draw = np.ones((480, 640), dtype=np.uint8)

    if lines is not None:

        for i in range(0, len(lines)):

            l = lines[i][0]
            p1 = (l[0], l[1])
            p2 = (l[2], l[3])

            cv.line(draw, p1, p2, [255], 1, cv.LINE_AA)

    cv.imshow("Draw", draw)
    cv.waitKey(0)

    cv.imwrite("./houghlines_p.png", draw)

    cv.destroyAllWindows()

    return


if __name__ == "__main__":

    main()
