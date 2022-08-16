import cv2
from cv2 import COLOR_BGR2GRAY

width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))


while True:
    ignore, frame = cam.read()

    #small coloured frame beside main coloured frame 
    frameROI=frame[150:210,250:390]
    cv2.imshow('my ROI',frameROI)
    cv2.moveWindow('my ROI' , 650 ,0)

    #converting small coloured frame into small gray frame
    frameROIGray=cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray frame',frameROIGray)
    cv2.moveWindow('gray frame',650,100)
 
    #big frame ni andar small gray region  
    frameROIBGR=cv2.cvtColor(frameROIGray,cv2.COLOR_GRAY2BGR)
    frame[150:210,250:390]=frameROIBGR


    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam' , 0 ,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
cam.release()    