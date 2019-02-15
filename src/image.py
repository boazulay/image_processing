import os
import time

import cv2
import numpy as np
from PIL import ImageGrab
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

def make_a_sound():
    print('Make a sound')
    winsound.Beep(frequency, duration)

def jungler_arrive():
    make_a_sound()
    print("jungler_arrive not implemted yets")

def screenshot():
    screenshot = ImageGrab.grab().save("screenshot.png")
    img = cv2.imread("screenshot.png")
    return img

def is_jungler(loc):
    print(loc[0])
    print(loc[1])
    mid_x = int(len(loc[0])/2)
    mid_y = int(len(loc[1])/2)
    if loc[0].any():
        print(loc[0][mid_x])
        print(loc[1][mid_y])
        jungler_arrive()


# def is_jungler(loc):
#     print(loc)
#     for pt in zip(*loc[::-1]):
#         print(pt)
#         if pt is not None:
#             jungler_arrive()
#             # cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)
#         else:
#             jungler_missing()
#         break



time_to_sleep=1
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 200  # Set Duration To 1000 ms == 1 second

while True:
    print('######################')
    time.sleep(time_to_sleep)

    img = screenshot()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('..\\images\\lee.PNG',0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    # print(loc)
    
    is_jungler(loc)
    