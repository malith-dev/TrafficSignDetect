import cv2
from ultralytics import YOLO

# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)
# cap.set(4, 720)

# cap = cv2.VideoCapture('http://192.168.55.144:4747/video')
# cap.set(3, 1280)
# cap.set(4, 720)

model = YOLO('D:\Lecture notes\SEMESTER 7\irp\Object-detection-YOLO\Traffic Sign detection\model2.pt')



results = model("Videos/16.mp4", show=True)
cv2.waitKey(0)

