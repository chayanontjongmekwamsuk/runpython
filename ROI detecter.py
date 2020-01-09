#!/usr/bin/env python
# coding: utf-8


import cv2
import numpy as np

print("welcome to ROI detector")

def getROI(img):
    cv2.circle(img , (100,100), 10, (255, 255, 255), -1)
    ROI = 2.1
    return img,ROI
