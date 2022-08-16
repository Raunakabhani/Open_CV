import cv2
from cv2 import circle
import mediapipe as mp 
print(cv2.__version__)

width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

#1 static image or not
#no of faces 
facemesh=mp.solutions.face_mesh.FaceMesh(False,3,0.5,0.5)
mpdraw=mp.solutions.drawing_utils
drawspecircle=mpdraw.DrawingSpec(thickness=1,circle_radius=2,color=(255,0,0))
drawspelines=mpdraw.DrawingSpec(thickness=1,circle_radius=2,color=(0,0,255))


while True:
    ignore, frame = cam.read()   #to grab single frame of video
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=facemesh.process(frameRGB)
    if results.multi_face_landmarks != None:
            for facelandmarks in results.multi_face_landmarks:
                mpdraw.draw_landmarks(frame,facelandmarks,mp.solutions.face_mesh.FACE_CONNECTIONS,drawspecircle,drawspelines)
                index=0
                for lm in facelandmarks.landmark:
                    cv2.putText(frame,str(index),(int(lm.x*width),int(lm.y*height)),cv2.FONT_HERSHEY_COMPLEX,0.2,(0,255,0),1)  
                    index=index+1             
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam' , 0 ,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
cam.release()    