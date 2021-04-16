import face_recognition
from PIL import UnidentifiedImageError
import json

albums = {}


def faceExists(imagesList):
    
    knownEncodings = []

    index = 0
    for i in range(len(imagesList)):
        
        

        try:
            image = face_recognition.load_image_file(imagesList[i])

            try:
                imageEncode = face_recognition.face_encodings(image)[0]
                result = face_recognition.compare_faces(knownEncodings,imageEncode) # Pass this to function checkResult

                if (checkResult(result) != -1): # Face already there
                    knownEncodings.append(imageEncode)
                    #data["Untitled"+str(checkResult(result))].append(imagesList[i])
                    albums[name].append(imagesList[i])

                else: # New face
                    name = "Untitled"+str(index)
                    knownEncodings.append(imageEncode)
                    albums[name] = [imagesList[i]]
                    index += 1 

            except IndexError:
                print("no faces in the image")

        except UnidentifiedImageError:
            print("non image added")

    # Add All Albums Album

def checkResult(resultArray):

    if not resultArray:
        return -1 # List is empty
    
    for i in range(len(resultArray)):
        if resultArray[i]==True:
            return i

    return -1