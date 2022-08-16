import cv2

width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade=cv2.CascadeClassifier('haar\data/haarcascade_frontalface_default.xml')
eyeCascade=cv2.CascadeClassifier('haar\data/haarcascade_eye.xml')


while True:
    ignore, frame = cam.read()
    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(frameGray,1.3,5)
    for face in faces:
        x,y,w,h=face
        cv2.rectangle(frameGray,(x,y),(x+w,y+h),(255,0,0),3)
        #searchinng eye only if face is found, to decrease computational power
        frameROI=frame[y:y+h,x:x+w]
        frameROIGray=cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
        eyes=eyeCascade.detectMultiScale(frameGray,1.3,5)
        for eye in eyes:
            x1,y1,w1,h1=eye
            print(eyes)
            cv2.rectangle(frameGray,(x1,y1),(x1+w1,y1+h1),(0,255,0),3)

    
    
    cv2.imshow('my WEBcam',frameGray)
    cv2.moveWindow('my WEBcam' , 0 ,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
cam.release()    