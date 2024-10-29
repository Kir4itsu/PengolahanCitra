# Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Set file path
file_path = 'P7/Data Image/ImageEdgeGray.png'

# Read the image
img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded
if img is None:
    print(f"Error: Gambar tidak ditemukan di path {file_path}.")
else:
    # Display the image
    plt.figure(figsize=(6, 6))
    plt.imshow(img, cmap='gray')
    plt.title("Original Gray-level Image")
    plt.axis('off')
    plt.show()
