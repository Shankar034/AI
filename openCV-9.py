import cv2

print(cv2.__version__)

width = 460
height=360

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame= cam.read()
    frame[130:250,140:180]=(10,100,200)
    cv2.imshow("Webcam",frame)
    cv2.moveWindow("Webcam",100,100)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()