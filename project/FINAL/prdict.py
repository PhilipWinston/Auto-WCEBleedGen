from ultralytics import YOLO
import numpy as np
from PIL import Image

# Load the classification model
classification_model = YOLO(r'C:\Users\phili\runs\classify\train5\weights\last.pt')

# Load the object detection model
object_detection_model = YOLO(r"C:\Users\phili\runs\detect\train\weights\best.pt")

# Define a function to determine if an image contains bleeding
def is_bleeding(image_path):
    # Perform classification to determine if it contains bleeding
    classification_results = classification_model(image_path)
    names_dict = classification_results[0].names
    probs = classification_results[0].probs.data.tolist()
    predicted_class = names_dict[np.argmax(probs)]
    bleeding_present = predicted_class == "bleeding"

    if bleeding_present:
        # If bleeding is present, perform object detection to locate bleeding regions
        object_detection_results = object_detection_model(source=image_path, show=True, save=True)
        print(object_detection_results)
        # Open an image
        image_path = r'C:\Users\phili\runs\detect\predict\img- (1042).png'
        img = Image.open(image_path)
        # Display the image (optional)
        img.show()
    return bleeding_present

# Example image path
image_path = r"C:\Users\phili\Downloads\WCEBleedGen\WCEBleedGen\bleeding\Images\img- (1042).png"

# Determine if the image contains bleeding and locate bleeding regions if present
if is_bleeding(image_path):
    print("Image contains bleeding.")
else:
    print("Image does not contain bleeding.")
