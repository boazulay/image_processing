import os
import time

import cv2
import numpy as np
from PIL import ImageGrab

def jungler_arrive():
    print("jungler_arrive not implemted yets")

def jungler_missing():
    print("jungler_missing not implemted yets")

time_to_sleep=1

while True:
    time.sleep(time_to_sleep)
    screenshot = ImageGrab.grab()
    screenshot.save("new.png")
    img = cv2.imread("new.png")
    # img = cv2.imread('..\\images\\all_and_lee.PNG')
    # img = cv2.imread('..\\images\\no_match.JPEG')
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
        # cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)

    if flag == True:
        jungler_arrive()
    else:
        jungler_missing()
    
    # cv2.imshow('detected', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
