import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import erosion, square

 
image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'

# Membaca dan mengonversi citra menjadi citra biner
f = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if f is not None:
    # Konversi citra ke biner
    _, f = cv2.threshold(f, 128, 1, cv2.THRESH_BINARY)

    # Struktur elemen untuk erosi (8 connectivity)
    B = np.ones((3, 3), dtype=np.uint8)

    # Tampilkan citra biner asli
    plt.figure(1)
    plt.imshow(f, cmap='gray')
    plt.title("Citra Biner Asli")
    plt.axis('off')

    # Ukuran citra dan matriks B
    N, M = f.shape
    I, J = B.shape
    I //= 2
    J //= 2

    # Proses erosi manual
    Citra_erosi = np.ones((N, M), dtype=np.uint8)
    for n in range(I, N - I):
        for m in range(J, M - J):
            erosi = 1
            for i in range(-I, I + 1):
                for j in range(-J, J + 1):
                    bit_erosi = B[I + i, J + j] & f[n + i, m + j]
                    erosi = erosi & bit_erosi
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
