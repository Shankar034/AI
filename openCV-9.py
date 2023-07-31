import cv2

print(cv2.__version__)

width = 640
height=360

cCenter=(175,175)
radius= 50
circleColor=(100,0,100)
cWidth=2
webText = 'I am God.'
fHeight = 1
FThickness =2

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame= cam.read()
    frame[100:250,100:250]=(10,100,200)
    cv2.rectangle(frame,(100,100),(250,250),(120,100,10),8)
    cv2.circle(frame,cCenter,radius,circleColor,cWidth)
    cv2.putText(frame,webText,(200,90),cv2.FONT_HERSHEY_COMPLEX,fHeight,(10,200,20),FThickness)
    cv2.imshow("Webcam",frame)
    cv2.moveWindow("Webcam",0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()