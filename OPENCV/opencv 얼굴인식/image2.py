import cv2
import sys
import dlib
import numpy as np

scaler = 0.3

cap = cv2.VideoCapture('snow.mp4')


detector = dlib.get_frontal_face_detector() #얼굴 디렉터 모듈 초기화
#머신러닝으로 학습된 모델
#predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat') # 얼굴 특징점 모듈 초기화


while True:
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.resize(img, (int(img.shape[1] * scaler), int(img.shape[0] * scaler)))
    ori = img.copy() #원본 저장

    #얼굴 찾기
    faces = detector(img) #img에서 얼굴 찾기
    face = faces[0] #여러 얼굴이 나오므로 얼굴 하나만 가져오기


    #visualize
    img = cv2.rectangle(img, pt1=(face.left(), face.top()),
    pt2=(face.right(), face.bottom()), color=(255,255,255),
    thickness=2, lineType=cv2.LINE_AA) #얼굴 네모난 모양으로 표시, 좌상단 우하단 좌표



    cv2.imshow('img',img)
    cv2.waitKey(1)