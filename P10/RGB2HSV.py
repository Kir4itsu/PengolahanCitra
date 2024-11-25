import numpy as np
import cv2
import matplotlib.pyplot as plt

def rgb_to_hsv(RGB):
    M, N, L = RGB.shape
    HSV = np.zeros((M, N, L), dtype=np.float32)

    for m in range(M):
        for n in range(N):
            r, g, b = RGB[m, n, :] / 255.0
            Max, Min = max(r, g, b), min(r, g, b)
            C = Max - Min

            V = Max
            S = 0 if Max == 0 else C / Max

            if C == 0:
                H = 0
            else:
                if r == Max:
                    H = (g - b) / C
                elif g == Max:
                    H = 2 + (b - r) / C
                elif b == Max:
                    H = 4 + (r - g) / C
                H = H * np.pi / 3

            if H < 0:
                H += 2 * np.pi

            HSV[m, n, :] = [H, S, V]

    return HSV

# Test fungsi dengan gambar RGB
image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'
RGB = cv2.imread(image_path)
if RGB is None:
    print("Error: Gambar tidak ditemukan atau gagal dibaca.")
else:
    RGB = cv2.cvtColor(RGB, cv2.COLOR_BGR2RGB)

    # Konversi ke HSV
    HSV = rgb_to_hsv(RGB)

    # Tampilkan gambar asli dan channel HSV
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 4, 1)
    plt.imshow(RGB)
    plt.title('Original RGB Image')
    plt.axis('off')

    plt.subplot(1, 4, 2)
    plt.imshow(HSV[:, :, 0], cmap='hsv')
    plt.title('Hue Channel')
    plt.axis('off')

    plt.subplot(1, 4, 3)
    plt.imshow(HSV[:, :, 1], cmap='gray')
    plt.title('Saturation Channel')
    plt.axis('off')

    plt.subplot(1, 4, 4)
    plt.imshow(HSV[:, :, 2], cmap='gray')
    plt.title('Value Channel')
    plt.axis('off')

    plt.show()
