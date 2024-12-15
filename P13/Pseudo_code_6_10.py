import cv2
import numpy as np
import matplotlib.pyplot as plt
import pywt

# Path gambar (ubah sesuai lokasi gambar Anda)
image_path = 'path/to/your/image/kuching.jpeg'

# Fungsi DWT (Discrete Wavelet Transform)
def dwt(f, wavelet):
    coeffs = pywt.dwt2(f, wavelet)
    LL, (LH, HL, HH) = coeffs
    return LL, LH, HL, HH

# Fungsi iDWT (Inverse Discrete Wavelet Transform)
def idwt(LL, LH, HL, HH, wavelet):
    coeffs = (LL, (LH, HL, HH))
    return pywt.idwt2(coeffs, wavelet)

# Fungsi untuk menyesuaikan ukuran array
def resize_to_match(arr, target_shape):
    resized = np.zeros(target_shape)
    min_rows = min(arr.shape[0], target_shape[0])
    min_cols = min(arr.shape[1], target_shape[1])
    resized[:min_rows, :min_cols] = arr[:min_rows, :min_cols]
    return resized

# Baca citra dan konversi ke grayscale
f = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if f is None:
    raise FileNotFoundError(f"Gambar tidak ditemukan di path: {image_path}")

# Tampilkan citra asli
plt.figure(figsize=(6, 6))
plt.imshow(f, cmap='gray')
plt.title('Citra Asli')
plt.axis('off')
plt.show()

# Gunakan wavelet Haar (db4)
wavelet = pywt.Wavelet('db4')

# Proses dekomposisi wavelet 4 skala
LL1, LH1, HL1, HH1 = dwt(f, wavelet)
LL2, LH2, HL2, HH2 = dwt(LL1, wavelet)
LL3, LH3, HL3, HH3 = dwt(LL2, wavelet)
LL4, LH4, HL4, HH4 = dwt(LL3, wavelet)

# Ukuran target untuk LL4
target_shape = LL4.shape

# Sesuaikan ukuran semua subband ke ukuran LL4
LH4 = resize_to_match(LH4, target_shape)
HL4 = resize_to_match(HL4, target_shape)
HH4 = resize_to_match(HH4, target_shape)
LH3 = resize_to_match(LH3, target_shape)
HL3 = resize_to_match(HL3, target_shape)
HH3 = resize_to_match(HH3, target_shape)
LH2 = resize_to_match(LH2, target_shape)
HL2 = resize_to_match(HL2, target_shape)
HH2 = resize_to_match(HH2, target_shape)
LH1 = resize_to_match(LH1, target_shape)
HL1 = resize_to_match(HL1, target_shape)
HH1 = resize_to_match(HH1, target_shape)

# Gabungkan semua subband ke dalam satu citra
WIm = np.vstack((
    np.hstack((LL4 / 4, LH4 / 2, HL4 / 2, HH4 / 2)),
    np.hstack((LH3 / 2, HL3 / 2, HH3 / 2, np.zeros_like(LL4))),
    np.hstack((LH2 / 2, HL2 / 2, HH2 / 2, np.zeros_like(LL4))),
    np.hstack((LH1 / 2, HL1 / 2, HH1 / 2, np.zeros_like(LL4)))
))

# Tampilkan citra dekomposisi
plt.figure(figsize=(10, 10))
plt.imshow(np.abs(WIm), cmap='gray')
plt.title('Citra Dekomposisi')
plt.axis('off')
plt.show()

# Proses rekonstruksi wavelet 4 skala
f0 = resize_to_match(LL4, LH4.shape) # Sesuaikan ukuran LL4 sebelum rekonstruksi
f0 = idwt(f0, LH4, HL4, HH4, wavelet)

# Lakukan rekonstruksi untuk skala berikutnya
f0 = resize_to_match(f0, LH3.shape) # Sesuaikan ukuran hasil rekonstruksi sebelumnya
f0 = idwt(f0, LH3, HL3, HH3, wavelet)
f0 = resize_to_match(f0, LH2.shape) # Sesuaikan ukuran untuk rekonstruksi berikutnya
f0 = idwt(f0, LH2, HL2, HH2, wavelet)
f0 = resize_to_match(f0, LH1.shape) # Sesuaikan ukuran untuk rekonstruksi terakhir
f0 = idwt(f0, LH1, HL1, HH1, wavelet)

print("Ukuran LL:", LL4.shape)
print("Ukuran LH:", LH4.shape)
print("Ukuran HL:", HL4.shape)
print("Ukuran HH:", HH4.shape)

# Tampilkan citra rekonstruksi
plt.figure(figsize=(6, 6))
plt.imshow(np.abs(f0), cmap='gray')
plt.title('Citra Rekonstruksi')
plt.axis('off')
plt.show()