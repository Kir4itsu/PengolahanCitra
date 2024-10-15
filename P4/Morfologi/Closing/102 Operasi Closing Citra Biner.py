import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import closing, square

# Path file gambar di sistem lokal
image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'

# Membaca citra grayscale
f = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if f is not None:
    # Konversi citra ke biner
    _, f = cv2.threshold(f, 128, 1, cv2.THRESH_BINARY)

    # Set ukuran kernel K dan matriks B untuk dilasi dan erosi
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

    # Proses dilasi manual
    Citra_dilasi = np.zeros((N, M), dtype=np.uint8)
    for n in range(I, N - I):
        for m in range(J, M - J):
            dilasi = 0
            for i in range(-I, I + 1):
                for j in range(-J, J + 1):
                    bit_dilasi = B[I + i, J + j] & f[n + i, m + j]
                    dilasi = dilasi | bit_dilasi
            Citra_dilasi[n, m] = dilasi

    # Proses erosi manual pada hasil dilasi
    Citra_closing = np.ones((N, M), dtype=np.uint8)
    for n in range(I, N - I):
        for m in range(J, M - J):
            erosi = 1
            for i in range(-I, I + 1):
                for j in range(-J, J + 1):
                    bit_erosi = B[I + i, J + j] & Citra_dilasi[n + i, m + j]
                    erosi = erosi & bit_erosi
            Citra_closing[n, m] = erosi

    # Tampilkan hasil closing manual
    plt.figure(2)
    plt.imshow(Citra_closing, cmap='gray')
    plt.title("Hasil Closing Manual")
    plt.axis('off')

    # Closing menggunakan fungsi dari skimage
    Citra_closing1 = closing(f, square(K))

    # Tampilkan hasil closing dengan fungsi skimage
    plt.figure(3)
    plt.imshow(Citra_closing1, cmap='gray')
    plt.title("Hasil Closing dengan Skimage")
    plt.axis('off')

    # Tampilkan semua plot
    plt.show()
else:
    print("Gagal membaca citra dari path yang diberikan.")
