# Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Set file path
file_path = 'P7/Data Image/ImageEdgeGray.png'

# Read the gray-level image
img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
Im = img.astype(float)

# Display original image
plt.figure(figsize=(6, 6))
plt.imshow(Im, cmap='gray')
plt.title("Original Gray-level Image")
plt.axis('off')
plt.show()

# Laplace operators
L1 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
L2 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
L3 = np.array([[1, 2, 1], [2, -12, 2], [1, 2, 1]])

# Apply Laplace operators using convolution
Ls1 = np.abs(convolve(Im, L1))
Ls2 = np.abs(convolve(Im, L2))
Ls3 = np.abs(convolve(Im, L3))

# Display the result of each Laplace operator
plt.figure(figsize=(6, 6))
plt.imshow(Ls1, cmap='gray')
plt.title("Laplace Gradient (Operator 1)")
plt.axis('off')
plt.show()

plt.figure(figsize=(6, 6))
plt.imshow(Ls2, cmap='gray')
plt.title("Laplace Gradient (Operator 2)")
plt.axis('off')
plt.show()

plt.figure(figsize=(6, 6))
plt.imshow(Ls3, cmap='gray')
plt.title("Laplace Gradient (Operator 3)")
plt.axis('off')
plt.show()
