import cv2
print(cv2.__version__)
cvt=0

def mouseClick(event, xPos, yPos, flags, params):
    global evt 
    global pvt
    if event == cv2.EVENT_LBUTTONDOWN:
        print("The event was : ", event)
        print("The point is ",xPos,yPos)
        evt = event
        pvt=(xPos,yPos)
    if event == cv2.EVENT_LBUTTONUP:
        print("The event was : ", event)
        print("The point is ",xPos,yPos)
        evt = event


height = 480
width= 640

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cv2.
cv2.setMouseCallback("Webcam", mouseClick)

while True:
    ignore, frame = cam.read()
    if evt==1 or evt ==4:
        cv2.circle(frame,pvt,50,(200,0,200),4)
    cv2.imshow("Webcam",frame)
    cv2.moveWindow("Webcam",10,10)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()