import cv2
#from cv2 import EVENT_LBUTTONDBLCLK
#from cv2 import EVENT_LBUTTONDOWN
evt=0

"""
when i run ,even after declaring global variable , it will crash because , global variable is inside the funct 
and the fun is not used as mouse is not clicked in starting , so just declare evt as 0 in starting of programme so programme does not crash 
"""

def mouseClick(event,xPos,yPos,flags,params):
    global evt
    global xposition
    global yposition 
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse event was:',event)
        print('at position',xPos,yPos)
        evt = event 
        xposition=xPos
        yposition=yPos

    if event==cv2.EVENT_LBUTTONUP:
        print('mouse event was:',event)
        print('at position',xPos,yPos)
        evt = event 
        xposition=xPos
        yposition=yPos


#event,xpos,ypos is a local variable, so if i use it in while loop ,it wont recognize
#so we have to make a global variable and make its value equal to local variable 


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

    if evt==1 or evt==4 :
        cv2.circle(frame,(xposition,yposition),100,(0,0,0),4)
    
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam' , 0 ,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
cam.release()    