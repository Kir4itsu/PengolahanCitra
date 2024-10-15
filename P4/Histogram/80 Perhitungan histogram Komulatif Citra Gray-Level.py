import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'

# Membaca citra
I = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if I is not None:
    # Tampilkan citra
    plt.figure(1)
    plt.imshow(I, cmap='gray')
    plt.title("Citra Grayscale")
    plt.axis('off')

    # Menghitung histogram menggunakan OpenCV
    Histo = cv2.calcHist([I], [0], None, [256], [0, 256]).flatten()

    # Plot histogram
    plt.figure(2)
    plt.plot(Histo)
    plt.title("Histogram Intensitas")
    plt.xlabel("Intensitas")
    plt.ylabel("Frekuensi")

    # Mendapatkan ukuran citra
    N, M = I.shape

    # Menghitung histogram kumulatif
    Hist_kum = np.zeros_like(Histo)
    Hist_kum[0] = Histo[0]
    for l in range(1, len(Histo)):
        Hist_kum[l] = Histo[l] + Hist_kum[l-1]

    # Normalisasi histogram kumulatif
    Hist_kum = Hist_kum / (N * M)

    # Plot histogram kumulatif
    plt.figure(3)
    plt.plot(Hist_kum)
    plt.title("Histogram Kumulatif")
    plt.xlabel("Intensitas")
    plt.ylabel("Frekuensi Kumulatif Ternormalisasi")

    # Tampilkan semua plot
    plt.show()
else:
    print("Gagal membaca citra dari jalur lokal.")
