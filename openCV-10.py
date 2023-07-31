import cv2
import time

print(cv2.__version__)

height=640
width= 360


cam= cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

tLast = time.time()
fpsFilter=30
time.sleep(0.1)
while True:
    dt= time.time()-tLast
    fps=1/dt
    fpsFilter= fpsFilter*0.9 + fps*0.1
    tLast=time.time()
    ignore,frame = cam.read()
    cv2.rectangle(frame,(100,100),(300,300),(100,10,20),2)
    cv2.circle(frame,(200,200),80,(100,100,10),2)
    cv2.putText(frame,'I am here..',(120,90),cv2.FONT_HERSHEY_COMPLEX,1,(20,100,200),2)
    cv2.rectangle(frame,(120,50),(300,100),(100,0,100),-1)
    cv2.putText(frame,str(int(fpsFilter)) + ' FPS',(150,90),cv2.FONT_HERSHEY_SIMPLEX,1,(100,100,0),3)
    cv2.imshow("Webframe",frame)
    cv2.moveWindow("Webframe",10,10)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release