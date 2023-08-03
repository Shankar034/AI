import cv2

print(cv2.__version__)

evt=0

def mouseClick(event, xPos, yPos, flags, params):
    global evt 
    global pnt1
    global pnt2
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        evt = event
        pnt1 = (xPos,yPos)

    if event ==cv2.EVENT_LBUTTONUP:
        print(event)
        evt= event
        pnt2 = (xPos, yPos)
    
    if event == cv2.EVENT_RBUTTONUP:
        print(event)
        evt= event

height=480
width=640


cam= cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam",mouseClick)

while True:
    ignore, frame= cam.read()
    if evt == 4:
        cv2.rectangle(frame,pnt1,pnt2,(100,155,200),2)
        ROI = frame[pnt1[1]:pnt2[1], pnt1[0]:pnt2[0]]
        cv2.imshow("ROI", ROI)
        cv2.moveWindow("ROI", int(width*1.1),0)
    if evt ==5:
        cv2.destroyWindow("ROI")
        evt=0
    cv2.imshow("Webcam",frame)
    cv2.moveWindow("Webcam",10,10)
    if cv2.waitKey(1) & 0xff== ord('q'):
        break
cam.release()