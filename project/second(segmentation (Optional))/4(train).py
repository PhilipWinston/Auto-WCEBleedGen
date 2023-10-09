from ultralytics import YOLO
if __name__ == '__main__':
    model = YOLO('yolov8n-seg.pt')  # load a pretrained model (recommended for training)

    model.train(data=r"C:\Users\phili\OneDrive\Desktop\project\second\config.yaml", epochs=20, imgsz=224)