import cv2

cam = cv2.VideoCapture(0)

while True:
    ignore, frame = cam.read()
    cv2.imshow('My-webcam', frame)
    cv2.moveWindow('My-webcam',100,100)
    grayCam = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray-cam',grayCam)
    cv2.moveWindow('gray-cam',300,300)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()
