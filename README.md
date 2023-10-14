# OpenCV와 IoT 기술을 이용한 길고양이 퇴치 시스템 

## :point_up: 연구 배경 및 목적
* 길고양이를 퇴치하는 '전기 펜스 설치', '담장 위 장애물 설치', '동작 감지', '스프링 쿨러' 등의 방법들은 복잡하고 고비용을 요구
* 학교 내에 길고양이 퇴치 시스템이 충분하지 않음
* 길고양이의 건물 내 침입방지를 위한 간단한 시스템을 OpenCV와 아두이노를 이용하여 구현
<br></br>
## :v: 설계 사양 (개발환경)
* Python (3.10 ver)
* OpenCV (4.1.2 ver)
* YOLO
* 아두이노 (Arduino IDE v 2.0.3, AVR studio4)
* DESKTOP (Windows 10)
* 화상 카메라 (Microsoft Lifecam HD-3000)
* 서보 모터, 녹음모듈
<br></br>
## 👌 OpenCV Code && Arduino Test
<table>
  <tr>
    <td><img alt="" src="https://github.com/ja2in/Data_Structure/assets/101400945/f79c4b59-681b-4f88-a4c6-faf34a847d41" /></td><td><img alt="" src="https://github.com/ja2in/Data_Structure/assets/101400945/826aadf1-76cf-471c-aa09-23843416f8c3 " /></td><td><img alt="" src="https://github.com/ja2in/Data_Structure/assets/101400945/8b06142c-c6e7-4502-8d56-66ee049322f7" /></td>
  <tr>
</table>

[23.08.29]
* youtubeTestCode.py 코드와 유튜브 영상을 통해 '고양이 얼굴 인식' 테스트를 진행
<br></br>
<br></br>

<table>
  <tr>
    <td><img alt="" src="https://github.com/ja2in/Stray-cat-extermination-system/assets/101400945/e5064ec5-9997-41af-a27e-6a6ab0f73f34" /></td><td><img alt="" src="https://github.com/ja2in/Stray-cat-extermination-system/assets/101400945/abf1812c-f30f-4f40-b7c7-7b50520877b5" /></td><td><img alt="" src="https://github.com/ja2in/Stray-cat-extermination-system/assets/101400945/6bdbd367-37fe-4582-bb47-41a541d4d16c" /></td>
  <tr>
</table>

[23.08.30] 
* cvlibTestCode.py 코드를 이용해 youtubeTestCode.py에서보다 좀 더 정확한 측정을 진행

<br></br>
<br></br>

<table>
  <tr>
    <td><img alt="" src="https://github.com/ja2in/Stray-cat-extermination-system/assets/101400945/9c7a740b-8d5d-487d-b6f5-5ef3ad13e8f4" /></td><td><img alt="" src="https://github.com/ja2in/Stray-cat-extermination-system/assets/101400945/f0658f27-a074-4846-9899-f71cfb3979b6" /></td>
  <tr>
</table>

[23.09.06] 
* moreAnimalTestCode.py 코드를 이용해 고양이 뿐만 아니라 다양한 동물들도 인식할 수 있도록 수정

<br></br>
<br></br>

<table>
  <tr>
    <td><img alt="" src="https://github.com/ja2in/Stray-cat-extermination-system/assets/101400945/df39d4c8-84ed-439f-940c-4438c1006764" /></td><td><img alt="" src="https://github.com/ja2in/Stray-cat-extermination-system/assets/101400945/314754bd-985d-4318-9c3b-1f28b1d2815b" /></td>
  <tr>
</table>

[23.09.11] 
* 카메라 모듈을 아두이노와 연결
* 기존 코드를 yolov3를 사용한 using yolov3.py 코드로 변경해 더 정확하고 다양한 객체 측정 가능

<br></br>
<br></br>

<table>
  <tr>
    <td><img alt="" src="https://github.com/ja2in/Stray-cat-extermination-system/assets/101400945/95af4a87-203e-4aae-9a6c-4d22c110df22" /></td><td><img alt="" src="https://github.com/ja2in/Stray-cat-extermination-system/assets/101400945/de9d18da-813b-4f19-82b7-15ebe7d2f82d" /></td><td><img alt="" src="https://github.com/ja2in/Stray-cat-extermination-system/assets/101400945/fb83f20f-3011-4fc5-9c74-791c918afb03" /></td>
  <tr>
</table>

[23.10.16]
* 아두이노에 소리모듈 연결 후 고양이가 인식되었을 때 소리 출력 테스트 완료
* 고양이 외 고라니를 객체 인식할 수 있도록 Colab을 통해 객체 학습을 진행

