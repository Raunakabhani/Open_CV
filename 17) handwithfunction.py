import cv2
import mediapipe as mp

width=640
height=360

mp_hands=mp.solutions.hands
hands1=mp_hands.Hands(False,2,0.5,0.5)
mpDraw=mp.solutions.drawing_utils

def parselandmark(frame):
    myhandsxy=[]
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands1.process(frameRGB)
    if results.multi_hand_landmarks:
        for handlandmarks in results.multi_hand_landmarks:
            myhandxy=[] 
            for landmark in handlandmarks.landmark:
                myhandxy.append((int(landmark.x*width),int(landmark.y*height)))
                myhandsxy.append(myhandxy)
    return myhandsxy


cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))


while True:
    ignore, frame = cam.read()  
    callfun=parselandmark(frame)
    for hand in callfun:
        cv2.circle(frame,hand[8],25,(255,0,255),4)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam' , 0 ,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
cam.release()    