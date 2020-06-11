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

    # The manual implementation of the Canny algorithm is a bit slow, so
    print("Please wait...")

    # Convert image from BGR to grayscale

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Gaussian Blurring

    blur = cv.GaussianBlur(gray, (5, 5), 0)

    cv.imwrite("data/manual_canny_blurred.png", blur)

    # Apply Sobel operator

    sobelx_64 = cv.Sobel(blur, cv.CV_32F, 1, 0, ksize=3)
    absx_64 = np.absolute(sobelx_64)
    sobelx_8u1 = absx_64/absx_64.max()*255
    G_x = np.uint8(sobelx_8u1)

    sobely_64 = cv.Sobel(blur, cv.CV_32F, 0, 1, ksize=3)
    absy_64 = np.absolute(sobely_64)
    sobely_8u1 = absy_64/absy_64.max()*255
    G_y = np.uint8(sobely_8u1)

    # Compute gradient magnitude

    G = np.hypot(G_x, G_y)
    G = G/G.max()*255
    G = np.uint8(G)

    # Compute gradient angle

    theta = np.arctan2(sobely_64, sobelx_64)
    angle = np.rad2deg(theta)

    cv.imwrite("data/manual_canny_G.png", G)

    # Non-maximum suppression

    non_max = np.zeros((rows, cols), dtype=np.uint8)

    for i in range(1, rows-1):

        for j in range(1, cols-1):

            # Horizontal 0
            if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180) or (-22.5 <= angle[i, j] < 0) or (-180 <= angle[i, j] < -157.5):

                b = G[i, j+1]
                c = G[i, j-1]

            # Diagonal 45
            elif (22.5 <= angle[i, j] < 67.5) or (-157.5 <= angle[i, j] < -112.5):

                b = G[i+1, j+1]
                c = G[i-1, j-1]

            # Vertical 90
            elif (67.5 <= angle[i, j] < 112.5) or (-112.5 <= angle[i, j] < -67.5):

                b = G[i+1, j]
                c = G[i-1, j]

            # Diagonal 135
            elif (112.5 <= angle[i, j] < 157.5) or (-67.5 <= angle[i, j] < -22.5):

                b = G[i+1, j-1]
                c = G[i-1, j+1]

            # Non-max Suppression
            if (G[i, j] >= b) and (G[i, j] >= c):

                non_max[i, j] = G[i, j]

            else:

                non_max[i, j] = 0

    cv.imwrite("data/manual_canny_non_max.png", non_max)

    # Double threshold

    highThreshold = 30
    lowThreshold = 10

    out = np.zeros((rows, cols), dtype=np.uint8)

    strong_i, strong_j = np.where(non_max >= highThreshold)
    zeros_i, zeros_j = np.where(non_max < lowThreshold)

    weak_i, weak_j = np.where((non_max <= highThreshold) & (non_max >= lowThreshold))

    # Hysteresis

    out[strong_i, strong_j] = 255
    out[zeros_i, zeros_j] = 0
    out[weak_i, weak_j] = 128

    for i in range(1, rows-1):

        for j in range(1, cols-1):

            if (out[i, j] == 128):

                if 255 in [out[i+1, j-1], out[i+1, j], out[i+1, j+1], out[i, j-1], out[i, j+1], out[i-1, j-1], out[i-1, j], out[i-1, j+1]]:

                    out[i, j] = 255

                else:

                    out[i, j] = 0

    print("Done")

    cv.imshow("Manual Canny", out)
    cv.waitKey(0)
    cv.imwrite("data/manual_canny.png", G)

    cv.destroyAllWindows()

    return


if __name__ == "__main__":

    main()
