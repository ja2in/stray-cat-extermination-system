import cv2
import urllib.request
import numpy as np
import serial
import time

url = 'http://192.168.215.22/cam-hi.jpg'
winName = 'ESP32 CAMERA'

classNames = []
classFile = r'C:\yoloV3\python\infor\coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = r'C:\yoloV3\python\infor\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt' #YOLO 환경설정파일
weightsPath = r'C:\yoloV3\python\infor\frozen_inference_graph.pb' #사전 훈련된 가중치들

cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)
net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

#아두이노와 시리얼 통신 설정
arduino = serial.Serial('com5', 115200)
time.sleep(1)

cat_class_id = 17
'''for idx, class_name in enumerate(classNames):
    if class_name == 'cat':
        cat_class_id = idx
        break'''

while(1):
    try:
        #이미지 가져오기
        imgResponse = urllib.request.urlopen (url) #abrimos el URL
        imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
        img = cv2.imdecode (imgNp,-1) #decodificamos

        #사물인식
        classIds, confs, bbox = net.detect(img,confThreshold=0.5)
        print(classIds,bbox)

        #사물인식된 경우 박스 및 테스트 입력
        if len(classIds) != 0:
            for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
                cv2.rectangle(img,box,color=(0,255,0),thickness = 3) #mostramos en rectangulo lo que se encuentra
                cv2.putText(img, classNames[classId-1], (box[0]+10,box[1]+30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0),2)

                # 'cat' 클래스가 탐지되면 아두이노에 메시지 전송
                if classId == cat_class_id:
                    arduino.write(b'1')
                else:
                    arduino.write(b'0')

            cv2.imshow(winName,img) # mostramos la imagen

    except:
        pass

    #ESC key 입력
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
    
cv2.destroyAllWindows()
