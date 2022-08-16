import cv2
import time
width=640
height=360
mytext='The human in frame is roni'
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
tlast=time.time()
fpsfilt=30
time.sleep(.1)


while True:
    dt=time.time()-tlast
    FPS=1/dt
    fpsfilt=fpsfilt*0.97+ FPS*0.03  #low pass filter
    print(FPS)
    tlast=time.time()
    ignore, frame = cam.read()
    #frame[140:220,220:360]=(0,0,0)
    cv2.rectangle(frame,(250,140),(420,290),(0,255,0),5)
    #cv2.circle(frame,(320,180),100,(0,0,0),4)
    cv2.putText(frame,mytext,(250,320),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),1)
    cv2.rectangle(frame,(25,25),(120,60),(0,255,255),-1)
    cv2.putText(frame,str(int(fpsfilt))+' FPS',(50,50),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,255),1)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam' , 0 ,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
cam.release()    