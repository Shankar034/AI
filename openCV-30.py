import cv2
import mediapipe as mp
width = 460
height=340
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(* 'MJPG'))

while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame,(width,height))
    cv2.imshow('My-webcam', frame)
    cv2.moveWindow('My-webcam',100,100)
    
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()
