import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import opening, square

# Path file gambar di sistem lokal
image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'

# Membaca citra grayscale
f = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if f is not None:
    # Konversi citra ke biner
    _, f = cv2.threshold(f, 128, 1, cv2.THRESH_BINARY)

    # Set ukuran kernel K dan matriks B untuk erosi dan dilasi
    K = 5
    B = np.ones((K, K), dtype=np.uint8)

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

    # Proses dilasi manual pada hasil erosi
    Citra_opening = np.zeros((N, M), dtype=np.uint8)
    for n in range(I, N - I):
        for m in range(J, M - J):
            dilasi = 0
            for i in range(-I, I + 1):
                for j in range(-J, J + 1):
                    bit_dilasi = B[I + i, J + j] & Citra_erosi[n + i, m + j]
                    dilasi = dilasi | bit_dilasi
            Citra_opening[n, m] = dilasi

    # Tampilkan hasil opening manual
    plt.figure(2)
    plt.imshow(Citra_opening, cmap='gray')
    plt.title("Hasil Opening Manual")
    plt.axis('off')

    # Opening menggunakan fungsi dari skimage
    Citra_opening1 = opening(f, square(K))

    # Tampilkan hasil opening dengan fungsi skimage
    plt.figure(3)
    plt.imshow(Citra_opening1, cmap='gray')
    plt.title("Hasil Opening dengan Skimage")
    plt.axis('off')

    # Tampilkan semua plot
    plt.show()
else:
    print("Gagal membaca citra dari path yang diberikan.")
