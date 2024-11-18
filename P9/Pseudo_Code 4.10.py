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
b1 = -np.exp(-alpha)
a1 = (1 + b1) / (1 - b1)
c1 = (1 + b1)

# Horizontal filtering
yp = np.zeros((N, M))
yn = np.zeros((N, M))

for i in range(N):
    yp[i, 0] = a1 * I[i, 0]
    yn[i, M-1] = a1 * I[i, M-1]
    yn[i, M-2] = a1 * I[i, M-2] - b1 * yn[i, M-1]
    
    for j in range(1, M-1):
        yp[i, j] = a1 * I[i, j] - b1 * yp[i, j-1]
        yn[i, M-j-1] = a1 * I[i, M-j] - b1 * yn[i, M-j]
    
    yp[i, M-1] = a1 * I[i, M-1] - b1 * yp[i, M-2]

Yx = yp + yn

# Vertical filtering
yp = np.zeros((N, M))
yn = np.zeros((N, M))

for j in range(M):
    yp[0, j] = a1 * I[0, j]
    yn[N-1, j] = a1 * I[N-1, j]
    yn[N-2, j] = a1 * I[N-2, j] - b1 * yn[N-1, j]
    
    for i in range(1, N-1):
        yp[i, j] = a1 * I[i, j] - b1 * yp[i-1, j]
        yn[N-i-1, j] = a1 * I[N-i, j] - b1 * yn[N-i, j]
    
    yp[N-1, j] = a1 * I[N-1, j] - b1 * yp[N-2, j]

Yy = np.abs(yp + yn)

# Edge detection in vertical direction
for j in range(M):
    yp[0, j] = c1 * Yx[0, j]
    yn[N-1, j] = -c1 * Yx[N-1, j]
    yn[N-2, j] = -c1 * Yx[N-2, j] - b1 * yn[N-1, j]
    
    for i in range(1, N-1):
        yp[i, j] = c1 * Yx[i-1, j] - b1 * yp[i-1, j]
        yn[N-i-1, j] = -c1 * Yx[N-i, j] - b1 * yn[N-i, j]
    
    yp[N-1, j] = c1 * Yx[N-1, j] - b1 * yp[N-2, j]

Yx = np.abs(yp + yn)

# Edge detection in horizontal direction
for i in range(N):
    yp[i, 0] = c1 * Yy[i, 0]
    yn[i, M-1] = -c1 * Yy[i, M-1]
    yn[i, M-2] = -c1 * Yy[i, M-2] - b1 * yn[i, M-1]
    
    for j in range(1, M-1):
        yp[i, j] = c1 * Yy[i, j-1] - b1 * yp[i, j-1]
        yn[i, M-j-1] = -c1 * Yy[i, M-j] - b1 * yn[i, M-j]
    
    yp[i, M-1] = c1 * Yy[i, M-1] - b1 * yp[i, M-2]

Yy = np.abs(yp + yn)

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