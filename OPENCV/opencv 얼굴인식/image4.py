import cv2
import sys
import dlib
import numpy as np

scaler = 0.3

cap = cv2.VideoCapture('snow.mp4')

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
while True:
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.resize(img, (int(img.shape[1] * scaler), int(img.shape[0] * scaler)))  # 이미지를 띄우기전 화면 조절
    ori = img.copy()

    faces = detector(img)
    face = faces[0]

    dlib_shape = predictor(img, face)
    shape_2d = np.array([[p.x,p.y] for p in dlib_shape.parts()])

    #computer center of face
    #특징점을 찾은 이유 : 얼굴의 좌상단, 우하단을 구해 얼굴의 사이즈, 중심을 구함\
    top_left = np.min(shape_2d, axis=0)#좌 상단 점
    bottom_right = np.max(shape_2d, axis=0)#우 하단 점
    center_x, center_y = np.mean(shape_2d, axis=0).astype(np.int)#중심


    img = cv2.rectangle(img, pt1=(face.left(), face.top()),
                        pt2=(face.right(), face.bottom()), color=(255, 255, 255),
                        thickness=2, lineType=cv2.LINE_AA)

    for s in shape_2d:
        cv2.circle(img, center=tuple(s),radius=1, color=(255,255,255),
        thickness=2, lineType=cv2.LINE_AA)

    cv2.circle(img, center=tuple(top_left),radius=1,
               color=(255,0,0),thickness=2, lineType=cv2.LINE_AA)#센터 좌표만 다름
    cv2.circle(img, center=tuple(bottom_right),radius=1,
               color=(255,0,0),thickness=2, lineType=cv2.LINE_AA)#센터 좌표만 다름
    cv2.circle(img, center=tuple((center_x, center_y)), radius=1,
               color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA)  # 센터 좌표만 다름

    cv2.imshow('img', img)
    cv2.waitKey(1)