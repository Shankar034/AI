import cv2
import numpy as np

def onTrack1(pos):
    global huelow
    huelow = pos
def onTrack2(pos):
    global hueHigh
    hueHigh = pos
def onTrack3(event):
    global SatLow
    SatLow = event
def onTrack4(event):
    global SatHigh
    SatHigh = event
def onTrack5(event):
    global ValueLow
    ValueLow = event
def onTrack6(event):
    global ValueHigh
    ValueHigh = event

height = 460
width = 580
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))


cv2.namedWindow("NewWin")
cv2.moveWindow("NewWin",width,0)
cv2.createTrackbar("hue low", "NewWin",10,179,onTrack1)
cv2.createTrackbar("hue high", "NewWin",20,179,onTrack2)
cv2.createTrackbar("sat low", "NewWin",20,255,onTrack3)
cv2.createTrackbar("sat high", "NewWin",110,255,onTrack4)
cv2.createTrackbar("val low", "NewWin",20,255,onTrack5)
cv2.createTrackbar("low high", "NewWin",110,255,onTrack6)


while True:
    ignore, frame= cam.read()
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerbound = np.array([huelow, SatLow, ValueLow])
    upperbound = np.array([hueHigh, SatHigh, ValueHigh])
    myMask = cv2.inRange(frameHSV, lowerbound, upperbound)
    myMask = cv2.bitwise_not(myMask)
    myObj= cv2.bitwise_and(frame, frame, mask=myMask)
    myMaskSmall = cv2.resize(myMask,(int(width/2), int(height/2)))
    myObjSmall = cv2.resize(myObj,(int(width/2), int(height)))
    cv2.imshow("HSV Obj",myObjSmall)
    cv2.moveWindow("HSV Obj",0,height)
    cv2.imshow("HSV",myMaskSmall)
    cv2.moveWindow("HSV",0,height)
    cv2.imshow("WebCam",frame)
    cv2.moveWindow("WebCam",0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()