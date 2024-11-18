# Pseudo code 4.13 - Morphological Operations (Closing after Opening)
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_opening, binary_closing

# Read the image
plt.show()
file_path = 'P7/Data Image/Noisegray50%Gaussian.png'
I = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
I = I.astype(float)

# Define the structuring element (8-connectivity)
B = np.ones((3, 3))

# Perform morphological opening
Open = binary_opening(I, structure=B).astype(float)

# Perform morphological closing on the result of opening
Close = binary_closing(Open, structure=B).astype(float)

# Display the original image
plt.figure(figsize=(6, 6))
plt.imshow(I, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.show()

# Display the result of the morphological operations (CoO)
plt.figure(figsize=(6, 6))
plt.imshow(Close, cmap='gray')
plt.title("Result of Opening followed by Closing")
plt.axis('off')
plt.show()