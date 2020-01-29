import cv2 #opencv-python
import sys
import dlib #pip install CMake  ,  dlib
import numpy as np

scaler = 0.3 #화면크기를 줄이기 위한 용도

cap = cv2.VideoCapture('girl.mp4')
#cv2.imread 이미지 읽기

while True:
    ret, img = cap.read()
    if not ret:
        break #프레임을 읽어들이지 못하면 종료

    img = cv2.resize(img, (int(img.shape[1] * scaler), int(img.shape[0] * scaler))) #이미지를 띄우기전 화면 조절

    cv2.imshow('img',img)#'img'라는 이름의 윈도우에 img를 띄우기
    cv2.waitKey(1) #1초 대기 : 동영상 잘보이게 하는 용도