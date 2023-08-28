import os
import cv2
import face_recognition as FR


imgDir = 'C:\\Users\Dell\Documents\Python\demoimages\known'
root= ''
file=''
for dirs,root, files in os.walk(imgDir):
    print('Directry in root ',dirs)
    print('My Working folder', root)
    print("Files in the root",files)
    for file in files:
        print('Your guy is ',file)
        if isinstance(root, str) and isinstance(file, str):
            fullFilePath = os.path.join(root,file)
            print(fullFilePath)
            name = os.path.splitext(file)[0]
            print(name)
            myPicture = FR.load_image_file(fullFilePath)
            myPicture= cv2.cvtColor(myPicture, cv2.COLOR_RGB2BGR)
            cv2.imshow(name,myPicture)
            cv2.moveWindowd(name,10,10)
            cv2.waitKey(2500)
            cv2.destroyAllWindows()