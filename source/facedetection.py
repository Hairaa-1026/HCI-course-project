import cv2
import numpy as np

cv2.namedWindow("Face_Detect")  # 定义一个窗口
cap = cv2.VideoCapture(0)  # 捕获摄像头图像
success, frame = cap.read()  # 读入第一帧
path = r'C:\Users\Hairaa\anaconda3\Lib\site-packages\cv2\data'
classifier = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
classifier.load(path + '\haarcascade_frontalface_default.xml')

while success:  # 如果读入帧正常
    size = frame.shape[:2]
    image = np.zeros(size, dtype=np.float16)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.equalizeHist(image, image)
    divisor = 8
    h, w = size
    minSize = (int(w / divisor), int(h / divisor))  # 像素一定是整数，或者用w//divisor

    faceRects = classifier.detectMultiScale(image, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, minSize)
    # 人脸识别

    if len(faceRects) > 0:
        for faceRect in faceRects:
            x, y, w, h = faceRect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 矩形轮廓

    cv2.imshow("Face_Detect", frame)
    # 显示轮廓
    success, frame = cap.read()  # 如正常则读入下一帧
    key = cv2.waitKey(200)
    c = chr(int(key) & 255)
    if c in ['q', 'Q', chr(27)]:  # 如果键入‘q'退出循环
        print('exit')
        break  # 退出循环

# 循环结束则清零
cap.release()
cv2.destroyAllWindows()
