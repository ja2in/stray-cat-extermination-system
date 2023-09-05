import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import pafy

url = 'youtube link'
video = pafy.new(url)
best_stream = video.getbest()
cap = cv2.VideoCapture()
cap.open(best_stream.url)

target_classes = ['cat', 'dog', 'bird', 'horse', 'elephant', 'sheep', 'cow', 'giraffe', 'zebra', 'bear']

while True:
    ret, frame = cap.read()

    bbox, label, conf = cv.detect_common_objects(frame)

    selected_bbox = []
    selected_label = []
    selected_conf = []

    for idx, obj_label in enumerate(label):
        if obj_label in target_classes:
            selected_bbox.append(bbox[idx])
            selected_label.append(obj_label)
            selected_conf.append(conf[idx])

    output_image = draw_bbox(frame, selected_bbox, selected_label, selected_conf)

    cv2.imshow('Object Detection', output_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
