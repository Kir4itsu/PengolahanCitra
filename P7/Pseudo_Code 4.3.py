# Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Set file path
file_path = 'P7/Data Image/ImageEdgeGray.png'

# Read the image
img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
Im = img.astype(float)

# Sobel kernels
Sx = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
Sy = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

# Sobel gradient
Gsx = convolve(Im, Sx)
Gsy = convolve(Im, Sy)
GS = np.abs(Gsx) + np.abs(Gsy)

# Display Sobel gradient
plt.figure(figsize=(6, 6))
plt.imshow(GS, cmap='gray')
plt.title("Sobel Gradient (Manual Convolution)")
plt.axis('off')
plt.show()
