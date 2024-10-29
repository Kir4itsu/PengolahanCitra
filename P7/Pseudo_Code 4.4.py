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

# Kirsch operators
G1 = np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]])
G2 = np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]])
G3 = np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]])
G4 = np.array([[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]])
G5 = np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]])
G6 = np.array([[-3, -3, -3], [5, 0, -3], [5, 5, -3]])
G7 = np.array([[5, -3, -3], [5, 0, -3], [5, -3, -3]])
G8 = np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]])

# Apply Kirsch operators using convolution
Gs1 = np.abs(convolve(Im, G1)) / 15
Gs2 = np.abs(convolve(Im, G2)) / 15
Gs3 = np.abs(convolve(Im, G3)) / 15
Gs4 = np.abs(convolve(Im, G4)) / 15
Gs5 = np.abs(convolve(Im, G5)) / 15
Gs6 = np.abs(convolve(Im, G6)) / 15
Gs7 = np.abs(convolve(Im, G7)) / 15
Gs8 = np.abs(convolve(Im, G8)) / 15

# Compute the maximum gradient at each pixel
GS = np.maximum.reduce([Gs1, Gs2, Gs3, Gs4, Gs5, Gs6, Gs7, Gs8])

# Display the result
plt.figure(figsize=(6, 6))
plt.imshow(GS, cmap='gray')
plt.title("Kirsch Gradient")
plt.axis('off')
plt.show()
