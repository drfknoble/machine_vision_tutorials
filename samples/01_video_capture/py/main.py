import cv2 as cv
import numpy as np

def main():

    camera = cv.VideoCapture(0)

    if not camera.isOpened():
        return 1

    while True:

        ret, frame = camera.read()

        cv.imshow("frame", frame)
        
        i = cv.waitKey(30)

        if i == 27:
            break

    return


if __name__ == "__main__":

    main()