import datetime
import cv2
from ultralytics import YOLO
import serial
import time

# 객체 감지를 위한 임계값 및 색깔 상수 정의
CONFIDENCE_THRESHOLD = 0.6
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# YOLO 모델 설정 파일 (gorani.yaml)에서 클래스 목록 로드
coco128 = open(r'ultralytics/data/scripts/gorani.yaml', 'r', encoding='utf-8')
data = coco128.read()
class_list = data.split('\n')
coco128.close()
gorani_class_id = 0
try:
    # YOLO 객체 감지 모델 초기화
    model = YOLO(r'C:\yoloV8\ultralytics-main\best (50).pt')
except Exception as e:
    print(f"Error initializing the YOLO model: {e}")
    exit()

# 아두이노와 시리얼 통신 설정
arduino = serial.Serial('com4', 115200)
time.sleep(1)

# ESP32-CAM이 제공하는 비디오 스트림 URL 설정
video_url = "http://192.168.215.22:81/stream"
cap = cv2.VideoCapture(video_url)

# 비디오 스트림을 성공적으로 열지 못한 경우 오류 출력하고 종료
if not cap.isOpened():
    print('Video Error: Cannot open the video stream')
    exit()

while True:
    start = datetime.datetime.now()

    ret, frame = cap.read()
    if not ret:
        print('Video Error: Cannot read a frame')
        break

    detection = model(frame)[0]

    for data in detection.boxes.data.tolist():
        confidence = float(data[4])
        if confidence < CONFIDENCE_THRESHOLD:
            continue

        xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])
        class_id = int(data[5])
        class_name = class_list[class_id]

        # 객체 경계 상자 그리기 및 클래스 이름 및 신뢰도 텍스트 표시
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), GREEN, 2)
        cv2.putText(frame, class_name + ' ' + str(int(confidence * 100)) + '%', (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)

        # 특정 클래스 (예: gorani)가 인식된 경우 아두이노에 신호 전송 (1을 전송)
        if class_id == gorani_class_id:
            arduino.write(b'1')
        else:
            arduino.write(b'0')

    end = datetime.datetime.now()

    # 프레임 처리 시간 및 FPS 계산 및 출력
    total = (end - start).total_seconds()
    print(f'Time to process 1 frame: {total * 1000:.0f} milliseconds')
    fps = f'FPS: {1 / total:.2f}'
    cv2.putText(frame, fps, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # 화면에 프레임 표시
    cv2.imshow('ESP32-CAM', frame)

    # 'q' 키를 누르면 루프 종료
    if cv2.waitKey(1) == ord('q'):
        break

# 비디오 스트림 종료 및 창 닫기
cap.release()
cv2.destroyAllWindows()
