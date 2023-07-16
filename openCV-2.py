import cv2
print(cv2.__version__)
cam = cv2.VideoCapture(0)
while True:
    ignore, frame= cam.read()
    cv2.imshow('my-webcam',frame)
    cv2.moveWindow("my-webcam",0,0)
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('my-greycam',grayFrame)
    cv2.moveWindow("my-greycam",600,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()

