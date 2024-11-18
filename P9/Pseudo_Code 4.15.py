# Pseudo code 4.15 - Edge Detection using Morphological Operations
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_erosion, binary_dilation

# Read the image
file_path = 'P7/Data Image/Noisegray50%Gaussian.png'
I = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
I = I.astype(float)

# Define the structuring element (8-connectivity)
B = np.ones((3, 3))

# Perform morphological erosion
Erosi = binary_erosion(I, structure=B).astype(float)

# Perform morphological dilation
Dilasi = binary_dilation(I, structure=B).astype(float)

# Calculate the differences for edge detection
Tepi_DID = np.abs(I - Dilasi)  # Difference between image and dilation
Tepi_DIE = np.abs(I - Erosi)   # Difference between image and erosion
Tepi_DDE = np.abs(Dilasi - Erosi)  # Difference between dilation and erosion

# Display the original image
plt.figure(figsize=(6, 6))
plt.imshow(I, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.show()

# Display edge detection result (Difference I - Dilation)
plt.figure(figsize=(6, 6))
plt.imshow(Tepi_DID, cmap='gray')
plt.title("Edge Detection (I - Dilasi)")
plt.axis('off')
plt.show()

# Display edge detection result (Difference I - Erosion)
plt.figure(figsize=(6, 6))
plt.imshow(Tepi_DIE, cmap='gray')
plt.title("Edge Detection (I - Erosi)")
plt.axis('off')
plt.show()

# Display edge detection result (Difference Dilasi - Erosi)
plt.figure(figsize=(6, 6))
plt.imshow(Tepi_DDE, cmap='gray')
plt.title("Edge Detection (Dilasi - Erosi)")
plt.axis('off')
plt.show()