import cv2
import numpy as np
import matplotlib.pyplot as plt

file_path = 'P7/Data Image/Noisegray50%Gaussian.png'

# Read the image
I = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
I = I.astype(float)
N, M = I.shape

# Input the alpha value
alpha = float(input('Masukkan nilai alpha: '))

# Calculate filter coefficients
K = (1 - np.exp(-alpha))**2 / (1 + 2 * alpha * np.exp(-alpha) - np.exp(-2 * alpha))
C = (1 - np.exp(-alpha))**2 / np.exp(-alpha)
a0 = K
a1 = K * (alpha - 1) * np.exp(-alpha)
a2 = K * (alpha + 1) * np.exp(-alpha)
a3 = -K * np.exp(-2 * alpha)
b1 = -2 * np.exp(-alpha)
b2 = np.exp(-2 * alpha)
c1 = C * np.exp(-alpha)

# Initialize arrays for filtering
yp = np.zeros((N, M))
yn = np.zeros((N, M))

# Horizontal filtering
for i in range(N):
    yp[i, 0] = a0 * I[i, 0]
    yp[i, 1] = a0 * I[i, 1] + a1 * I[i, 0] - b1 * yp[i, 0]
    yn[i, M-1] = 0
    yn[i, M-2] = a2 * I[i, M-1] - b1 * yn[i, M-1]
    yn[i, M-3] = a2 * I[i, M-2] + a3 * I[i, M-1] - b1 * yn[i, M-2] - b2 * yn[i, M-1]
    
    for j in range(2, M-2):
        yp[i, j] = a0 * I[i, j] + a1 * I[i, j-1] - b1 * yp[i, j-1] - b2 * yp[i, j-2]
        yn[i, M-j-1] = a2 * I[i, M-j] + a3 * I[i, M-j+1] - b1 * yn[i, M-j] - b2 * yn[i, M-j+1]
    
    yp[i, M-1] = a0 * I[i, M-1] + a1 * I[i, M-2] - b1 * yp[i, M-2] - b2 * yp[i, M-3]

Yx = yp + yn

# Vertical filtering
for j in range(M):
    yp[0, j] = a0 * I[0, j]
    yp[1, j] = a0 * I[1, j] + a1 * I[0, j] - b1 * yp[0, j]
    yn[N-1, j] = 0
    yn[N-2, j] = a2 * I[N-1, j] - b1 * yn[N-1, j]
    yn[N-3, j] = a2 * I[N-2, j] + a3 * I[N-1, j] - b1 * yn[N-2, j] - b2 * yn[N-1, j]
    
    for i in range(2, N-2):
        yp[i, j] = a0 * I[i, j] + a1 * I[i-1, j] - b1 * yp[i-1, j] - b2 * yp[i-2, j]
        yn[N-i-1, j] = a2 * I[N-i, j] + a3 * I[N-i+1, j] - b1 * yn[N-i, j] - b2 * yn[N-i+1, j]

Yy = yp + yn

# Combine horizontal and vertical edges
Y = Yx + Yy

# Display results
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