import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'

# Membaca citra
I = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if I is not None:
    # Tampilkan citra asli
    plt.figure(1)
    plt.imshow(I, cmap='gray')
    plt.title("Citra Grayscale Asli")
    plt.axis('off')

    # Menghitung histogram
    Histo = cv2.calcHist([I], [0], None, [256], [0, 256]).flatten()

    # Mendapatkan ukuran citra
    N, M = I.shape

    # Menghitung histogram kumulatif
    Hist_kum = np.zeros_like(Histo)
    Hist_kum[0] = Histo[0]
    for l in range(1, len(Histo)):
        Hist_kum[l] = Histo[l] + Hist_kum[l-1]

    # Normalisasi histogram kumulatif
    Hist_kum = Hist_kum / (N * M)

    # Histogram equalization manual
    Im_equal = np.zeros_like(I)
    for n in range(N):
        for m in range(M):
            Im_equal[n, m] = round(Hist_kum[I[n, m]] * 255)

    # Tampilkan hasil citra equalization manual
    plt.figure(2)
    plt.imshow(Im_equal, cmap='gray')
    plt.title("Citra Equalization Manual")
    plt.axis('off')

    # Histogram equalization menggunakan OpenCV
    I_equal = cv2.equalizeHist(I)

    # Tampilkan hasil citra equalization dengan OpenCV
    plt.figure(3)
    plt.imshow(I_equal, cmap='gray')
    plt.title("Citra Equalization dengan OpenCV")
    plt.axis('off')

    # Tampilkan semua plot
    plt.show()
else:
    print("Gagal membaca citra dari jalur lokal.")
