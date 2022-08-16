import cv2

xposition=0
yposition=0
def mycallBack1(xpos):
    print('xPos:',xpos)
    global xposition
    xposition=xpos
def mycallBack2(ypos):
    print('yPos',ypos)
    global yposition
    yposition=ypos

#width and height ne directly taskbar thi change nai thai karan k ane ek fixed ratio hoi 16:9 no
#so anu calculation thodu batadvu padse 

def mycallBack3(val):
    print('yPos',val)
    global width
    width=val
    height=int(width*9/16)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

width=640
height=360

cv2.namedWindow('myTrackbars')
cv2.resizeWindow('myTrackbars',400,100)
cv2.moveWindow('myTrackbars',640,0)
cv2.createTrackbar('xPos','myTrackbars',0,640,mycallBack1)
cv2.createTrackbar('yPos','myTrackbars',0,360,mycallBack2)
cv2.createTrackbar('width','myTrackbars',width,1920,mycallBack3)



cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))


while True:
    cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
    ignore, frame = cam.read()
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam' , xposition ,yposition)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
cam.release()    