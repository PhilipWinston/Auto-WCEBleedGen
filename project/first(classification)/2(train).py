from ultralytics import YOLO
if __name__ == '__main__':
    # Your code here

    model = YOLO('yolov8n-cls.pt')  # load a pretrained model (recommended for training)

    model.train(data=r"C:\Users\phili\Downloads\WCEBleedGen\forfirstcode",
            epochs=20, imgsz=224)