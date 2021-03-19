import cv2
import face_recognition
import os
from PIL import UnidentifiedImageError
import json

data = {}

def loadImagesFromFodler(folder):
    images = os.listdir(folder)
    return (images)

def faceExists(folder):
    
    knownEncodings = []

    imagesList = loadImagesFromFodler(folder)

    for i in range(len(imagesList)):
        
        name = "Untitled"+str(i)
        realName = imagesList[i].split(".")
        try:
            image = face_recognition.load_image_file(folder+"/"+imagesList[i])
            imageEncode = face_recognition.face_encodings(image)[0]
            result = face_recognition.compare_faces(knownEncodings,imageEncode) # Pass this to function checkResult

            if (checkResult(result) != -1): # Face already there
                knownEncodings.append(imageEncode)
                data["Untitled"+str(checkResult(result)+1)].append(imagesList[i])

            else: # New face
                knownEncodings.append(imageEncode)
                data[realName[0]] = [imagesList[i]]
            
        except UnidentifiedImageError:
            print()

    with open("sample.json","w") as outfile:
        json.dump(data, outfile)
    
    print(data)


def checkResult(resultArray):

    if not resultArray:
        return -1 # List is empty
    
    for i in range(len(resultArray)):
        if resultArray[i]==True:
            return i

    return -1
    


faceExists("testDB")
