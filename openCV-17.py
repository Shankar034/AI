import cv2
import numpy as np
print(cv2.__version__)

xVal =0
yVal=0
evt= 0
def mouseClick(event, xPos, yPos, flags, params):
    global xVal
    global yVal
    global evt
    if event== cv2.EVENT_LBUTTONDOWN:
        print(event)
        xVal = xPos
        yVal = yPos
        evt = event
    
    if event == cv2.EVENT_RBUTTONUP:
        evt = event
        print(event)

height =480
width =680

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow("WebCam")
cv2.setMouseCallback("WebCam",mouseClick)


while True:
    ignore, frame = cam.read()
    if evt == 1:
        x= np.zeros([220,220,3], dtype = np.uint8)
        clr= frame[yVal][xVal]
        print(clr)
        x[:,:]=clr
        cv2.putText(x,str(clr),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(68,54,58),1)
        cv2.imshow("The Window",x)
        cv2.moveWindow("The Window",width,0)
        evt =0
    cv2.imshow("WebCam",frame)
    cv2.moveWindow("WebCam",0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cam.release()