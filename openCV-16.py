import cv2

print(cv2.__version__)

def callBack1(val):
    global xPos
    print("xPos : ",val)
    xPos=val


width = 680
height=460
xPos = int(width*3/4)
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow("Web1")
cv2.resizeWindow("Web1",200,400)
cv2.moveWindow("Web1",width,0)
cv2.createTrackbar("xPos", "Web1",xPos,width,callBack1)


while True:
    ignore, frame = cam.read()
    cv2.imshow("Webcam",frame)
    cv2.moveWindow("Webcam",xPos,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()