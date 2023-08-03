import cv2

print(cv2.__version__)

def myCallBack1(val):
    global xPos
    print("xPos is : ",val)
    xPos=val


def myCallBack2(val):
    global yPos
    print('yPos is: ',val)
    yPos=val

def myCallBack3(val):
    global radius
    print('Radius is : ',val)
    radius=val


height=580
width=740
xPos=int(width/2)
yPos=int(height/2)
radius = 20

cam= cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow("Webcam")
cv2.resizeWindow("Webcam",460,340)
cv2.moveWindow("Webcam",width,0)
cv2.createTrackbar("xPos ","Webcam",xPos,760,myCallBack1)
cv2.createTrackbar("yPos ","Webcam",yPos,580,myCallBack2)
cv2.createTrackbar("Radius ","Webcam",radius,290,myCallBack3)



while True:
    ignore, frame= cam.read()
    cv2.circle(frame,(xPos,yPos),radius,(122,0,122),3)
    cv2.imshow("My Webcam",frame)
    cv2.moveWindow("My Webcam",10,10)
    if cv2.waitKey(1) & 0xff== ord('q'):
        break
cam.release()