import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import pafy

# YouTube 동영상 URL
url = 'youtube link'

# YouTube 동영상 가져오기
video = pafy.new(url)
best_stream = video.getbest()
cap = cv2.VideoCapture()
cap.open(best_stream.url)

while True:
    # 비디오 프레임 읽기
    ret, frame = cap.read()

    # 객체 탐지 수행
    bbox, label, conf = cv.detect_common_objects(frame)

    # 고양이 클래스만 선택
    selected_bbox = []
    selected_label = []
    selected_conf = []

    for idx, obj_label in enumerate(label):
        if obj_label == 'cat':
            selected_bbox.append(bbox[idx])
            selected_label.append(obj_label)
            selected_conf.append(conf[idx])

    # 감지된 고양이 객체에 사각형 및 레이블 그리기
    output_image = draw_bbox(frame, selected_bbox, selected_label, selected_conf)

    # 화면에 프레임 표시
    cv2.imshow('Cat Detection', output_image)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()
