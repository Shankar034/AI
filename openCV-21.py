import cv2
import numpy as np

print(cv2.__version__)

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
cv2.createTrackbar("Hue Low", "FPS",10,179,trackbar1)
cv2.createTrackbar("Hue High", "FPS",20,179,trackbar2)
cv2.createTrackbar("Hue Low1", "FPS",10,179,trackbar7)
cv2.createTrackbar("Hue High1", "FPS",20,179,trackbar8)
cv2.createTrackbar("Saturation Low", "FPS",10,255,trackbar3)
cv2.createTrackbar("Saturation High", "FPS",250,255,trackbar4)
cv2.createTrackbar("Value Low", "FPS",10,255,trackbar5)
cv2.createTrackbar("Value High", "FPS",250,255,trackbar6)

while True:
    ignore, frame = cam.read()
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBond = np.array([HueLow,SaturationLow, ValueLow])
    upperBond = np.array([HueHigh, SaturationHigh, ValueHigh])

    lowerBond1 = np.array([HueLow1,SaturationLow, ValueLow])
    upperBond1 = np.array([HueHigh1, SaturationHigh, ValueHigh])
    maskH = cv2.inRange(frameHSV,lowerBond,upperBond)
    maskS = cv2.inRange(frameHSV,lowerBond1,upperBond1)
    
    maskS= maskS | maskH

    # maskS = cv2.add(maskH,maskS)
    # maskS = np.logical_or(maskH,maskS)


    frameall= cv2.bitwise_and(frame,frame,mask=maskS)
    frameS1= cv2.bitwise_and(frame,frame,mask=maskS)

    frameall= cv2.resize(maskS,(int(width/2),int(Height/2)))
    frameS= cv2.resize(frameS1,(int(width/2),int(Height/2)))

    cv2.imshow("Frame", frame)
    cv2.moveWindow("Frame", 10, 10)
    cv2.imshow("FrameH", frameall)
    cv2.moveWindow("FrameH",10, Height)
    cv2.imshow("FrameS", frameS)
    cv2.moveWindow("FrameS", int(width/2), Height)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()