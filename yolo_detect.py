
import torch
from PIL import Image
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detect_objects(frame):
    results = model(frame)
    results.print()
    return results.pandas().xyxy[0]

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        detections = detect_objects(frame)
        print(detections[['name', 'confidence']])
        cv2.imshow('YOLO Detection', frame)
        if cv2.waitKey(1) == ord('q'):
            break
