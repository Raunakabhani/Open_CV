import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX

width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))


roniFace=FR.load_image_file('C:/Users/Admin/Documents/Python/demoImages/known/RAUNAK.png')
faceLoc=FR.face_locations(roniFace)[0]
ronifaceencode=FR.face_encodings(roniFace)[0]

masuFace=FR.load_image_file('C:/Users/Admin/Documents/Python/demoImages/known/masu.jpg')
faceLoc=FR.face_locations(masuFace)[0]
masufaceencode=FR.face_encodings(masuFace)[0]


knownEncodings=[ronifaceencode,masufaceencode]
names=['Roni','masu']

while True:
    ignore, unknownface = cam.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    unknownfaceBGR=cv2.cvtColor(unknownface,cv2.COLOR_RGB2BGR)
    facelocations=FR.face_locations(unknownface)
    unknownencodings=FR.face_encodings(unknownface,facelocations)

    for facelocation,unknownencoding in zip(facelocations,unknownencodings):
        top,right,bottom,left=facelocation 
        cv2.rectangle(unknownface,(left,top),(right,bottom),(255,0,0),3)
        name='unknown person'
        matches=FR.compare_faces(knownEncodings,unknownencoding)
        #print(matches)
        if True in matches:
            matchIndex=matches.index(True)
            print(matchIndex)
            print(name[matchIndex])
            name=names[matchIndex]
        cv2.putText(unknownface,name,(left,top),font,0.9,(0,255,0),5)



    cv2.imshow('my WEBcam',unknownface)
    cv2.moveWindow('my WEBcam' , 0 ,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
cam.release()    
cv2.destroyAllWindows