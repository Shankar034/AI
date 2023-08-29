import os
import cv2
import face_recognition as FR
import pickle

encoding=[]
names= []

imageDir = 'C:\\Users\Dell\Documents\Python\demoimages\known'

for root, dirs,files in os.walk(imageDir):
    print(dirs)
    print(files)
    for file in files:
        print(file)
        fullFilePath = os.path.join(root, file)
        print(fullFilePath)
        image = FR.load_image_file(fullFilePath)
        fileEncoding = FR.face_encodings(image)[0]
        name = os.path.splitext(file)[0]
        encoding.append(encoding)
        names.append(name)
with open('train.pkl','wb') as f:
    pickle.dump(names,f)
    pickle.dump(encoding, f)
