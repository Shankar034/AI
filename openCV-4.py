import cv2

width =420
height=360

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(* 'MJPG'))

while True:
    ignore, frame = cam.read()
    cv2.imshow('Web-cam', frame)
    cv2.moveWindow('Web-cam',10,20)
    myFrame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('my-cam', myFrame)
    cv2.moveWindow('my-cam',100,200)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release();
