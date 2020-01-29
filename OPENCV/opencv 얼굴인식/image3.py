import cv2
import sys
import dlib
import numpy as np

scaler = 0.3

cap = cv2.VideoCapture('snow.mp4')

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat') #사람얼굴 특징을 68개 점으로 추출
while True:
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.resize(img, (int(img.shape[1] * scaler), int(img.shape[0] * scaler)))
    ori = img.copy()

    # 얼굴 찾기
    faces = detector(img)
    face = faces[0]

    dlib_shape = predictor(img, face)  # img의 얼굴 영역안의 특징점 찾기
    # 연산을 쉽게하기 위해서 행렬로 바꾸고 shpe_2d로 저장
    shape_2d = np.array([[p.x,p.y] for p in dlib_shape.parts()])#dlib객체를 numpy 객체로 변환



    # visualize
    img = cv2.rectangle(img, pt1=(face.left(), face.top()),
                        pt2=(face.right(), face.bottom()), color=(255, 255, 255),
                        thickness=2, lineType=cv2.LINE_AA)

    for s in shape_2d:
        cv2.circle(img, center=tuple(s),radius=1, color=(255,255,255),
        thickness=2, lineType=cv2.LINE_AA)#원그리기(얼굴의 특징점 68ea)

    cv2.imshow('img', img)
    cv2.waitKey(1)