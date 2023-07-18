import cv2

cam = cv2.VideoCapture(0)

while True:
    ignore, frame = cam.read()
    cv2.imshow('My-webcam', frame)
    cv2.moveWindow('My-webcam',100,100)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()
