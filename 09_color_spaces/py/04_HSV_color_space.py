import cv2 as cv

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
    cv.imwrite('../images/04/01.PNG', img)

    # Convert from BGR color space to HSV

    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    cv.imshow("HSV", hsv_img)
    cv.waitKey(1)
    cv.imwrite("data/hsv.PNG", hsv_img)
    cv.imwrite('../images/04/02.PNG', hsv_img)

    H = hsv_img[:, :, 0]
    S = hsv_img[:, :, 1]
    V = hsv_img[:, :, 2]
    
    cv.imshow("H", H)
    cv.waitKey(1)
    cv.imwrite("data/hsv_H.PNG", H)
    cv.imwrite('../images/04/03.PNG', H)

    cv.imshow("S", S)
    cv.waitKey(1)
    cv.imwrite("data/hsv_S.PNG", S)
    cv.imwrite('../images/04/04.PNG', S)
    
    cv.imshow("V", V)
    cv.waitKey(0)
    cv.imwrite("data/hsv_V.PNG", V)
    cv.imwrite('../images/04/05.PNG', V)
    
    cv.destroyAllWindows()

    return 0

if __name__ == "__main__":

    main()