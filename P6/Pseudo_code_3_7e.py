import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

# Alamat file input dan output
input_image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'
output_image_path = r'C:\Users\Administrator\Pictures\LCH_image1.jpg'

# Pastikan file gambar ada di folder tersebut
if not os.path.exists(input_image_path):
    print("File gambar tidak ditemukan.")
else:
    print("File gambar ditemukan")
    # Baca gambar
    img = cv2.imread(input_image_path)
    # Konversi BGR ke RGB untuk konsistensi dengan matplotlib
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Tampilkan gambar asli
plt.figure(1)
plt.imshow(img_rgb)
plt.title("Gambar Asli")
plt.axis('off')

# Dapatkan ukuran gambar
N, M, L = img_rgb.shape

# Inisialisasi matriks LCH Edge
LCH_Edge = np.ones((300, 300, 3), dtype=np.uint8) * 128

# Threshold dan matriks konversi
Th = 0.00885645
MAT = np.array([[0.412453, 0.357580, 0.180423],
                [0.212671, 0.715160, 0.072169],
                [0.019334, 0.119193, 0.950227]])

# Loop untuk setiap piksel dalam gambar
for n in range(N):
    for m in range(M):
        # Baca komponen R, G, B dan hitung nilai dalam ruang XYZ
        r, g, b = img_rgb[n, m, 0] / 255, img_rgb[n, m, 1] / 255, img_rgb[n, m, 2] / 255
        RGB = np.array([r, g, b])
        XYZ = MAT @ RGB

        # Normalisasi dan threshold
        X = max(XYZ[0] / 0.950456, 1e-6)  # Hindari nilai negatif atau nol
        Y = max(XYZ[1], 1e-6)
        Z = max(XYZ[2] / 1.088754, 1e-6)
        XT, YT, ZT = X > Th, Y > Th, Z > Th

        # Fungsi f(t)
        fX = np.where(XT, X**(1/3), 7.787 * X + 16/116)
        fY = np.where(YT, Y**(1/3), 7.787 * Y + 16/116)
        fZ = np.where(ZT, Z**(1/3), 7.787 * Z + 16/116)

        # Hitung L, a, b, C, dan H
        L = 116 * fY - 16
        a = 500 * (fX - fY)
        b = 200 * (fY - fZ)
        C = np.sqrt(a**2 + b**2)
        H = np.arctan2(b, a)

        # Proyeksi ke koordinat 2D
        j = 125 + int(round(C * np.cos(H)))
        i = 200 - int(round(C * np.sin(H) + L))

        # Pastikan koordinat berada dalam batas matriks
        if 0 <= i < 300 and 0 <= j < 300:
            LCH_Edge[i, j] = img_rgb[n, m]

# Loop untuk kondisi edge
for b in range(256):
    for g in range(256):
        for r in range(256):
            RGB = np.array([r / 255, g / 255, b / 255])
            XYZ = MAT @ RGB
            X, Y, Z = max(XYZ[0] / 0.950456, 1e-6), max(XYZ[1], 1e-6), max(XYZ[2] / 1.088754, 1e-6)
            XT, YT, ZT = X > Th, Y > Th, Z > Th

            # Fungsi f(t)
            fX = np.where(XT, X**(1/3), 7.787 * X + 16/116)
            fY = np.where(YT, Y**(1/3), 7.787 * Y + 16/116)
            fZ = np.where(ZT, Z**(1/3), 7.787 * Z + 16/116)

            # Hitung L, a, b, C, dan H
            L = 116 * fY - 16
            a = 500 * (fX - fY)
            b = 200 * (fY - fZ)
            C = np.sqrt(a**2 + b**2)
            H = np.arctan2(b, a)

            # Proyeksi ke koordinat 2D
            j = 125 + int(round(C * np.cos(H)))
            i = 200 - int(round(C * np.sin(H) + L))

            # Kondisi untuk menentukan nilai edge
            if ((r == b and g == 255) or (r == g and b == 255) or (b == g and r == 255) or
                (r == 255 and g == 255) or (g == 255 and b == 255) or (b == 255 and r == 255) or
                (b == 0 and g == 0) or (r == 0 and g == 0) or (b == 0 and r == 0) or
                (b == r and g == 0) or (r == g and b == 0) or (b == g and r == 0) or
                (b == 255 and r == 0) or (b == 255 and g == 0) or (g == 255 and r == 0) or
                (g == 255 and b == 0) or (r == 255 and b == 0) or (r == 255 and g == 0) or
                (r == g and g == b)):
                if 0 <= i < 300 and 0 <= j < 300:
                    LCH_Edge[i, j] = [r, g, b]

# Tampilkan gambar hasil distribusi warna LCH Edge
plt.figure(2)
plt.imshow(LCH_Edge)
plt.title("Distribusi Warna LCH Edge")
plt.axis('off')

# Simpan hasil gambar
cv2.imwrite(output_image_path, cv2.cvtColor(LCH_Edge, cv2.COLOR_RGB2BGR))

plt.show()
