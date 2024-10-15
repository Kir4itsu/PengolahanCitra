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

    # Mendapatkan ukuran citra
    N, M = I.shape

    # Menghitung histogram secara manual
    Histo = np.zeros(256)
    for n in range(N):
        for m in range(M):
            Histo[I[n, m]] += 1

    # Plot histogram manual
    plt.figure(2)
    plt.plot(Histo)
    plt.title("Histogram Manual")
    plt.xlabel("Intensitas")
    plt.ylabel("Frekuensi")

    # Menghitung histogram menggunakan OpenCV
    Histo1 = cv2.calcHist([I], [0], None, [256], [0, 256])

    # Plot histogram menggunakan OpenCV
    plt.figure(3)
    plt.plot(Histo1)
    plt.title("Histogram Menggunakan OpenCV")
    plt.xlabel("Intensitas")
    plt.ylabel("Frekuensi")

    # Tampilkan semua plot
    plt.show()
else:
    print("Gagal membaca citra dari jalur lokal.")
