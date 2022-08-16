import cv2
import numpy as np


video=cv2.VideoCapture('solidWhiteRight.mp4')
while True:
    ret,frame = video.read()
    if not ret:
        video=video=cv2.VideoCapture('solidWhiteRight.mp4')
        continue
        
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
video.release()    
cv2.destroyAllWindows()