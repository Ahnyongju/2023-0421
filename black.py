import cv2
import os
import time

# 카메라 객체 생성
cap = cv2.VideoCapture(0)

# 캡처한 이미지를 저장할 디렉토리 생성
if not os.path.exists('captures'):
    os.makedirs('captures')

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 흑백 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 영상 출력
    cv2.imshow('Black and White Video', gray)

    # 키 입력 확인
    key = cv2.waitKey(1)

    # 'c' 키를 누르면 이미지 캡처
    if key == ord('c'):
        img_name = f'captures/capture_{str(int(time.time()))}.png'
        cv2.imwrite(img_name, gray)  # 흑백 이미지 사용
        print(f'Captured image saved as {img_name}')

    # 'q' 키를 누르면 종료
    elif key == ord('q'):
        break

# 카메라 및 창 닫기
cap.release()
cv2.destroyAllWindows()
