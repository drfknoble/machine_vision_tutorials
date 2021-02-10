import cv2 as cv

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
    cv.imwrite('../images/03/01.PNG', img)

    # Convert from BGR color space to YUV

    yuv_img = cv.cvtColor(img, cv.COLOR_BGR2YUV)

    cv.imshow("YUV", yuv_img)
    cv.waitKey(1)
    cv.imwrite("data/YUV.png", yuv_img)
    cv.imwrite('../images/03/02.PNG', yuv_img)

    Y = yuv_img[:, :, 0]
    U = yuv_img[:, :, 1]
    V = yuv_img[:, :, 2]
    
    cv.imshow("Y", Y)
    cv.waitKey(1)
    cv.imwrite("data/YUV_Y.png", Y)
    cv.imwrite('../images/03/03.PNG', Y)

    cv.imshow("U", U)
    cv.waitKey(1)
    cv.imwrite("data/YUV_U.png", U)
    cv.imwrite('../images/03/04.PNG', U)
    
    cv.imshow("V", V)
    cv.waitKey(0)
    cv.imwrite("data/YUV_V.png", V)
    cv.imwrite('../images/03/05.PNG', V)
    
    cv.destroyAllWindows()

    return

if __name__ == "__main__":

    main()