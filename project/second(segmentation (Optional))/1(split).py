import os
import shutil

# Define paths
base_dir = r'C:\Users\phili\Downloads\WCEBleedGen\WCEBleedGen'
forseccode_dir = os.path.join(base_dir, 'forseccode')

# Create destination directories for 'forseccode' labels
for phase in ['train', 'val']:
    for label_type in ['bleeding', 'non-bleeding']:
        label_folder = os.path.join(forseccode_dir, 'labels', phase, label_type, 'Annotation')
        os.makedirs(label_folder, exist_ok=True)

# Copy bleeding annotations to 'forseccode' directories
bleeding_annotations_dir = os.path.join(base_dir, 'bleeding', 'Annotations')
bleeding_train_images = os.listdir(os.path.join(forseccode_dir, 'images', 'train', 'bleeding'))
bleeding_val_images = os.listdir(os.path.join(forseccode_dir, 'images', 'val', 'bleeding'))

def clean_image_number(image_filename):
    # Extract the number between the parentheses and remove spaces
    image_number = image_filename.split('(')[-1].split(')')[0].replace(' ', '')
    return image_number

for phase, images in [('train', bleeding_train_images), ('val', bleeding_val_images)]:
    for image in images:
        image_number = clean_image_number(image)
        source_annotation_path = os.path.join(bleeding_annotations_dir, f'ann- ({image_number}).png')
        destination_annotation_path = os.path.join(forseccode_dir, 'labels', phase, 'bleeding', 'Annotation', f'img- ({image_number}).png')
        
        # Check if the source annotation file exists before copying
        if os.path.exists(source_annotation_path):
            shutil.copyfile(source_annotation_path, destination_annotation_path)

# Copy non-bleeding annotations to 'forseccode' directories
non_bleeding_annotations_dir = os.path.join(base_dir, 'non-bleeding', 'annotation')
non_bleeding_train_images = os.listdir(os.path.join(forseccode_dir, 'images', 'train', 'non-bleeding'))
non_bleeding_val_images = os.listdir(os.path.join(forseccode_dir, 'images', 'val', 'non-bleeding'))

for phase, images in [('train', non_bleeding_train_images), ('val', non_bleeding_val_images)]:
    for image in images:
        image_number = clean_image_number(image)
        source_annotation_path = os.path.join(non_bleeding_annotations_dir, f'ann- ({image_number}).png')
        destination_annotation_path = os.path.join(forseccode_dir, 'labels', phase, 'non-bleeding', 'Annotation', f'img- ({image_number}).png')
        
        # Check if the source annotation file exists before copying
        if os.path.exists(source_annotation_path):
            shutil.copyfile(source_annotation_path, destination_annotation_path)
