import cv2
import numpy as np

def ontrack1(val):
    global huelow 
    huelow=val
    print('Hue low',huelow)

def ontrack2(val):
    global huehigh
    huehigh=val
    print('Hue high',huehigh)

def ontrack3(val):
    global satlow 
    satlow=val
    print('Sat low',satlow)

def ontrack4(val):
    global sathigh 
    sathigh=val
    print('Sat high',sathigh)

def ontrack5(val):
    global vallow 
    vallow=val
    print('Val low',vallow)

def ontrack6(val):
    global valhigh 
    valhigh=val
    print('Val high',valhigh)


width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

huelow=10
huehigh=20
satlow=10
sathigh=250
vallow=10
valhigh=250

cv2.namedWindow('myTrackbars')
cv2.resizeWindow('myTrackbars',400,270)
cv2.moveWindow('myTrackbars',width,0)
cv2.createTrackbar('hue low','myTrackbars',10,179,ontrack1)
cv2.createTrackbar('hue high','myTrackbars',31,179,ontrack2)
cv2.createTrackbar('sat low','myTrackbars',66,255,ontrack3)
cv2.createTrackbar('sat high','myTrackbars',255,255,ontrack4)
cv2.createTrackbar('val low','myTrackbars',193,255,ontrack5)
cv2.createTrackbar('val high','myTrackbars',255,255,ontrack6)




while True:
    ignore, frame = cam.read()
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerBOUND=np.array([huelow,satlow,vallow])
    upperBOUND=np.array([huehigh,sathigh,valhigh])
    mymask=cv2.inRange(frameHSV,lowerBOUND,upperBOUND)
    #mymask=cv2.bitwise_not(mymask)   #j color detectection mate value set kariche trackbar ma  ,ana sivay nu badhu batadse a 
    myobject=cv2.bitwise_and(frame,frame,mask=mymask)
    mysmallobject=cv2.resize(myobject,(int(width/2),int(height/2)))
    cv2.imshow('my object',mysmallobject)
    cv2.moveWindow('my object',int(width/2),int(height))
    cv2.imshow('my mask',mymask)
    mysmallmask=cv2.resize(mymask,(int(width/2),int(height/2)))
    cv2.imshow('my mask',mysmallmask)
    cv2.moveWindow('my mask',0,height)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam' , 0 ,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
cam.release()    