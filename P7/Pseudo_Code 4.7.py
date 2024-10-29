# Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Set file path
file_path = 'P7/Data Image/Noisegray50%Gaussian.png'

# Read the image
I = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

# First derivative of Gaussian filter
s = 1.0  # Example sigma value
A = -(1 / (2 * np.pi * s**4))
C = (2 * s**2)
bx = np.zeros((7, 7))
by = np.zeros((7, 7))
for i in range(7):
    for j in range(7):
        bx[i, j] = (i - 3) * A * np.exp(-(((i - 3)**2 + (j - 3)**2) / C))
        by[i, j] = (j - 3) * A * np.exp(-(((i - 3)**2 + (j - 3)**2) / C))

Iprim_x = np.abs(convolve(I.astype(float), bx))
Iprim_y = np.abs(convolve(I.astype(float), by))
Iprim = Iprim_x + Iprim_y

# Display edge-detected image
plt.figure(figsize=(6, 6))
plt.imshow(Iprim, cmap='gray')
plt.title("Edge Detection using First Derivative of Gaussian")
plt.axis('off')
plt.show()
