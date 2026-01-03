from ultralytics import YOLO
model = YOLO("yolov8n.pt")
def detect(frame):
    return model(frame)
