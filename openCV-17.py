import cv2

print(cv2.__version__)

def mouseClick(event, xPos, yPos, flags, params):
    global xVal
    global yVal
    global evt


height =480
width =680

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow("WebHo")
cv2.setMouseCallback("WebHo",mouseClick)


while True:
    ignore, frame = cam.read()
    cv2.imshow("WebCam",frame)
    cv2.moveWindow("WebCam",0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cam.release()