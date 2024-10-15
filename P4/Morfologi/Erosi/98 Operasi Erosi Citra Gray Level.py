import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import erosion, square

# Path file gambar di komputer lokal
image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'

# Membaca citra grayscale
f = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if f is not None:
    # Tampilkan citra asli
    plt.figure(1)
    plt.imshow(f, cmap='gray')
    plt.title("Citra Grayscale Asli")
    plt.axis('off')

    # Struktur elemen untuk erosi (8 connectivity)
    B = np.ones((3, 3), dtype=np.uint8)

    # Ukuran elemen struktural dan citra
    N, M = f.shape
    I, J = B.shape
    I //= 2
    J //= 2

    # Proses erosi manual dengan operasi minimum
    Citra_erosi = np.full((N, M), 255, dtype=np.uint8)
    for n in range(I, N - I):
        for m in range(J, M - J):
            erosi = 255
            for i in range(-I, I + 1):
                for j in range(-J, J + 1):
                    erosi = min(B[I + i, J + j] * f[n + i, m + j], erosi)
            Citra_erosi[n, m] = erosi

    # Tampilkan hasil erosi manual
    plt.figure(2)
    plt.imshow(Citra_erosi, cmap='gray')
    plt.title("Hasil Erosi Manual")
    plt.axis('off')

    # Erosi menggunakan fungsi dari skimage
    Citra_erosi1 = erosion(f, square(3))

    # Tampilkan hasil erosi dengan fungsi skimage
    plt.figure(3)
    plt.imshow(Citra_erosi1, cmap='gray')
    plt.title("Hasil Erosi dengan Skimage")
    plt.axis('off')

    # Tampilkan semua plot
    plt.show()
else:
    print("Gagal membaca citra dari jalur lokal.")
