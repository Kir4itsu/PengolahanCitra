import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

file_path = 'P7/Data Image/Noisegray50%Gaussian.png'

# Read the image
I = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
I = I.astype(float)

# Input the standard deviation (sigma1 and sigma2)
s1 = float(input('Masukkan nilai standar deviasi 1 (sigma1): '))
s2 = float(input('Masukkan nilai standar deviasi 2 (sigma2): '))

# Calculate Gaussian filter coefficients
A1 = (1 / (2 * np.pi * s1**2))
A2 = (1 / (2 * np.pi * s2**2))
C1 = (2 * s1**2)
C2 = (2 * s2**2)

# Initialize Gaussian kernels
G1 = np.zeros((9, 9))
G2 = np.zeros((9, 9))

# Compute the Gaussian kernels
for i in range(9):
    for j in range(9):
        G1[i, j] = A1 * np.exp(-((i - 4)**2 + (j - 4)**2) / C1)
        G2[i, j] = A2 * np.exp(-((i - 4)**2 + (j - 4)**2) / C2)

# Apply the Gaussian filters using convolution
Idog1 = convolve(I, G1)  # I * G1
Idog2 = convolve(I, G2)  # I * G2
Idog = np.abs(Idog1 - Idog2)  # |I * G1 - I * G2|

# Display results
plt.figure(figsize=(6, 6))
plt.imshow(I, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.show()

plt.figure(figsize=(6, 6))
plt.imshow(Idog, cmap='gray')
plt.title("Edge Detection using Difference of Gaussian (DoG)")
plt.axis('off')
plt.show()