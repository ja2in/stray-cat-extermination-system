import datetime
import cv2
from ultralytics import YOLO
import youtube_dl
import serial
import time

CONFIDENCE_THRESHOLD = 0.6
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

coco128 = open(r'ultralytics/data/scripts/gorani.yaml', 'r', encoding='utf-8')
data = coco128.read()
class_list = data.split('\n')
coco128.close()

model = YOLO(r'C:\yoloV8\ultralytics-main\best (50).pt')

#아두이노와 시리얼 통신 설정
arduino = serial.Serial('com4', 115200)
time.sleep(1)
gorani_class_id = 0

# YouTube 동영상 URL 설정
video_url = "Youtube link"

# 동영상 다운로드 및 재생
ydl_opts = {
    'format': 'best',
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    video_url = info_dict['url']

cap = cv2.VideoCapture(video_url)

while True:
    start = datetime.datetime.now()

    ret, frame = cap.read()
    if not ret:
        print('Video Error')
        break

    detection = model(frame)[0]

    for data in detection.boxes.data.tolist():
        confidence = float(data[4])
        if confidence < CONFIDENCE_THRESHOLD:
            continue

        xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])
        class_id = int(data[5])
        class_name = class_list[class_id]
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), GREEN, 2)
        # 소수점 이하 자리를 제거하여 유사도를 정수로 표시
        cv2.putText(frame, class_name + ' ' + str(int(confidence * 100)) + '%', (xmin, ymin), cv2.FONT_ITALIC, 1, WHITE, 2)
        
        # 사물이 인식된 경우 신호 전송
        if class_id == gorani_class_id:
            arduino.write(b'1')
        else:
            arduino.write(b'0')
    end = datetime.datetime.now()

    total = (end - start).total_seconds()
    print(f'Time to process 1 frame: {total * 1000:.0f} milliseconds')

    fps = f'FPS: {1 / total:.2f}'
    cv2.putText(frame, fps, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
