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

# Inisialisasi matriks HCL Edge
HCL_Edge = np.ones((225, 400, 3), dtype=np.uint8) * 128
gamma = 10

# Loop untuk setiap piksel dalam gambar
for n in range(N):
    for m in range(M):
        r, g, b = img_rgb[n, m]
        
        # Hitung Max, Min, Q
        Max = max(r, g, b)
        Min = min(r, g, b)
        Q = 1.0 if Max == 0 else np.exp((Min * gamma) / (Max * 100.0))
        
        # Hitung nilai L, C, dan H
        L = (Q * Max + (Q - 1.0) * Min) / 2.0
        rg = r - g
        gb = g - b
        C = (abs(b - r) + abs(rg) + abs(gb)) * Q / 3.0
        H = np.arctan2(gb, rg)
        
        # Kondisi untuk nilai H
        if C == 0:
            H = 0.0
        elif rg >= 0 and gb >= 0:
            H = 2 * H / 3
        elif rg >= 0 and gb < 0:
            H = 4 * H / 3
        elif rg < 0 and gb >= 0:
            H = np.pi + 4 * H / 3
        else:
            H = 2 * H / 3 - np.pi
        
        # Proyeksi ke koordinat 2D
        j = 200 + int(round(C * np.cos(H)))
        i = 200 - int(round(C * np.sin(H) / 4.0 + L))
        
        # Pastikan koordinat berada dalam batas matriks
        if 0 <= i < 225 and 0 <= j < 400:
            HCL_Edge[i, j] = [r, g, b]

# Loop untuk kondisi edge
for b in range(256):
    for g in range(256):
        for r in range(256):
            # Kondisi untuk menentukan nilai edge
            if ((r == b and g == 255) or (r == g and b == 255) or (b == g and r == 255) or
                (r == 255 and g == 255) or (g == 255 and b == 255) or (b == 255 and r == 255) or
                (b == 0 and g == 0) or (r == 0 and g == 0) or (b == 0 and r == 0) or
                (b == r and g == 0) or (r == g and b == 0) or (b == g and r == 0) or
                (b == 255 and r == 0) or (b == 255 and g == 0) or (g == 255 and r == 0) or
                (g == 255 and b == 0) or (r == 255 and b == 0) or (r == 255 and g == 0) or
                (r == g and g == b) or (H == np.pi / 18) or (H == -np.pi / 18)):
                
                Max = max(r, g, b)
                Min = min(r, g, b)
                Q = 1.0 if Max == 0 else np.exp((Min * gamma) / (Max * 100.0))
                
                # Hitung nilai L, C, dan H
                L = (Q * Max + (Q - 1.0) * Min) / 2.0
                rg = r - g
                gb = g - b
                C = (abs(b - r) + abs(rg) + abs(gb)) * Q / 3.0
                H = np.arctan2(gb, rg)
                
                # Kondisi untuk nilai H
                if C == 0:
                    H = 0.0
                elif rg >= 0 and gb >= 0:
                    H = 2 * H / 3
                elif rg >= 0 and gb < 0:
                    H = 4 * H / 3
                elif rg < 0 and gb >= 0:
                    H = np.pi + 4 * H / 3
                else:
                    H = 2 * H / 3 - np.pi
                
                # Proyeksi ke koordinat 2D
                j = 200 + int(round(C * np.cos(H)))
                i = 200 - int(round(C * np.sin(H) / 4.0 + L))
                
                # Pastikan koordinat berada dalam batas matriks
                if 0 <= i < 225 and 0 <= j < 400:
                    HCL_Edge[i, j] = [r, g, b]

# Tampilkan gambar hasil distribusi warna HCL Edge
plt.figure()
plt.imshow(HCL_Edge)
plt.title("Distribusi Warna HCL Edge")
plt.axis('off')
plt.show()