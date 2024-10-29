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

# Display original image
plt.figure(figsize=(6, 6))
plt.imshow(Im, cmap='gray')
plt.title("Original Gray-level Image")
plt.axis('off')
plt.show()

# Calculate gradient pixel by pixel
N, M = Im.shape
Gy = np.zeros((N-1, M-1))
Gx = np.zeros((N-1, M-1))
G = np.zeros((N-1, M-1))

for n in range(N-1):
    for m in range(M-1):
        Gy[n, m] = abs(Im[n+1, m+1] - Im[n, m])  # Gradient 45º
        Gx[n, m] = abs(Im[n, m+1] - Im[n+1, m])  # Gradient 135º
        G[n, m] = np.sqrt(Gx[n, m]**2 + Gy[n, m]**2)  # Total gradient

# Display total gradient
plt.figure(figsize=(6, 6))
plt.imshow(G, cmap='gray')
plt.title("Total Gradient (45º and 135º)")
plt.axis('off')
plt.show()
