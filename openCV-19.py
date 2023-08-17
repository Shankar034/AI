import cv2

pos =0
def onTrack1(event):
    global pos
    pos = event


height = 460
width = 580
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))


cv2.namedWindow("NewWin")
cv2.moveWindow("NewWin",width,0)
cv2.createTrackbar("low high", "NewWin",0,460,onTrack1)
cv2.createTrackbar("low high", "NewWin",0,460,onTrack1)
cv2.createTrackbar("low high", "NewWin",0,460,onTrack1)
cv2.createTrackbar("low high", "NewWin",0,460,onTrack1)
cv2.createTrackbar("low high", "NewWin",0,460,onTrack1)
cv2.createTrackbar("low high", "NewWin",0,460,onTrack1)


while True:
    ignore, frame= cam.read()
    cv2.imshow("WebCam",frame)
    cv2.moveWindow("WebCam",0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()