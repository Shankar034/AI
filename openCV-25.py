import cv2
import face_recognition as FR
name='Unknown Face'
font=cv2.FONT_HERSHEY_SIMPLEX
donFace = FR.load_image_file('C:/Users/Dell/Documents/Python/demoimages/known/Donald Trump.jpg')
faceloc = FR.face_locations(donFace)[0]
donEncoding= FR.face_encodings(donFace)[0]

nancyFace = FR.load_image_file('C:/Users/Dell/Documents/Python/demoimages/known/Nancy Pelosi.jpg')
faceloc = FR.face_locations(nancyFace)[0]
nancyEncoding= FR.face_encodings(nancyFace)[0]

knownEncoding = [donEncoding,nancyEncoding]
names= ["Donald Trump","Nancy Pelosi"]

unknownFace = FR.load_image_file('C:/Users/Dell/Documents/Python/demoimages/unknown/u5.jpg')
unknownFaceBGR = cv2.cvtColor(unknownFace, cv2.COLOR_RGB2BGR)
faceLocations = FR.face_locations(unknownFace)
unknownEncodings = FR.face_encodings(unknownFace,faceLocations)

for faceLocation, unknownEncoding in zip(faceLocations,unknownEncodings):
    top, right, buttom, left = faceLocation
    print(faceLocation)
    cv2.rectangle(unknownFaceBGR, (left,top),(right,buttom),(255,255,0),3)
    matches = FR.compare_faces(knownEncoding,unknownEncoding)
    print(matches)
    if True in matches:
        matchIndex = matches.index(True)
        print(matchIndex)
        print(names[matchIndex])
        name = names[matchIndex]
    cv2.putText(unknownFaceBGR,name,(left, top),font, 1,(0,0,230),3)
cv2.imshow("Image",unknownFaceBGR)



cv2.waitKey(10000)


# print(faceloc)
# top, right, buttom, left = faceloc
# cv2.rectangle(donFace,(left,top),(right,buttom),(0,255,255),3)
# donFaceBGR=cv2.cvtColor(donFace, cv2.COLOR_RGB2BGR)
# cv2.imshow("My Bar", donFaceBGR)