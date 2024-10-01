import os
import cv2

def apply_clahe(image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(image)

def preprocess_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Ensure output directory exists
    
    for image_name in os.listdir(input_dir):
        if image_name.endswith((".png", ".jpg", ".jpeg")):  # Only process image files
            image_path = os.path.join(input_dir, image_name)
            print(f"Processing {image_path}")  # Print the file being processed
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            
            if image is None:
                print(f"Failed to read {image_path}")
                continue
            
            processed_image = apply_clahe(image)
            output_path = os.path.join(output_dir, image_name)
            cv2.imwrite(output_path, processed_image)
            print(f"Saved processed image to {output_path}")

# Specify the directories
input_directory = "/content/Data"  # Path to your input data
output_directory = "/content/preprocessed_images"  # Path where preprocessed images will be saved

# Preprocess the images
preprocess_images(input_directory, output_directory)
