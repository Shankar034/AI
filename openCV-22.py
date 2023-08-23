import cv2
import numpy as np

print(cv2.__version__)

xpos=0
ypos=0
HueLow=19
HueHigh=74

HueLow1=26
HueHigh1=47

SaturationLow=42
SaturationHigh=146

ValueLow=137
ValueHigh=255

def trackbar1(val):
    global HueLow
    print(val)
    HueLow = val
def trackbar2(val):
    global HueHigh
    print(val)
    HueHigh = val
def trackbar3(val):
    global SaturationLow
    print(val)
    SaturationLow = val
def trackbar4(val):
    global SaturationHigh
    print(val)
    SaturationHigh = val
def trackbar5(val):
    global ValueLow
    print(val)
    ValueLow = val
def trackbar6(val):
    global ValueHigh
    print(val)
    ValueHigh = val
def trackbar7(val):
    global HueLow1
    print(val)
    HueLow1 = val
def trackbar8(val):
    global HueHigh1
    print(val)
    HueHigh1 = val

Height = 460
width = 680
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,Height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow("FPS")
cv2.moveWindow("FPS", width,0)

cv2.createTrackbar("Hue Low", "FPS",19,179,trackbar1)
cv2.createTrackbar("Hue High", "FPS",74,179,trackbar2)
cv2.createTrackbar("Saturation Low", "FPS",42,255,trackbar3)
cv2.createTrackbar("Saturation High", "FPS",146,255,trackbar4)
cv2.createTrackbar("Value Low", "FPS",137,255,trackbar5)
cv2.createTrackbar("Value High", "FPS",255,255,trackbar6)
cv2.createTrackbar("Hue Low1", "FPS",26,179,trackbar7)
cv2.createTrackbar("Hue High1", "FPS",47,179,trackbar8)

while True:
    ignore, frame = cam.read()
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBond = np.array([HueLow,SaturationLow, ValueLow])
    upperBond = np.array([HueHigh, SaturationHigh, ValueHigh])

    lowerBond1 = np.array([HueLow1,SaturationLow, ValueLow])
    upperBond1 = np.array([HueHigh1, SaturationHigh, ValueHigh])
    myMask = cv2.inRange(frameHSV,lowerBond,upperBond)
    myMask2 = cv2.inRange(frameHSV,lowerBond1,upperBond1)
    
    myMask= myMask | myMask2

    # myMask = cv2.add(myMask,myMask2)
    # myMask = np.logical_or(myMask,myMask2)

    # myMask= cv2.bitwise_not(myMask)
    counters, junk = cv2.findContours(myMask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame,counters, -1,(255,0,0),3)

    for counter in counters:
        area = cv2.contourArea(counter)
        if area >= 200:
            # cv2.drawContours(frame,[counter], 0,(255,0,0),3)
            x,y,w,h=cv2.boundingRect(counter)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,120,255),3)
            xpos= x
            ypos= y
            xpos = int(xpos/width*1920)
            ypos = int(ypos/Height*1080)


    myMasksmall= cv2.resize(myMask,(int(width/2),int(Height/2)))
    mySelection= cv2.bitwise_and(frame,frame,mask=myMask)
    mySelection= cv2.resize(mySelection,(int(width/2),int(Height/2)))


    # frameS1= cv2.bitwise_and(frame,frame,mask=myMask)


    cv2.imshow("my selection", mySelection)
    cv2.moveWindow("my selection", int(width/2), Height)

    cv2.imshow("my mask", myMasksmall)
    cv2.moveWindow("my mask", 0, Height)

    cv2.imshow("my Webcam", frame)
    cv2.moveWindow("my Webcam",xpos, ypos)


    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()