from ultralytics import YOLO

import numpy as np


model = YOLO(r'C:\Users\phili\runs\classify\train5\weights\last.pt')  # load a custom model

results = model(r"C:\Users\phili\Downloads\WCEBleedGen\forfirstcode\train\bleeding\img- (40).png")  # predict on an image

names_dict = results[0].names

probs = results[0].probs.data.tolist()

print(names_dict)
print(probs)

print(names_dict[np.argmax(probs)])
