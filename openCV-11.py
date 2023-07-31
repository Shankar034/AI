import cv2

print(cv2.__version__)

width = 640
height=360



cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame= cam.read()
    frameRoi=frame[170:310,280:440]
    grayRoi =cv2.cvtColor(frameRoi,cv2.COLOR_BGR2GRAY);
    cv2.imshow("ROI frame",frameRoi)
    cv2.moveWindow("ROI frame",650,0)
    cv2.imshow("ROI gray",grayRoi)
    cv2.moveWindow("ROI gray",650,200)
    cv2.imshow("Webcam",frame)
    cv2.moveWindow("Webcam",0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
