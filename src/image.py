import os
import time

import cv2
import numpy as np
from PIL import ImageGrab
import winsound
import wx


def make_a_sound():
    print('Make a sound')
    winsound.Beep(frequency, duration)

def jungler_arrive(x, y):
    print("jungler_arrive")
    make_a_sound()
    print("Jengler postion:", x, y)
    s.DrawRectangle(x, y, 10, 10)

def screenshot():
    screenshot = ImageGrab.grab().save("screenshot.png")
    img = cv2.imread("screenshot.png")
    return img

def is_jungler(loc):
    if loc[0].any():
        y = loc[0][int(len(loc[0])/2)]
        x = loc[1][int(len(loc[1])/2)]
        jungler_arrive(x, y)



time_to_sleep=1
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 200  # Set Duration To 1000 ms == 1 second
app = wx.App(False)
s = wx.ScreenDC()
s.StartDrawingOnTop
s.Pen = wx.Pen("#FF0000")

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
    