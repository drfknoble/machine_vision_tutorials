import cv2 as cv
import numpy as np

def main():

    # Load image

    img = cv.imread("data/apples.png")

    if img is None:
        return

    # Resize image

    rows, cols, channels = img.shape
    
    rows = rows // 2
    cols = cols // 2

    img = cv.resize(img, (cols, rows))

    cv.imshow("img", img)
    cv.waitKey(0)

    # Kernel, K = [0, 0, 0; 0, 1, 0; 0, 0, 0]

    kernel = np.float32([0, 0, 0, 0, 1, 0, 0, 0, 0])
    kernel = kernel.reshape((3, 3))

    I_img = cv.filter2D(img, cv.CV_8UC3, kernel)

    cv.imshow("Identity Image", I_img)
    cv.waitKey(0)
    cv.imwrite("data/I_img.png", I_img)

    # Kernel, K = [0, -1, 0; -1, 5, -1; 0, -1, 0]

    kernel = np.float32([0, -1, 0, -1, 5, -1, 0, -1, 0])
    kernel = kernel.reshape((3, 3))

    I_img = cv.filter2D(img, cv.CV_8UC3, kernel)

    cv.imshow("Sharpened Image", I_img)
    cv.waitKey(0)
    cv.imwrite("data/sharp_img.png", I_img)

    # Kernel, K = 1/9 * [1, 1, 1; 1, 1, 1; 1, 1, 1]

    kernel = 1.0/9.0 * np.float32([1, 1, 1, 1, 1, 1, 1, 1, 1])
    kernel = kernel.reshape((3, 3))

    box_img = cv.filter2D(img, cv.CV_8UC3, kernel)

    cv.imshow("Box Blurred Image", box_img)
    cv.waitKey(0)
    cv.imwrite("data/box_img.png", box_img)

    # Kernel, K = 1/16 * [1, 2, 1; 2, 4, 2; 1, 2, 1]

    kernel = 1.0/16.0 * np.float32([1, 2, 1, 2, 4, 2, 1, 2, 1])
    kernel = kernel.reshape((3, 3))

    box_img = cv.filter2D(img, cv.CV_8UC3, kernel)

    cv.imshow("Gaussian Blurred Image", box_img)
    cv.waitKey(0)
    cv.imwrite("data/gaussian_img.png", box_img)

    # Kernel, K = [1, 0, 0; 0, 1, 0; 0, 0, 1]

    kernel = np.float32([1, 0, 0, 0, 1, 0, 0, 0, 1])
    kernel = kernel.reshape((3, 3))

    I3_img = cv.filter2D(img, cv.CV_8UC3, kernel)
  
    cv.imshow("Eye(3) Image", I3_img)
    cv.waitKey(0)
    cv.imwrite("data/I3_img.png", I3_img)

    # Kernel, K = [0, 1, 0; 1, -4, 1; 0, 1, 0]

    kernel = np.float32([-1, -1, -1, -1, 8, -1, -1, -1, -1])
    kernel = kernel.reshape((3, 3))

    edge_img = cv.filter2D(img, cv.CV_8UC3, kernel)
  
    cv.imshow("Edges Image", edge_img)
    cv.waitKey(0)
    cv.imwrite("data/edge_img.png", edge_img)

    cv.destroyAllWindows()

    return


if __name__ == "__main__":

    main()