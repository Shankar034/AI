import cv2
print(cv2.__version__)

height= 460
width = 640

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

facecascade= cv2.CascadeClassifier('haar\haarcascade_frontalface_default.xml')

while True:
    ignore, frame = cam.read()

    frameGrey= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(frameGrey,1.3,5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y), (x+w,y+h), (255,0,0),3)
    cv2.imshow("Webcam",frame)
    cv2.moveWindow("Webcam",10,10)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()