# Import library yang diperlukan
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

# Tentukan path gambar
image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'

# Baca gambar
img = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Dapatkan ukuran gambar
N, M, L = img_rgb.shape

# Inisialisasi matriks HSL Edge
HSL_Edge = np.ones((300, 300, 3), dtype=np.uint8) * 128

# Loop untuk setiap piksel dalam gambar
for n in range(N):
    for m in range(M):
        r, g, b = img_rgb[n, m]
        
        # Hitung Max, Min, C, L
        Max = max(r, g, b)
        Min = min(r, g, b)
        C = Max - Min
        L = (Max + Min) / 2.0
        
        # Hitung Saturation (S)
        S = 0 if Max == Min else C / (2 * L / 255) if L >= 127 else C / (2 - (2 * L / 255))
        
        # Hitung Hue (H)
        if C == 0:
            H = 0
        elif r == Max:
            H = (g - b) / C
        elif g == Max:
            H = 2 + (b - r) / C
        else:
            H = 4 + (r - g) / C
        H = H * np.pi / 3  # Konversi ke radian
        
        # Proyeksi ke koordinat 2D
        j = 150 + int((S / 2) * np.cos(H))
        i = 285 - int((S / 2) * np.sin(H) / 8.0 + L)
        
        # Pastikan koordinat berada dalam batas matriks
        if 0 <= i < 300 and 0 <= j < 300:
            HSL_Edge[i, j] = [r, g, b]

# Loop untuk warna RGB (kondisi edge)
for b in range(256):
    for g in range(256):
        for r in range(256):
            # Hitung Max, Min, C, L
            Max = max(r, g, b)
            Min = min(r, g, b)
            C = Max - Min
            L = (Max + Min) / 2.0
            
            # Hitung Saturation (S)
            S = 0 if Max == Min else C / (2 * L / 255) if L >= 127 else C / (2 - (2 * L / 255))
            
            # Hitung Hue (H)
            if C == 0:
                H = 0
            elif r == Max:
                H = (g - b) / C
            elif g == Max:
                H = 2 + (b - r) / C
            else:
                H = 4 + (r - g) / C
            H = H * np.pi / 3  # Konversi ke radian
            
            # Proyeksi ke koordinat 2D
            j = 150 + int((S / 2) * np.cos(H))
            i = 285 - int((S / 2) * np.sin(H) / 8.0 + L)
            
            # Kondisi untuk menentukan nilai edge
            if ((r == b and g == 255) or (r == g and b == 255) or (b == g and r == 255) or
                (r == 255 and g == 255) or (g == 255 and b == 255) or (b == 255 and r == 255) or
                (b == 0 and g == 0) or (r == 0 and g == 0) or (b == 0 and r == 0) or
                (b == r and g == 0) or (r == g and b == 0) or (b == g and r == 0) or
                (b == 255 and r == 0) or (b == 255 and g == 0) or (g == 255 and r == 0) or
                (g == 255 and b == 0) or (r == 255 and b == 0) or (r == 255 and g == 0) or
                (r == g and g == b)):
                if 0 <= i < 300 and 0 <= j < 300:
                    HSL_Edge[i, j] = [r, g, b]

# Tampilkan gambar hasil distribusi warna HSL Edge
plt.figure()
plt.imshow(HSL_Edge)
plt.title("Distribusi Warna HSL Edge")
plt.axis('off')
plt.show()