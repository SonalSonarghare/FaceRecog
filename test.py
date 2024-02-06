import os
import pickle
import cvzone
import numpy as np
import cv2
import face_recognition

cap = cv2.VideoCapture(0)
cap.set(3, 520)  # Set width
cap.set(4, 385)  # Set height

imgBackground = cv2.imread('Real-images/Realtimebkg.png')

# importing the mode images into list
folderModePath = 'Real-images/mode'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# Load the encoding file
print("Loading Encode File...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithCNames = pickle.load(file)
file.close()
encodeListKnown, CriminalName = encodeListKnownWithCNames
print("Encode File Loaded...")

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)  # Scale
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)  # RGB FROM BGR

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    resized_img = cv2.resize(img, (520, 385))
    imgBackground[95:95 + 385, 18:18 + 520] = resized_img  # Move image to the right by 18 pixels
    imgBackground[40:40 + 397, 580:580 + 398] = cv2.resize(imgModeList[0], (398, 397))

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        # Lower the distance better the match
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print("matches", matches)
        print("faceDis", faceDis)

        matchIndex = np.argmin(faceDis)
        print("Match Index", matchIndex)

        if matches[matchIndex]:
            print("CRIMINAL DETECTED!!")
            print(CriminalName[matchIndex])
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = x1 - 40, 78 + y1, x2 - x1, y2 - y1

            # Load and display image of the criminal on the left side of the video feed
            criminal_image = cv2.imread(f"Test-Images/{CriminalName[matchIndex]}.jpg")
            if criminal_image is not None:
                imgBackground[40:40 + 397, 580:580 + 398] = cv2.resize(criminal_image, (398, 397))
                # Add text "CRIMINAL FOUND" below the photo
                cv2.putText(imgBackground, "CRIMINAL FOUND", (640, 465), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.rectangle(imgBackground, bbox, (0, 0, 255), 2)
            cv2.rectangle(imgBackground, (bbox[0], bbox[1] + bbox[3] + 1), (bbox[0] + bbox[2], bbox[1] + bbox[3] + 40),
                          (0, 0, 255), cv2.FILLED)

            cv2.putText(imgBackground, CriminalName[matchIndex],
                        (bbox[0] + 10, bbox[1] + bbox[3] + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("RealTime Face Recog", imgBackground)
    cv2.waitKey(1)