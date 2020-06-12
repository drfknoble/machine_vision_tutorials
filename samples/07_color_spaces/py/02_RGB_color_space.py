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

    # Covert from BGR color space to RGB color space

    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Get blue, green, and red channels

    R = rgb_img[:, :, 0]
    G = rgb_img[:, :, 1]
    B = rgb_img[:, :, 2]

    R_colorized = np.zeros((rows, cols, 3), dtype=np.uint8)
    R_colorized[:, :, 2] = R

    cv.imshow("R_colorized", R_colorized)
    cv.waitKey(0)
    cv.imwrite("data/RGB_R.png", R)  
    cv.imwrite("data/RGB_R_colorized.png", R_colorized)
   
    G_colorized = np.zeros((rows, cols, 3), dtype=np.uint8)
    G_colorized[:, :, 1] = G

    cv.imshow("G_colorized", G_colorized)
    cv.waitKey(0)  
    cv.imwrite("data/RGB_G.png", G)  
    cv.imwrite("data/RGB_G_colorized.png", G_colorized)

    B_colorized = np.zeros((rows, cols, 3), dtype=np.uint8)
    B_colorized[:, :, 0] = B

    cv.imshow("B_colorized", B_colorized)
    cv.waitKey(0)
    cv.imwrite("data/RGB_B.png", B)  
    cv.imwrite("data/RGB_B_colorized.png", B_colorized)
    

    cv.destroyAllWindows()

    return

if __name__ == "__main__":

    main()