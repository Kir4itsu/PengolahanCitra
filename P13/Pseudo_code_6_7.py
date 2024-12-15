import cv2
import numpy as np
from math import sqrt, cos, pi
import matplotlib.pyplot as plt

# Path gambar (ubah sesuai lokasi gambar Anda)
image_path = 'path/to/your/image/kuching.jpeg'

# Fungsi untuk menghitung matriks QDCT
def compute_QDCT_matrix(n, Q):
    c0 = 1 / sqrt(2) # Konstanta
    QDC = np.zeros((n, n))
    for u in range(n):
        cu = c0 if u == 0 else 1
        for x in range(n):
            QDC[u, x] = sqrt(2 / (n * Q)) * cu * cos(((2 * x + 1) * pi * u) / (2 * n))
    return QDC

# Fungsi untuk menghitung matriks iQDCT
def compute_iQDCT_matrix(n, Q):
    c0 = 1 / sqrt(2) # Konstanta
    iQDC = np.zeros((n, n))
    for x in range(n):
        for u in range(n):
            cu = c0 if u == 0 else 1
            iQDC[x, u] = sqrt((2 * Q) / n) * cu * cos(((2 * x + 1) * pi * u) / (2 * n))
    return iQDC

# Baca citra dan konversi ke grayscale
f = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if f is None:
    raise FileNotFoundError(f"Gambar tidak ditemukan di path: {image_path}")
f = f.astype(float) # Konversi ke float

n = 8 # Ukuran blok
Q = 4.5 # Nilai Q

# Ambil blok 8x8 pertama
block = f[:n, :n]

# Hitung matriks QDCx dan QDCy
QDCx = compute_QDCT_matrix(n, Q)
QDCy = QDCx.T # Transpose untuk QDCy

# Hitung QDCT
F = np.dot(np.dot(QDCx, block), QDCy)

# Hitung matriks iQDCx dan iQDCy
iQDCx = compute_iQDCT_matrix(n, Q)
iQDCy = iQDCx.T # Transpose untuk iQDCy

# Rekonstruksi iQDCT
iQDCT = np.round(np.dot(np.dot(iQDCx, F), iQDCy))

# Tampilkan hasil
print("Blok asli (8x8):")
print(block)
print("\nHasil QDCT (8x8):")
print(F)
print("\nHasil rekonstruksi iQDCT (8x8):")
print(iQDCT)

# Visualisasi blok asli dan hasil rekonstruksi
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(block, cmap='gray')
plt.title('Blok Asli (8x8)')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(iQDCT, cmap='gray')
plt.title('Rekonstruksi iQDCT (8x8)')
plt.axis('off')
plt.show()