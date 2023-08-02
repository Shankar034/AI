import cv2
print(cv2.__version__)

height= 460
width = 680

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    cv2.imshow("WebCam",frame)
    cv2.moveWindow("WebCam",10,10)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()