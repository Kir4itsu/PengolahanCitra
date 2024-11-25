import numpy as np
import cv2
import matplotlib.pyplot as plt

def rgb_to_hcl(RGB):
    M, N, L = RGB.shape
    HCL = np.zeros((M, N, L), dtype=np.float32)
    gamma = 30.0

    for m in range(M):
        for n in range(N):
            r, g, b = RGB[m, n, :] / 255.0
            Max, Min = max(r, g, b), min(r, g, b)

            if Max == 0:
                Q = 1.0
            else:
                Q = np.exp((Min * gamma) / (Max * 100.0))

            L = (Q * Max + (Q - 1.0) * Min) / 2.0
            C = (abs(b - r) + abs(r - g) + abs(g - b)) * Q / 3.0
            H = np.arctan2(g - b, r - g)

            if H < 0:
                H += 2 * np.pi

            HCL[m, n, :] = [H, C, L]

    return HCL

# Uji fungsi dengan gambar contoh
image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'
RGB = cv2.imread(image_path)
if RGB is None:
    print("Error: Gambar tidak ditemukan atau gagal dibaca.")
else:
    RGB = cv2.cvtColor(RGB, cv2.COLOR_BGR2RGB)
    HCL = rgb_to_hcl(RGB)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 3, 1)
    plt.imshow(RGB)
    plt.title('Original RGB Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(HCL[:, :, 0], cmap='hsv')
    plt.title('Hue Channel')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(HCL[:, :, 1], cmap='gray')
    plt.title('Chroma Channel')
    plt.axis('off')

    plt.show()
