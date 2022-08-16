import cv2
import mediapipe as mp


#if its static image than true(image stream) , otherwise false(video stream)
#2 for maxx no of hand detected 
#model_complexity 0.5
#min detection confidence
mp_hands=mp.solutions.hands
hands1=mp_hands.Hands(False,2,0.5,0.5)
mpDraw=mp.solutions.drawing_utils


width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))



while True:
    myhandsxy=[]
    ignore, frame = cam.read()   
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands1.process(frameRGB)   #it is some type of class object and not any array 
    if results.multi_hand_landmarks != None: #will come in this loop if and only if the hand is detected 
        for handlandmarks in results.multi_hand_landmarks:
            myhandxy=[]  #to get array of tupples  #ane agar starting ma define kari deso to it wont work properly 
            #handlandmarks is x,y,z coordinated 
            #mpDraw.draw_landmarks(frame,handlandmarks,mp.solutions.hands.HAND_CONNECTIONS)
            
            #below line is for grabbing all 21 x,y points of hands  
            for landmark in handlandmarks.landmark:
                myhandxy.append((int(landmark.x*width),int(landmark.y*height)))
            
            #print(myhandxy) #to print array of tupples of x,y point 
            cv2.circle(frame,myhandxy[8],25,(255,0,255),-1)
            myhandsxy.append(myhandxy) #to get data of 2 hands together 
            print(myhandsxy)
    
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam' , 0 ,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
cam.release()  

#from handlandmarks we want [(x0,y0),(x1,y1)], this has all the info of coordinates of our hands 