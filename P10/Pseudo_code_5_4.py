import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'
I = cv2.imread(image_path)

if I is None:
    print("Error: Gambar tidak ditemukan atau gagal dibaca.")
else:
    I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
    I1 = I.copy()
    N, M, L = I.shape

    # RGB segmentation
    Q = 4  # Quantization level
    Th = 255 / Q  # Threshold for quantization
    RGBidx = np.round(I / Th).astype(int)
    RGBpeta = np.round(RGBidx * Th).astype(np.uint8)

    # Display the original and RGB segmented image
    plt.figure(1)
    plt.imshow(I)
    plt.title('Citra Asli')
    plt.axis('off')

    plt.figure(2)
    plt.imshow(RGBpeta)
    plt.title('Peta Warna Citra (RGB)')
    plt.axis('off')

    # Cari batas antara dua warna arah x
    for n in range(N):
        for m in range(M - 1):
            diff = np.sqrt(np.sum((RGBidx[n, m] - RGBidx[n, m + 1]) ** 2))
            if diff > 0:
                I[n, m, :] = [255, 255, 255]

    # Cari batas antara dua warna arah y
    for n in range(N - 1):
        for m in range(M):
            diff = np.sqrt(np.sum((RGBidx[n, m] - RGBidx[n + 1, m]) ** 2))
            if diff > 0:
                I[n, m, :] = [255, 255, 255]

    # Display the segmented image result (RGB)
    plt.figure(3)
    plt.imshow(I.astype(np.uint8))
    plt.title('Citra Hasil Segmentasi (RGB)')
    plt.axis('off')

    # HSV segmentation
    HSV = cv2.cvtColor(I1, cv2.COLOR_RGB2HSV)
    HSVidx = np.zeros_like(HSV, dtype=float)
    HSVidx[:, :, 0] = np.round(HSV[:, :, 0] / (360 / Q)) * (360 / Q)
    HSVidx[:, :, 1:] = np.round(HSV[:, :, 1:] / Th) * Th

    plt.figure(4)
    plt.imshow(HSVidx.astype(np.uint8))
    plt.title('Peta Warna Citra (HSV)')
    plt.axis('off')

    plt.show()
