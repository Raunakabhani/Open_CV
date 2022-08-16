import cv2

width=640
height=360
mytext='The human in frame is roni'
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))


while True:
    ignore, frame = cam.read()
    #frame[140:220,220:360]=(0,0,0)
    cv2.rectangle(frame,(250,140),(420,290),(0,255,0),5)
    #cv2.circle(frame,(320,180),100,(0,0,0),4)
    #cicle ni code live imshow ni code ni upar j hovi joy baki circle dekhase nai
    cv2.putText(frame,mytext,(250,320),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),1)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam' , 0 ,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
cam.release()    