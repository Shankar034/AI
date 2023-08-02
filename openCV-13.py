import cv2
print(cv2.__version__)
evt =0
def mouseClick(event, xPos, yPos, flags, params):
    global evt
    global pvt
    if event == cv2.EVENT_LBUTTONDOWN:
        print(" The mouse Event was :",event)
        print("The position is ", xPos,yPos)
        evt = event
        pvt = (xPos,yPos)
    if event == cv2.EVENT_LBUTTONUP:
        print(" The mouse Event was :",event)
        print("The position is ",xPos,yPos)
        evt = event
       



height= 460
width = 680

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow("WebCam")
cv2.setMouseCallback("WebCam",mouseClick)

while True:
    ignore, frame = cam.read()
    if evt==1:
        cv2.circle(frame,pvt,30,(120,180,1),2)
    cv2.imshow("WebCam",frame)
    cv2.moveWindow("WebCam",10,10)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()