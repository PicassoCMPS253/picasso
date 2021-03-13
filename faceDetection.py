import cv2
import face_recognition
import os
from PIL import UnidentifiedImageError



def loadImagesFromFodler(folder):
    images = os.listdir(folder)
    return (images)

def faceExists(folder):
    
    knownImages = []

    imagesList = loadImagesFromFodler(folder)

    for i in range(len(imagesList)):


        try:
            image = face_recognition.load_image_file(folder+"/"+imagesList[i])
            imageEncode = face_recognition.face_encodings(image)[0]
            result = face_recognition.compare_faces(knownImages,imageEncode)
            knownImages.append(imageEncode)
            print(result)
        except UnidentifiedImageError:
            print("NON IMAGE OBJECT!")


    '''
    cImage = face_recognition.load_image_file("testDB/c1.jpeg")
    unknownImage = face_recognition.load_image_file("testDB/c2.jpeg")
    
    cinco = face_recognition.face_encodings(cImage)[0]
    unknownImageInco = face_recognition.face_encodings(unknownImage)[0]

    result = face_recognition.compare_faces(knownImages,unknownImageInco)
    print(result)
    '''



faceExists("testDB")
