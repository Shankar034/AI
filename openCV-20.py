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
cv2.createTrackbar("Saturation Low", "FPS",10,255,trackbar3)
cv2.createTrackbar("Saturation High", "FPS",20,255,trackbar4)
cv2.createTrackbar("Value Low", "FPS",10,255,trackbar5)
cv2.createTrackbar("Value High", "FPS",20,255,trackbar6)
# cv2.createTrackbar("Hue Low", "FPS",10,179,trackbar)

while True:
    ignore, frame = cam.read()
    cv2.imshow("Frame", frame)
    cv2.moveWindow("Frame", 10, 10)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()