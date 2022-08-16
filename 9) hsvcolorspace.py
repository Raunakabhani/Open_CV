import cv2
import numpy as np

evt=0
xVal=0
yVal=0

def mouseClick(event,xPos,yPos,flag,params):
    global evt
    global xVal
    global yVal
    if(event==cv2.EVENT_LBUTTONDOWN):
        print(event)
        evt=event
        xVal=xPos
        yVal=yPos
    if event==cv2.EVENT_RBUTTONUP:
        evt=event
        print(event)

width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam',mouseClick)

while True:
    ignore, frame = cam.read()
    if evt==1:  #if left mouse click 
        x=np.zeros([250,250,3],dtype=np.uint8)   #create a size of window 250*250
        y=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        clr=y[yVal][xVal]
        print(clr)
        x[:,:]=clr
        cv2.putText(x,str(clr),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
        cv2.imshow('color picker',x)
        cv2.moveWindow('color picker',width,0)
        evt=0
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam', 0 ,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
cam.release()    