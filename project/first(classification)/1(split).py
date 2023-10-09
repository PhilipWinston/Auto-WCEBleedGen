import os
import random
import shutil

# Define paths
base_dir = r'C:\Users\phili\Downloads\WCEBleedGen\WCEBleedGen'
bleeding_dir = os.path.join(base_dir, 'bleeding')
non_bleeding_dir = os.path.join(base_dir, 'non-bleeding')
forfirstcode_dir = os.path.join(base_dir, 'forfirstcode')

# Create destination directories for 'forfirstcode'
for phase in ['train', 'val']:
    for label_type in ['bleeding', 'non-bleeding']:
        folder_path = os.path.join(forfirstcode_dir, phase, label_type)
        os.makedirs(folder_path, exist_ok=True)

# Get a list of bleeding and non-bleeding images
bleeding_images = [f for f in os.listdir(os.path.join(bleeding_dir, 'Images')) if f.endswith('.png')]
non_bleeding_images = [f for f in os.listdir(os.path.join(non_bleeding_dir, 'images')) if f.endswith('.png')]

# Randomly shuffle the lists
random.shuffle(bleeding_images)
random.shuffle(non_bleeding_images)

# Calculate split indices
bleeding_split = int(0.8 * len(bleeding_images))
non_bleeding_split = int(0.8 * len(non_bleeding_images))

# Split the dataset into training and validation sets
train_bleeding = bleeding_images[:bleeding_split]
val_bleeding = bleeding_images[bleeding_split:]
train_non_bleeding = non_bleeding_images[:non_bleeding_split]
val_non_bleeding = non_bleeding_images[non_bleeding_split:]

# Copy bleeding images to 'forfirstcode' directories
for phase, images in [('train', train_bleeding), ('val', val_bleeding)]:
    for image in images:
        source_path = os.path.join(bleeding_dir, 'Images', image)
        destination_path = os.path.join(forfirstcode_dir, phase, 'bleeding', image)
        shutil.copyfile(source_path, destination_path)

# Copy non-bleeding images to 'forfirstcode' directories
for phase, images in [('train', train_non_bleeding), ('val', val_non_bleeding)]:
    for image in images:
        source_path = os.path.join(non_bleeding_dir, 'images', image)
        destination_path = os.path.join(forfirstcode_dir, phase, 'non-bleeding', image)
        shutil.copyfile(source_path, destination_path)
