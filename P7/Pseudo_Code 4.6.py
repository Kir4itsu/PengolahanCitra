# Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Set file path
file_path = 'P7/Data Image/Noisegray50%Gaussian.png'

# Read the image
I = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

# Gaussian filter
s = 1.0  # Example sigma value
A = (1 / (2 * np.pi * s**2))
C = (2 * s**2)
b = np.zeros((7, 7))
for i in range(7):
    for j in range(7):
        b[i, j] = A * np.exp(-(((i-3)**2 + (j-3)**2) / C))

Iprim = convolve(I.astype(float), b)

# Display filtered image
plt.figure(figsize=(6, 6))
plt.imshow(Iprim, cmap='gray')
plt.title("Filtered Image with Gaussian Filter")
plt.axis('off')
plt.show()
