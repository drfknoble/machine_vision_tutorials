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
    cv.imwrite('../images/02/01.PNG', img)

    # Detect lines' edges

    edges = cv.Canny(img, 127, 255)

    lines = cv.HoughLinesP(edges, 1, np.pi/180, 225, None, 50, 3)

    draw = np.zeros((rows, cols), dtype=np.uint8)

    if lines is not None:

        for i in range(0, len(lines)):

            l = lines[i][0]
            p1 = (l[0], l[1])
            p2 = (l[2], l[3])

            cv.line(draw, p1, p2, [255], 1, cv.LINE_AA)

    cv.imshow("prob_hough_lines", draw)
    cv.waitKey(0)
    cv.imwrite("data/prob_hough_lines.png", draw)
    cv.imwrite('../images/02/02.PNG', draw)

    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":

    main()
