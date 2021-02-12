import cv2 as cv
import numpy as np

def main():

    camera = cv.VideoCapture(0)

    if not camera.isOpened():
        print('ERROR::CV::Could not open video device.')
        return 1

    while True:

        ret, frame = camera.read()

        if ret is True:
            cv.imshow("frame", frame)
        
        i = cv.waitKey(30)

        if i == 27:
            cv.imwrite('../images/01/01.PNG', frame)
            break

    cv.destroyAllWindows()

    return 0


if __name__ == "__main__":

    main()