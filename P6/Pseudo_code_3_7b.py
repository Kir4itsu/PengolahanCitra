import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

# Tentukan alamat file gambar
image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'

# Pastikan file gambar ada
if os.path.exists(image_path):
    print("File gambar ditemukan")
    # Baca gambar
    img = cv2.imread(image_path)
    # Konversi BGR ke RGB
    Img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Dapatkan ukuran citra
    N, M, L = Img.shape
    
    # Inisialisasi matriks tampilan dalam ruang RGB
    RGB_Citra = np.ones((425, 425, 3), dtype=np.uint8) * 128
    sudut = -5 * np.pi / 6
    
    # Loop untuk mengisi matriks tampilan dengan warna citra
    for n in range(N):
        for m in range(M):
            r = float(Img[n, m, 0])
            g = float(Img[n, m, 1])
            b = float(Img[n, m, 2])
            j = 150 + int(g + (b * np.sin(sudut)))
            i = 280 - int(b * np.sin(sudut) + r)
            if 0 <= i < 425 and 0 <= j < 425:
                RGB_Citra[i, j, 0] = r
                RGB_Citra[i, j, 1] = g
                RGB_Citra[i, j, 2] = b
    
    # Tampilkan distribusi warna citra dalam ruang RGB
    plt.figure(5)
    plt.imshow(RGB_Citra)
    plt.title("Distribusi Warna Citra dalam Ruang RGB")
    plt.axis('off')
    plt.show()
else:
    print("File gambar tidak ditemukan.")