import os

import cv2
import numpy as np

# img = cv2.imread('..\\images\\all_and_lee.PNG')
img = cv2.imread('C:\\Users\\Boaz Azulay\\Desktop\\test.JPEG')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('..\\images\\lee.PNG',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

flag = False
for pt in zip(*loc[::-1]):
    if pt is not None:
        flag = True
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)

print(flag)
cv2.imshow('detected', img)

# leesin_img = cv2.imread('C:\\Users\\Boaz Azulay\\Desktop\\lee.PNG',0)
# cv2.imshow('image', leesin_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
