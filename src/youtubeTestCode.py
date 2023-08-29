import cv2, pafy

# 고양이 탐지기 모델 불러오기
cat_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
 
url = 'youtube link'
video = pafy.new(url)
best_stream = video.getbest()
cap = cv2.VideoCapture()
cap.open(best_stream.url)

while True:
    # 비디오 프레임 읽기
    ret, frame = cap.read()

    # 회색조로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 고양이 탐지
    cats = cat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 탐지된 고양이 주위에 사각형 그리기
    for (x, y, w, h) in cats:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

    # 화면에 프레임 표시
    cv2.imshow('Cat Detection', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()
