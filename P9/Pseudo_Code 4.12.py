# Pseudo code 4.12 - Edge Detection using Recursive Filter
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
file_path = 'P7/Data Image/Noisegray50%Gaussian.png'
I = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
I = I.astype(float)
N, M = I.shape # Get the size of the image

# Input the alpha and beta values
alpha = float(input('Masukkan nilai alpha: '))
beta = float(input('Masukkan nilai beta: '))

# Calculate filter coefficients
K1a = (1 + (1 + 2 * np.cos(alpha * beta)) * (np.exp(-2 * alpha) - np.exp(-alpha)) - np.exp(-3 * alpha))
K1b = (1 - np.cos(alpha * beta)) * (np.exp(-alpha) + np.exp(-2 * alpha)) + (((1 - beta**2) / (2 * beta)) * np.sin(alpha * beta)) * (np.exp(-alpha) - np.exp(-2 * alpha))
K1 = K1a / K1b

c0 = K1 * np.exp(-alpha) * (1 - np.cos(alpha * beta) + (((1 - beta**2) / (2 * beta)) * np.sin(alpha * beta)))
c1 = K1 * np.exp(-2 * alpha) * (1 - np.cos(alpha * beta) - (((1 - beta**2) / (2 * beta)) * np.sin(alpha * beta)))
b1 = -np.exp(-alpha) * (1 + 2 * np.cos(alpha * beta))
b2 = np.exp(-2 * alpha) * (1 + 2 * np.cos(alpha * beta))
b3 = -np.exp(-3 * alpha)

K2 = K1a / (0.5 + (1.5 - 2 * np.cos(alpha * beta)) * (np.exp(-alpha) + np.exp(-2 * alpha)) + np.sin(alpha * beta) * (np.exp(-alpha) - np.exp(-2 * alpha)) / beta + 0.5 * np.exp(-3 * alpha))
a0 = 0.5 * K2
a1 = K2 * np.exp(-alpha) * (0.5 - 1.5 * np.cos(alpha * beta) + 0.5 * np.sin(alpha * beta) / beta)
a2 = K2 * np.exp(-2 * alpha) * (1 - 0.5 * np.cos(alpha * beta) - 0.5 * np.sin(alpha * beta) / beta)
a3 = K2 * np.exp(-alpha) * (1 - 0.5 * np.cos(alpha * beta) + 0.5 * np.sin(alpha * beta) / beta)
a4 = K2 * np.exp(-2 * alpha) * (0.5 - 1.5 * np.cos(alpha * beta) - 0.5 * np.sin(alpha * beta) / beta)
a5 = 0.5 * K2 * np.exp(-3 * alpha)

# Initialize arrays for filtering
yp = np.zeros((N, M))
yn = np.zeros((N, M))

# Horizontal filtering
for i in range(N):
    yp[i, 0] = a0 * I[i, 0]
    yp[i, 1] = a0 * I[i, 1] + a1 * I[i, 0] - b1 * yp[i, 0]
    yp[i, 2] = a0 * I[i, 2] + a1 * I[i, 1] + a2 * I[i, 0] - b1 * yp[i, 1] - b2 * yp[i, 0]
    yn[i, M-1] = 0
    yn[i, M-2] = a3 * I[i, M-1]
    yn[i, M-3] = a3 * I[i, M-2] + a4 * I[i, M-1] - b1 * yn[i, M-1]
    yn[i, M-4] = a3 * I[i, M-3] + a4 * I[i, M-2] + a5 * I[i, M-1] - b1 * yn[i, M-2] - b2 * yn[i, M-1]
    
    for j in range(3, M-3):
        yp[i, j] = a0 * I[i, j] + a1 * I[i, j-1] + a2 * I[i, j-2] - b1 * yp[i, j-1] - b2 * yp[i, j-2] - b3 * yp[i, j-3]
        yn[i, M-j-1] = a3 * I[i, M-j] + a4 * I[i, M-j+1] + a5 * I[i, M-j+2] - b1 * yn[i, M-j] - b2 * yn[i, M-j+1] - b3 * yn[i, M-j+2]

Yx = yp + yn

# Vertical filtering
for j in range(M):
    yp[0, j] = a0 * I[0, j]
    yp[1, j] = a0 * I[1, j] + a1 * I[0, j] - b1 * yp[0, j]
    yp[2, j] = a0 * I[2, j] + a1 * I[1, j] + a2 * I[0, j] - b1 * yp[1, j] - b2 * yp[0, j]
    yn[N-1, j] = 0
    yn[N-2, j] = a3 * I[N-1, j]
    yn[N-3, j] = a3 * I[N-2, j] + a4 * I[N-1, j] - b1 * yn[N-1, j]
    yn[N-4, j] = a3 * I[N-3, j] + a4 * I[N-2, j] + a5 * I[N-1, j] - b1 * yn[N-2, j] - b2 * yn[N-1, j]
    
    for i in range(3, N-3):
        yp[i, j] = a0 * I[i, j] + a1 * I[i-1, j] + a2 * I[i-2, j] - b1 * yp[i-1, j] - b2 * yp[i-2, j] - b3 * yp[i-3, j]
        yn[N-i-1, j] = a3 * I[N-i, j] + a4 * I[N-i+1, j] + a5 * I[N-i+2, j] - b1 * yn[N-i, j] - b2 * yn[N-i+1, j] - b3 * yn[N-i+2, j]

Yy = yp + yn

# Combine horizontal and vertical edges
Y = Yx + Yy

# Display the original and edge-detected images
plt.figure(figsize=(6, 6))
plt.imshow(I, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.show()

plt.figure(figsize=(6, 6))
plt.imshow(Y, cmap='gray')
plt.title("Edge Detected Image")
plt.axis('off')
plt.show()