import cv2

# Function takes imagePath as paramter and returns an image with detected faces
def detectFaces(imagePath):
    image = cv2.imread("<image path>") # Read image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert image to gray

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=3,
            minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    status = cv2.imwrite('faces_detected.jpg', image)
