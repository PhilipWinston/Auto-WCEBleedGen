from ultralytics import YOLO
import numpy as np
from PIL import Image
import os
import pandas as pd

# Load the classification model
classification_model = YOLO(r"C:\Users\phili\OneDrive\Desktop\project\FINAL\classification.pt")

# Create an empty list to store the results
results_list = []

# Define a function to determine if an image contains bleeding
def is_bleeding(image_path):
    # Perform classification to determine if it contains bleeding
    classification_results = classification_model(image_path)
    names_dict = classification_results[0].names
    probs = classification_results[0].probs.data.tolist()
    predicted_class = names_dict[np.argmax(probs)]
    return predicted_class

# Directory containing the images
image_dir = r"C:\Users\phili\Downloads\Auto-WCEBleedGen Challenge Test Dataset\Auto-WCEBleedGen Challenge Test Dataset\Test Dataset 1"

# Iterate through all image files in the directory
for image_file in os.listdir(image_dir):
    if image_file.endswith(".png") or image_file.endswith(".jpg"):
        image_path = os.path.join(image_dir, image_file)

        # Determine if the image contains bleeding
        predicted_class = is_bleeding(image_path)

        # Append the result to the list
        results_list.append({"Image Name": image_file, "Predicted Class": predicted_class})

# Create a DataFrame from the list of results
results_df = pd.DataFrame(results_list)

# Save the results to an Excel file
results_excel_path = r"C:\Users\phili\OneDrive\Desktop\project\For test data set\bleeding_results(1).xlsx"
results_df.to_excel(results_excel_path, index=False)

print("Results saved to:", results_excel_path)
