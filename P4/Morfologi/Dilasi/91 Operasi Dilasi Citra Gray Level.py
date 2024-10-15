import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import dilation, square

image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'

# Membaca citra grayscale
f = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if f is not None:
    # Tampilkan citra asli
    plt.figure(1)
    plt.imshow(f, cmap='gray')
    plt.title("Citra Grayscale Asli")
    plt.axis('off')

    # Struktur elemen untuk dilasi (8 connectivity)
    B = np.ones((3, 3), dtype=np.uint8)

    # Ukuran elemen struktural dan citra
    N, M = f.shape
    I, J = B.shape
    I //= 2
    J //= 2

    # Proses dilasi manual dengan operasi maksimal
    Citra_dilasi = np.zeros((N, M), dtype=np.uint8)
    for n in range(I, N - I):
        for m in range(J, M - J):
            dilasi = 0
            for i in range(-I, I + 1):
                for j in range(-J, J + 1):
                    dilasi = max(B[I + i, J + j] * f[n + i, m + j], dilasi)
            Citra_dilasi[n, m] = dilasi

    # Tampilkan hasil dilasi manual
    plt.figure(2)
    plt.imshow(Citra_dilasi, cmap='gray')
    plt.title("Hasil Dilasi Manual")
    plt.axis('off')

    # Dilasi menggunakan fungsi dari skimage
    Citra_dilasi1 = dilation(f, square(3))

    # Tampilkan hasil dilasi dengan fungsi skimage
    plt.figure(3)
    plt.imshow(Citra_dilasi1, cmap='gray')
    plt.title("Hasil Dilasi dengan Skimage")
    plt.axis('off')

    # Tampilkan semua plot
    plt.show()
else:
    print("Gagal membaca citra dari jalur lokal.")
