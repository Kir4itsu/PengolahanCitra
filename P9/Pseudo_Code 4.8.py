import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

file_path = 'P7/Data Image/Noisegray50%Gaussian.png'

# Read the image
I = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

# Input the standard deviation (sigma)
s = float(input('Masukkan nilai standar deviasi (sigma): '))

# Calculate the coefficients for the LoG filter
A = -(1 / (np.pi * s**4))
C = (2 * s**2)
b = np.zeros((11, 11))  # Create an 11x11 kernel for LoG filter
for i in range(11):
    for j in range(11):
        D = -(((i - 5)**2 + (j - 5)**2) / C)
        b[i, j] = A * (1 + D) * np.exp(D)

# Apply the LoG filter using convolution
Iprim = np.abs(convolve(I.astype(float), b))

# Display the original image
plt.figure(figsize=(6, 6))
plt.imshow(I, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.show()

# Display the filtered image (edge detection)
plt.figure(figsize=(6, 6))
plt.imshow(Iprim, cmap='gray')
plt.title("Edge Detection using Laplace of Gaussian (LoG)")
plt.axis('off')
plt.show()