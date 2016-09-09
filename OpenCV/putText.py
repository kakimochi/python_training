#coding: UTF-8

import numpy as np
import cv

img = cv.imread('hoge.jpg', 0)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'hogehoge', (10, 500), font, 4, (255,255,255),2,cv.LINE_AA)
