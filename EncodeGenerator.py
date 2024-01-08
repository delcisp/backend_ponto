import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate("accountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://attendancesystem-cb9a3-default-rtdb.firebaseio.com/",
    'storageBucket': "attendancesystem-cb9a3.appspot.com"
})
folderPath = 'Images'
def findEncodings(folderPath):
    encodeList = {}  # Dicionário para armazenar encodings por ID de usuário
    imagesWithoutFaces = {}  # Dicionário para armazenar IDs e imagens sem rostos detectados
    for userId in os.listdir(folderPath):
        userPath = os.path.join(folderPath, userId)
        userEncodings = []
        userImagesWithoutFaces = []
        if os.path.isdir(userPath):
            for imgName in os.listdir(userPath):
                imgPath = os.path.join(userPath, imgName)
                img = cv2.imread(imgPath)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encodings = face_recognition.face_encodings(img)
                if encodings:
                    userEncodings.extend(encodings)
                else:
                    userImagesWithoutFaces.append(imgName)
        encodeList[userId] = userEncodings
        if userImagesWithoutFaces:
            imagesWithoutFaces[userId] = userImagesWithoutFaces
    return encodeList, imagesWithoutFaces
encodeListKnown, imagesWithoutFaces = findEncodings(folderPath)
for userId, images in imagesWithoutFaces.items():
    if images:
        print(f"Usuário {userId} - Não foi possível encontrar rostos nas seguintes imagens: {images}")
print("Encoding Complete")
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnown, file)
file.close()
print("File Saved")
