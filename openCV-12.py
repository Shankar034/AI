import cv2

height= 680
width =460

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
rows =10
columns=10
while True:
    ignore, frame = cam.read()

    colorB=frame[100:200,100:200]
    colorB1=cv2.cvtColor(colorB,cv2.COLOR_BGR2GRAY)
    grayF= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grayF[100:200,100:200]=colorB1
    cv2.imshow("Frame1",grayF)
    cv2.moveWindow("Frame1",10,10)
    cv2.imshow("Frame2",colorB)
    cv2.moveWindow("Frame2",700,100)
     
            
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release