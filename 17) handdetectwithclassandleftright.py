from pickle import NONE
from unittest import result
import cv2

class mphands:
    import mediapipe as mp
    def __init__(self,maxhands=2,tol1=0.5,tol2=0.5):
        self.hands=self.mp.solutions.hands.Hands(False,maxhands,tol1,tol2)
    def Marks(self,frame):
        myhands=[]
        handstype=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            #print(results.multi_handedness) # it prints left or right hand shown in pic (but result is opposite)
            for hand in results.multi_handedness:
                print(hand.classification[0].label)
                hand_type=hand.classification[0].label
                handstype.append(hand_type)
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landmark in handLandMarks.landmark:
                    myHand.append((int(landmark.x*width),int(landmark.y*height)))
                myhands.append(myHand)
        return myhands,handstype


width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findhands=mphands(2)#no of hands to be detected  


while True:
    ignore, frame = cam.read()   #to grab single frame of video
    
    handdata,handstype=findhands.Marks(frame)
    for hand,handtype in zip(handdata,handstype):
        if handtype=='Right':
            handcolor=(255,0,0)
        elif handtype=='Left':
            handcolor=(0,255,0)

        for ind in [0,5,6,7,8]:
            #cv2.circle(frame,hand[ind],25,handcolor,3)
            cv2.circle(frame,hand[9],125,handcolor,3)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam' , 0 ,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
cam.release()    