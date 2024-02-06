from fileinput import filename
import face_recognition as fr
import cv2 as cv
from tkinter import Tk
from tkinter.filedialog import askopenfilename  # open filechooser
import os

# choose photo
Tk().withdraw()
load_image = askopenfilename()
target_image = fr.load_image_file(load_image)
target_encoding = fr.face_encodings(target_image)


# Searches for occurrence of this face
def encode_faces(folder):
    list_Faces_encoding = []

    for filename in os.listdir(folder):
        known_image = fr.load_image_file(f'{folder}{filename}')
        know_encoding = fr.face_encodings(known_image)[0]

        list_Faces_encoding.append((know_encoding, os.path.splitext(filename)[0]))
    return list_Faces_encoding


# looks for the target faces
def find_target_face():
    face_locations = fr.face_locations(target_image)
    face_encodings = fr.face_encodings(target_image, face_locations)

    known_faces = encode_faces('Faces/')
    found_matches = []
    found_unknown = []

    for i, face_encoding in enumerate(face_encodings):
        is_match = False
        for known_face in known_faces:
            if fr.compare_faces([known_face[0]], face_encoding, tolerance=0.55)[0]:
                found_matches.append((face_locations[i], known_face[1]))
                is_match = True
                break
        if not is_match:
            found_unknown.append(face_locations[i])

    for location, label in found_matches:
        create_frame(location, label)
    for location in found_unknown:
        create_frame(location, 'Unknown')

def create_frame(location, label):
    top, right, bottom, left = location
    if label != "Unknown":
        cv.rectangle(target_image, (left, top), (right, bottom), (255,0, 0), 2)
        cv.rectangle(target_image, (left, bottom + 25), (right+120, bottom), (255,0, 0), cv.FILLED)
        cv.putText(target_image, label, (left , bottom +20), cv.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1)
    else:
        cv.rectangle(target_image, (left, top), (right, bottom), (0,255, 0), 2)
        cv.rectangle(target_image, (left, bottom + 25), (right, bottom), (0,255, 0), cv.FILLED)
        cv.putText(target_image, label, (left , bottom +20), cv.FONT_HERSHEY_DUPLEX, 0.9, (255, 255, 255), 1)



def render_image():
    rgb_img = cv.cvtColor(target_image, cv.COLOR_BGR2RGB)
    cv.imshow('Image Face Recognition', rgb_img)
    cv.waitKey(0)


find_target_face()
render_image()
