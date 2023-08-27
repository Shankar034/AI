import cv2
import face_recognition as FR
name='Unknown Face'

height = 460
width = 680
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

font=cv2.FONT_HERSHEY_SIMPLEX

shanFace = FR.load_image_file('C:/Users/Dell/Documents/Python/demoimages/known/Shankar Bhandari.jpg')
faceloc = FR.face_locations(shanFace)[0]
shanEncoding= FR.face_encodings(shanFace)[0]

nancyFace = FR.load_image_file('C:/Users/Dell/Documents/Python/demoimages/known/Fiyana Saud.jpg')
faceloc = FR.face_locations(nancyFace)[0]
nancyEncoding= FR.face_encodings(nancyFace)[0]

knownEncoding = [shanEncoding,nancyEncoding]
names= ["Shankar Bhandari","Fiyana Saud"]


while True:
    ignore, unknownFace = cam.read()
    unknownFaceBGR = cv2.cvtColor(unknownFace, cv2.COLOR_BGR2RGB)
    faceLocations = FR.face_locations(unknownFace)
    unknownEncodings = FR.face_encodings(unknownFace,faceLocations)

    for faceLocation, unknownEncoding in zip(faceLocations,unknownEncodings):
        top, right, buttom, left = faceLocation
        print(faceLocation)
        cv2.rectangle(unknownFace, (left,top),(right,buttom),(255,255,0),3)
        matches = FR.compare_faces(knownEncoding,unknownEncoding)
        print(matches)
        if True in matches:
            matchIndex = matches.index(True)
            print(matchIndex)
            print(names[matchIndex])
            name = names[matchIndex]
        cv2.putText(unknownFace,name,(left, top),font, 1,(0,0,230),3)
    cv2.imshow("Image",unknownFace)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()

    

