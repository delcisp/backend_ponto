import pickle
import cv2
import face_recognition
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np
import firebase_admin
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime, timedelta
import os
import sys
from firebase_admin import credentials
import threading
from queue import Queue
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
cred = credentials.Certificate(resource_path('accountKey.json'))
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://attendancesystem-cb9a3-default-rtdb.firebaseio.com/",
    'storageBucket': "attendancesystem-cb9a3.appspot.com"
})
bucket = storage.bucket()
detector = FaceMeshDetector(maxFaces=1)
blinkCounter = 0
counter = 0
lastRecognizedId = None
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erro ao acessar a câmera. Verifique se está conectada e nenhum outro aplicativo a está usando.")
cap.set(3, 640)
cap.set(4, 480)
imgBackground = cv2.imread('Resources/background.png')
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
folderModePath = resource_path('Resources/Modes')
modePathList = os.listdir(folderModePath)
imgModeList = [cv2.imread(os.path.join(folderModePath, path)) for path in modePathList]
idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
file_path = resource_path('encodeFile.p')
file = open(file_path, 'rb')
encodeListKnown = pickle.load(file)
file.close()
modeType = 0
counter = 0
point_id = -1
imgEmployee = []
today_date = datetime.now().strftime("%Y-%m-%d")
last_recognized_time = {}
def fetch_data(userId, result_queue):
    global modeType
    employeeInfo = db.reference(f'Employees/{userId}').get()
    if employeeInfo:
        print("aqui esta apenas informando a employeeInfo")
        print(employeeInfo)
        blob_path = f"Images/{userId}/image1.jpeg"  # Usando 'image1.jpeg' como exemplo
        blob = bucket.get_blob(blob_path)
        if blob:
            print("consegui carregar o blob!")
            array = np.frombuffer(blob.download_as_string(), np.uint8)
            imgEmployee = cv2.imdecode(array, cv2.IMREAD_COLOR)
            if imgEmployee is None or not hasattr(imgEmployee, 'shape'):
                print("Erro na decodificacao")
                imgEmployee = None
            datetimeObject = datetime.strptime(employeeInfo['last_attendance_time'], "%Y-%m-%d %H:%M:%S")
            secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
            result_queue.put((datetimeObject, secondsElapsed, employeeInfo, imgEmployee))
            print("se passaram: ", secondsElapsed, "segundos")
            modeType = 0
        else:
            print("Erro na porra do blobbloblbob")
            imgEmployee = None
def identifyUser(encodeCurFrame, encodeListKnown, threshold=0.8):
    best_match = None
    highest_match_ratio = threshold
    for encodeFace in encodeCurFrame:
        for userId, userEncodings in encodeListKnown.items():
            matches = face_recognition.compare_faces(userEncodings, encodeFace)
            faceDis = face_recognition.face_distance(userEncodings, encodeFace)
            match_ratio = np.sum(matches) / len(matches)
            if match_ratio > highest_match_ratio:
                highest_match_ratio = match_ratio
                best_match = (userId, match_ratio, np.mean(faceDis))
    return best_match
while True:
    result_queue = Queue()
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)
    if faces:
        face = faces[0]
        for point_id in idList:
            cv2.circle(img, face[point_id], 5, (255, 0, 255), -1)
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 634, 808:808 + 414] = imgModeList[modeType]
    if faceCurFrame:
        bestMatch = identifyUser(encodeCurFrame, encodeListKnown)
        if bestMatch:
            userId, matchRatio, avgDistance = bestMatch
            if userId not in last_recognized_time or (datetime.now() - last_recognized_time[userId]).total_seconds() > 10:
                print(f"Reconhecido: {userId} com precisão de {matchRatio} e distância média de {avgDistance}")
                last_recognized_time[userId] = datetime.now()
                current_time = datetime.now()
                data_thread = threading.Thread(target=fetch_data, args=(userId, result_queue))
                data_thread.start()
                data_thread.join()
                datetimeObject, secondsElapsed, employeeInfo, imgEmployee = result_queue.get()
                if secondsElapsed > 46000:
                        print("entrou no primeiro secondsElapsed")
                        modeType = 1
                        ref = db.reference(f'Employees/{userId}')
                        entrance_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                        db.reference(f'/Employees/{userId}/daily_records/{today_date}/entrance').set(entrance_time)
                        new_datetime = datetimeObject + timedelta(seconds=1)
                        employeeInfo['total_attendance'] = new_datetime.strftime("%Y-%m-%d %H:%M:%S")
                        ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
                elif secondsElapsed > 3600:
                        modeType = 4
                        print("entrou no segundo secondsElapsed")
                        employeeRef = db.reference(f'Employees/{userId}')
                        new_datetime = datetimeObject + timedelta(seconds=1)
                        total_attendance = new_datetime.strftime("%Y-%m-%d %H:%M:%S")
                        employeeRef.update({'total_attendance': total_attendance, 'gone_in': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
                        dailyRecordRef = db.reference(f'Employees/{userId}/daily_records/{today_date}')
                        exit_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        dailyRecordRef.update({'exit': exit_time})
                        print("Registro de saída adicionado para hoje.")
                else:
                        new_datetime = datetimeObject + timedelta(seconds=1)
                        modeType = 2
                        counter = 0
                        imgBackground[44:44 + 634, 808:808 + 414] = imgModeList[modeType]
                        print("entrou no else das condicoes de secondsElapsed")
                if modeType != 4:
                        if 10 < counter < 20:
                            modeType = 2
                        imgBackground[44:44 + 634, 808:808 + 414] = imgModeList[modeType]
                if counter <= 10:
                    try:
                        print("ta indo colocar a imagem")
                        cv2.putText(imgBackground, str(employeeInfo['role']), (1006, 550),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                        cv2.putText(imgBackground, str(employeeInfo['name']), (1006, 493),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                        (w, h), _ = cv2.getTextSize(employeeInfo['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                        offset = (414 - w) // 2
                        cv2.putText(imgBackground, str(employeeInfo['name']), (808 + offset, 445),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)
                        imgBackground[175:175 + 216, 909:909 + 216] = imgEmployee
                        print("mana ja passou a imagem")
                    except (NameError, KeyError) as e:
                        print("Erro:", e)
                        modeType = 4
                modeType = 2
    else:
        modeType = 0
        counter = 0
    cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendence", imgBackground)
    cv2.waitKey(10)

