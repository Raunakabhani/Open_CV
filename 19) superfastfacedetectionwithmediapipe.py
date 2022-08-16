from unittest import result
import cv2
from cv2 import COLOR_BGR2RGB
import mediapipe as mp
print(cv2.__version__)

width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

findface=mp.solutions.face_detection.FaceDetection()
drawface=mp.solutions.drawing_utils


while True:
    ignore, frame = cam.read()   #to grab single frame of video
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=findface.process(frameRGB)
    if results.detections!=None:
        for face in results.detections:
            bbox=face.location_data.relative_bounding_box
            topleft=(int(bbox.xmin*width),int(bbox.ymin*height))
            bottomRight=(int((bbox.xmin+bbox.width)*width),int((bbox.ymin+bbox.height )*height))
            cv2.rectangle(frame,topleft,bottomRight,(0,255,0),5)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam' , 0 ,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
cam.release()    