import cv2
import face_recognition
import pickle
import os

# Importing  Criminals images
folderPath = 'Faces'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
CriminalName = [] #Name of criminal
for path in pathList:
  imgList.append(cv2.imread(os.path.join(folderPath,path)))
  CriminalName.append(os.path.splitext(path)[0])
  #print(path)
  #print(os.path.splitext(path)[0])
print(CriminalName)

def findEncodings(imagesList):
    encodeList= []
    for img in imagesList :
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # RBG FROM BGR
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithCNames = [encodeListKnown, CriminalName]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithCNames,file)
file.close()