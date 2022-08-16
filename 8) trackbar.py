import cv2

"""
when i run ,even after declaring global variable , it will crash because , global variable is inside the funct 
and the fun is not used as mouse is not clicked in starting , so just declare evt as 0 in starting of programme so programme does not crash 
"""
xposition=0
yposition=0

#event,xpos,ypos is a local variable, so if i use it in while loop ,it wont recognize
#so we have to make a global variable and make its value equal to local variable 

def mycallBack1(xpos):
    print('xPos:',xpos)
    global xposition
    xposition=xpos
def mycallBack2(ypos):
    print('yPos',ypos)
    global yposition
    yposition=ypos
    
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

""" this fun creates a window that can be used as a placeholder for image and trackbars
created windows are referred to by their image """

cv2.namedWindow('myTrackbars')
cv2.resizeWindow('myTrackbars',400,100)
cv2.moveWindow('myTrackbars',width,0)
cv2.createTrackbar('xPos','myTrackbars',0,1920,mycallBack1)
cv2.createTrackbar('yPos','myTrackbars',0,1920,mycallBack2)

while True:
    ignore, frame = cam.read()
    cv2.circle(frame,(xposition,yposition),25,(0,0,0),4) 
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam' , 0 ,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
cam.release()    