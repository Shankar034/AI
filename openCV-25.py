import cv2
import face_recognition as FR

font=cv2.FONT_HERSHEY_SIMPLEX
donFace = FR.load_image_file('C:/Users/Dell/Documents/Python/demoimages/known/Donald Trump.jpg')
faceloc = FR.face_locations(donFace)[0]
donEncoding= FR.face_encodings(donFace)[0]

shankarFace = FR.load_image_file('C:/Users/Dell/Documents/Python/demoimages/known/Shankar Bhandari.jpg')
faceloc = FR.face_locations(donFace)[0]
shankarEncoding= FR.face_encodings(donFace)[0]

print(faceloc)
top, right, buttom, left = faceloc
cv2.rectangle(donFace,(left,top),(right,buttom),(0,255,255),3)
donFaceBGR=cv2.cvtColor(donFace, cv2.COLOR_RGB2BGR)
cv2.imshow("My Bar", donFaceBGR)
cv2.waitKey(5000)