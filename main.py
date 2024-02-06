

# 10.02.2023
# File > Settings > Project> Project Interpreter
import cv2
# create object(cap).(0) for 1 camera
# open webcam

cap = cv2.VideoCapture(0)

while True:
    ret, frames = cap.read()
    cv2.imshow('webcam', frames)
    k = cv2.waitKey(10)
    if k == 27:   # 27 ASCII escape
        break
# shutdown camera
cap.release()
cv2.destroyAllWindows()
