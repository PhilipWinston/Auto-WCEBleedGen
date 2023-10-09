from ultralytics import YOLO
import cv2
import PIL
# Load a model
model = YOLO(r"C:\Users\phili\runs\detect\train\weights\best.pt")  # load a custom model

# Predict with the model
results = model(source=r"C:\Users\phili\Downloads\WCEBleedGen\WCEBleedGen\bleeding\Images\img- (1042).png",show=True,save=True) 
print(results)