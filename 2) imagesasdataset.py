import numpy as np
import cv2

while True:
    frame=np.zeros([100,100,3],dtype=np.uint8)
    frame[:,:]=(0,0,255)
    cv2.imshow('My window',frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
