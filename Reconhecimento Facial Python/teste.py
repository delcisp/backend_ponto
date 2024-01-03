import os
import pickle
import cv2
import face_recognition
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime, timedelta
cred = credentials.Certificate("accountKey.json")
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
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = [cv2.imread(os.path.join(folderModePath, path)) for path in modePathList]
idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
file = open('encodeFile.p', 'rb')
encodeListKnown, employeesIds = pickle.load(file)
file.close()
modeType = 0
counter = 0
id = -1
imgEmployee = []
today_date = datetime.now().strftime("%Y-%m-%d")
last_recognized_time = {}
while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)
    if faces:
        face = faces[0]  # Obtenha o primeiro rosto (ou ajuste conforme necessário)
        for id in idList:
            cv2.circle(img, face[id], 5, (255, 0, 255), -1)
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 634, 808:808 + 414] = imgModeList[modeType]
    if faceCurFrame and (id not in last_recognized_time or (datetime.now() - last_recognized_time[id]).total_seconds() > 50):
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex]:
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                id = employeesIds[matchIndex]
                current_time = datetime.now()
                last_recognized_time[id] = current_time
                if counter == 0:
                    counter = 1
                    leftUp = face[159]
                    leftDown = face[23]
                    leftLeft = face[130]
                    leftRight = face[243]
                    lengthVer, _ = detector.findDistance(leftUp, leftDown)
                    lengthHor, _ = detector.findDistance(leftLeft, leftRight)
                    ratio = int((lengthVer / lengthHor) * 100)
                    threshold_lengthVer = 10
                if ratio < 30 and lengthVer > threshold_lengthVer:
                    blinkCounter += 1
                    print(f'ei tu piscou! ta na piscada {blinkCounter}')
                elif counter == 1:
                    counter = 2
                    employeeInfo = db.reference(f'Employees/{id}').get()
                    print("aqui esta apenas informando a employeeInfo")
                    print(employeeInfo)
                    blob = bucket.get_blob(f'Images/{id}.jpeg')
                    array = np.frombuffer(blob.download_as_string(), np.uint8)
                    imgEmployee = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)
                    datetimeObject = datetime.strptime(employeeInfo['last_attendance_time'], "%Y-%m-%d %H:%M:%S")
                    secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
                    print("se passaram: ", secondsElapsed, "segundos")
                    modeType = 0
                    if secondsElapsed > 46000:
                        print("entrou no primeiro secondsElapsed")
                        modeType = 1
                        ref = db.reference(f'Employees/{id}')
                        entrance_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                        db.reference(f'/Employees/{id}/daily_records/{today_date}/entrance').set(entrance_time)
                        new_datetime = datetimeObject + timedelta(seconds=1)
                        employeeInfo['total_attendance'] = new_datetime.strftime("%Y-%m-%d %H:%M:%S")
                        ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
                    elif secondsElapsed > 3600:
                        modeType = 4
                        print("entrou no segundo secondsElapsed")
                        employeeRef = db.reference(f'Employees/{id}')
                        new_datetime = datetimeObject + timedelta(seconds=1)
                        total_attendance = new_datetime.strftime("%Y-%m-%d %H:%M:%S")
                        employeeRef.update({'total_attendance': total_attendance, 'gone_in': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
                        dailyRecordRef = db.reference(f'Employees/{id}/daily_records/{today_date}')
                        exit_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        dailyRecordRef.update({'exit': exit_time})
                        print("Registro de saída adicionado para hoje.")
                    else:
                        new_datetime = datetimeObject + timedelta(seconds=1)
                        modeType = 2
                        counter = 0
                        imgBackground[44:44 + 634, 808:808 + 414] = imgModeList[modeType]
                        print("entrou no else do ifsecondsElapsed > 50")
                if modeType != 4:
                    if 10 < counter < 20:
                        modeType = 2
                    imgBackground[44:44 + 634, 808:808 + 414] = imgModeList[modeType]
                    if counter <= 10:
                      try:
                        cv2.putText(imgBackground, str(employeeInfo['role']), (1006, 550),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                        cv2.putText(imgBackground, str(employeeInfo['name']), (1006, 493),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                        (w, h), _ = cv2.getTextSize(employeeInfo['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                        offset = (414 - w) // 2
                        cv2.putText(imgBackground, str(employeeInfo['name']), (808 + offset, 445),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)
                        imgBackground[175:175 + 216, 909:909 + 216] = imgEmployee
                      except (NameError, KeyError) as e:
                        print("Erro:", e)
                        modeType = 4
                    counter += 1
                    if counter >= 20:
                        counter = 0
                        modeType = 0
                        employeeInfo = []
                        imgEmployee = []
                        imgBackground[44:44 + 634, 808:808 + 414] = imgModeList[modeType]
    else:
        modeType = 0
        counter = 0
    cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendence", imgBackground)
    cv2.waitKey(1)
