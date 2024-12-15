import cv2
import numpy as np
from math import sqrt, cos, pi
import matplotlib.pyplot as plt

def compute_DCT_matrix(n):
    """Fungsi untuk menghitung matriks DCT"""
    c0 = 1 / sqrt(2)  # Konstanta
    DC = np.zeros((n, n))
    for u in range(n):
        cu = c0 if u == 0 else 1
        for x in range(n):
            DC[u, x] = sqrt(2 / n) * cu * cos(((2 * x + 1) * pi * u) / (2 * n))
    return DC

def DCT_2D(block, DCx, DCy):
    """Fungsi untuk menghitung DCT 2D"""
    return np.dot(np.dot(DCx, block), DCy)

def iDCT_2D(F, iDCx, iDCy):
    """Fungsi untuk menghitung invers DCT 2D"""
    return np.dot(np.dot(iDCx, F), iDCy)

# Path gambar
image_path = 'path/to/your/image.jpg'  # Ganti dengan path gambar Anda

# Baca citra dan konversi ke grayscale
f = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if f is None:
    raise FileNotFoundError(f"Gambar tidak ditemukan di path: {image_path}")

f = f.astype(float)  # Konversi ke float
n = 8  # Ukuran blok

# Ambil blok 8x8 pertama
block = f[:n, :n]

# Hitung matriks DCx dan DCy
DCx = compute_DCT_matrix(n)
DCy = compute_DCT_matrix(n)

# Hitung DCT blok
F = DCT_2D(block, DCx, DCy)

# Matriks kuantisasi
Q = np.array([
    [2, 2, 3, 4, 5, 6, 8, 11],
    [2, 2, 2, 4, 5, 7, 9, 11],
    [3, 2, 3, 5, 7, 9, 11, 12],
    [4, 4, 5, 7, 9, 11, 12, 12],
    [5, 5, 7, 9, 11, 12, 12, 12],
[6, 7, 9, 11, 12, 12, 12, 12],
[8, 9, 11, 12, 12, 12, 12, 12],
[11, 11, 12, 12, 12, 12, 12, 12]
])
# Proses kuantisasi
Fq = np.round(F / Q)
# Proses dekuantisasi
Fdq = Fq * Q
# Matriks iDCx dan iDCy
iDCx = DCx.T # Transpose matriks DCx
iDCy = DCy.T # Transpose matriks DCy
# Rekonstruksi blok menggunakan iDCT
iDCT = np.round(iDCT_2D(Fdq, iDCx, iDCy))
# Tampilkan hasil
print("Blok asli (8x8):")
print(block)
print("\nHasil DCT (8x8):")
print(F)
print("\nHasil kuantisasi (8x8):")
print(Fq)
print("\nHasil dekuantisasi (8x8):")
print(Fdq)
print("\nHasil rekonstruksi iDCT (8x8):")
print(iDCT)
# Visualisasi blok asli dan hasil rekonstruksi

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(block, cmap='gray')
plt.title('Blok Asli (8x8)')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(iDCT, cmap='gray')
plt.title('Rekonstruksi iDCT (8x8)')
plt.axis('off')
plt.show()