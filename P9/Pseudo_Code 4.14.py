# Pseudo code 4.14 - Morphological Operations (Opening after Closing)
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_opening, binary_closing

# Read the image
file_path = 'P7/Data Image/Noisegray50%Gaussian.png'
I = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
I = I.astype(float)

# Define the structuring element (8-connectivity)
B = np.ones((3, 3))

# Perform morphological closing
Close = binary_closing(I, structure=B).astype(float)

# Perform morphological opening on the result of closing
Open = binary_opening(Close, structure=B).astype(float)

# Display the original image
plt.figure(figsize=(6, 6))
plt.imshow(I, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.show()

# Display the result of the morphological operations (OoC)
plt.figure(figsize=(6, 6))
plt.imshow(Open, cmap='gray')
plt.title("Result of Closing followed by Opening")
plt.axis('off')
plt.show()