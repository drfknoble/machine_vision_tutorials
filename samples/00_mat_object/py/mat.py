# %%

import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 1), dtype=np.uint8)

cv.rectangle(img, (100, 100,), (400, 400), 255, -1)

cv.imshow("img", img)
cv.waitKey(1)

background_img_1 = np.zeros((480, 640, 1), dtype=np.uint8)
background_img_2 = np.zeros((480, 640, 1), dtype=np.uint8)

cv.rectangle(background_img_1, (150, 150,), (350, 350), 255, -1)
cv.rectangle(background_img_2, (200, 200,), (450, 450), 255, -1)

background_img = background_img_1 + background_img_2

cv.imshow("background_img", background_img)
cv.waitKey(1)

sub_img = img - background_img

cv.imshow("sub_img", sub_img)
cv.waitKey(0)

cv.destroyAllWindows()

