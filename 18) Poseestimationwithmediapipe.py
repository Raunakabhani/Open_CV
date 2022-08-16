import cv2
import mediapipe as mp

print(cv2.__version__)

width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

#1st paratmer for still image 
#2nd parameter for looking only at upper body 
#3rd parameter is for smooothing the data points 

pose=mp.solutions.pose.Pose(False,False,True,0.5,0.5)
mpDraw=mp.solutions.drawing_utils

while True:
    ignore, frame = cam.read()   #to grab single frame of video
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=pose.process(frameRGB)
    landmarks=[]
    print(results)
    if results.pose_landmarks != None :
        mpDraw.draw_landmarks(frame,results.pose_landmarks,mp.solutions.pose.POSE_CONNECTIONS)
        #print(results.pose_landmarks.landmark)
        for lm in results.pose_landmarks.landmark:
            #print((lm.x,lm.y))
            landmarks.append((int(lm.x*width),int(lm.y*height)))
            print(landmarks)
        cv2.circle(frame,landmarks[0],20,(0,255,0),3)

    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam' , 0 ,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
cam.release()    