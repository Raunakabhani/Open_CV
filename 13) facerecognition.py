import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX

donFace=FR.load_image_file('C:/Users/Admin/Documents/Python/demoImages/known/Donald Trump.jpg')
faceLoc=FR.face_locations(donFace)[0]
donfaceencode=FR.face_encodings(donFace)[0]

nancyFace=FR.load_image_file('C:/Users/Admin/Documents/Python/demoImages/known/Nancy Pelosi.jpg')
faceLoc=FR.face_locations(nancyFace)[0]
nancyfaceencode=FR.face_encodings(nancyFace)[0]

knownEncodings=[donfaceencode,nancyfaceencode]
names=['Donal Trump','Nancy Pelosi']

unknownface=FR.load_image_file('C:/Users/Admin/Documents/Python/demoImages/unknown/u1.jpg')
unknownfaceBGR=cv2.cvtColor(unknownface,cv2.COLOR_RGB2BGR)
facelocations=FR.face_locations(unknownface)
unknownencodings=FR.face_encodings(unknownface,facelocations)

for facelocation,unknownencoding in zip(facelocations,unknownencodings):
    top,right,bottom,left=facelocation 
    cv2.rectangle(unknownfaceBGR,(left,top),(right,bottom),(255,0,0),3)
    name='unknown person'
    matches=FR.compare_faces(knownEncodings,unknownencoding)
    #print(matches)
    if True in matches:
        matchIndex=matches.index(True)
        print(matchIndex)
        print(name[matchIndex])
        name=names[matchIndex]
    cv2.putText(unknownfaceBGR,name,(left,top),font,.5,(255,0,0),2)

cv2.imshow('my faces',unknownfaceBGR)




'''print(faceLoc)
top,right,bottom,left=faceLoc
cv2.rectangle(donFace,(left,top),(right,bottom),(255,0,0),3)
donFaceBGR=cv2.cvtColor(donFace,cv2.COLOR_RGB2BGR)
cv2.imshow('my window',donFaceBGR)'''
cv2.waitKey(5000) 