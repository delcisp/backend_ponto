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

    try:
        for userId in os.listdir(folderPath):
            userPath = os.path.join(folderPath, userId)
            userEncodings = []
            userImagesWithoutFaces = []
            if os.path.isdir(userPath):
                for imgName in os.listdir(userPath):
                    imgPath = os.path.join(userPath, imgName)
                    try:
                        img = cv2.imread(imgPath)
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        encodings = face_recognition.face_encodings(img)
                        if encodings:
                            userEncodings.extend(encodings)
                        else:
                            userImagesWithoutFaces.append(imgName)
                    except Exception as e:
                        print(f"Erro ao carregar imagem {imgPath}: {e}")
            encodeList[userId] = userEncodings
            if userImagesWithoutFaces:
                imagesWithoutFaces[userId] = userImagesWithoutFaces
    except Exception as e:
        print(f"Erro ao encontrar encodings: {e}")
        return None, None

    return encodeList, imagesWithoutFaces

try:
    encodeListKnown, imagesWithoutFaces = findEncodings(folderPath)
    for userId, images in imagesWithoutFaces.items():
        if images:
            print(f"Usuário {userId} - Não foi possível encontrar rostos nas seguintes imagens: {images}")
    print("Encoding Complete")
    with open("EncodeFile.p", 'wb') as file:
        pickle.dump(encodeListKnown, file)
    file.close()
    print("File Saved")
except Exception as e:
    print(f"Erro ao salvar arquivo: {e}")

