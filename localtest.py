#!/usr/bin/python3
# coding=utf-8
# Copyright(C) Team #6392 Dimension Creators

import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

min_hue, min_sat, min_val = 35, 43, 30
max_hue, max_sat, max_val = 77, 255, 255
kernel = np.ones((7, 7), np.uint8)

if not cap.isOpened():
    print("No Cameras Detected!")
    # frame = cv2.imread("C:\\Users\\Leo\\Desktop\\image.bmp", flags=cv2.IMREAD_UNCHANGED)
    # hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    # binary_img = cv2.inRange(
    #     hsv, (min_hue, min_sat, min_val), (max_hue, max_sat, max_val))
    # for i in range(0, 5):
    #     binary_img = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, kernel)
    # for i in range(0, 5):
    #     binary_img = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, kernel)
    # a, contours, b = cv2.findContours(
    #     binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(frame, contours, -1, (204, 1195, 49), 5)
    # while True:
    #     cv2.namedWindow('binary_img')
    #     cv2.namedWindow('original_img')
    #     cv2.imshow('binary_img', binary_img)
    #     cv2.imshow('original_img', frame)

else:
    while True:
        ret, frame = cap.read()
        t1 = time.time_ns()
        if not ret:
            break
        else:
            hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
            binary_img = cv2.inRange(
                hsv, (min_hue, min_sat, min_val), (max_hue, max_sat, max_val))

            for i in range(0, 5):
                binary_img = cv2.morphologyEx(
                    binary_img, cv2.MORPH_OPEN, kernel)

            for i in range(0, 5):
                binary_img = cv2.morphologyEx(
                    binary_img, cv2.MORPH_CLOSE, kernel)

            a, contours, b = cv2.findContours(
                image=binary_img, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(frame, contours, contourIdx=-1,
                             thickness=5, color=(204, 195, 49))

            t2 = time.time_ns()
            fps = "FPS: " + str(int(1/((t2 - t1) * (10**-9))))
            cv2.putText(img=frame, text=fps, org=(
                0, 15), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(218, 178, 217))

            cv2.imshow('binary_img', binary_img)
            cv2.imshow('color_img', frame)

            if cv2.waitKey(1) and 0xFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()
