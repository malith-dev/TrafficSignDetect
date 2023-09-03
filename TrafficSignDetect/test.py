
import cv2
from ultralytics import YOLO

# cap = cv2.VideoCapture(0)  # For Webcam
# cap.set(3, 1280)
# cap.set(4, 720)


# cap = cv2.VideoCapture('http://192.168.55.144:4747/video')
# cap.set(3, 1280)
# cap.set(4, 720)

model = YOLO('Traffic Sign detection/model2.pt')


# while True:
#     success, img = cap.read()
#     results = model(img, show=True)




# results = model("D:\Lecture notes\SEMESTER 7\irp\Object-detection-YOLO\Traffic Sign detection\Videos\Signs2.mp4", show=True)
results = model("Videos/16.mp4", show=True)
cv2.waitKey(0)
#
# @misc{ traffic-signs-detection-uudww_dataset,
#     title = { Traffic Signs Detection Dataset },
#     type = { Open Source Dataset },
#     author = { Mohamed Atef },
#     howpublished = { \url{ https://universe.roboflow.com/mohamed-atef-dwbkp/traffic-signs-detection-uudww } },
#     url = { https://universe.roboflow.com/mohamed-atef-dwbkp/traffic-signs-detection-uudww },
#     journal = { Roboflow Universe },
#     publisher = { Roboflow },
#     year = { 2023 },
#     month = { jan },
#     note = { visited on 2023-04-30 },
# }
