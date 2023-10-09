from ultralytics import YOLO
if __name__ == '__main__':
# Load a model
    model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
    results = model.train(data=r"C:\Users\phili\OneDrive\Desktop\project\third\config.yml", epochs=100,imgsz=224)  # train the model