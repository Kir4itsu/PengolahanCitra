import cv2
import numpy as np
import matplotlib.pyplot as plt
import pywt

# Path gambar (ubah sesuai lokasi gambar Anda)
image_path = 'path/to/your/image/kuching.jpeg'

# Fungsi untuk menghitung DWT Haar
def dwthaar(image):
    LL, (LH, HL, HH) = pywt.dwt2(image, 'haar')
    return LL, HL, LH, HH

# Fungsi untuk menyesuaikan ukuran array
def resize_to_match(arr, target_shape):
    result = np.zeros(target_shape)
    min_rows = min(arr.shape[0], target_shape[0])
    min_cols = min(arr.shape[1], target_shape[1])
    result[:min_rows, :min_cols] = arr[:min_rows, :min_cols]
    return result

# Baca citra dan konversi ke grayscale
Im = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if Im is None:
    raise FileNotFoundError(f"Gambar tidak ditemukan di path: {image_path}")

# Tampilkan citra asli
plt.figure(figsize=(6, 6))
plt.imshow(Im, cmap='gray')
plt.title('Citra Asli')
plt.axis('off')
plt.show()

# Proses DWT untuk level 1, 2, dan 3
for level in range(1, 4):
    print(f"Melakukan DWT Haar hingga level {level}...")
    
    # Hitung DWT sesuai jumlah level
    LL1, HL1, LH1, HH1 = dwthaar(Im)
    LL2, HL2, LH2, HH2 = None, None, None, None
    LL3, HL3, LH3, HH3 = None, None, None, None
    
    if level >= 2:
        LL2, HL2, LH2, HH2 = dwthaar(LL1)
    if level >= 3:
        LL3, HL3, LH3, HH3 = dwthaar(LL2)
    
    # Gabungkan hasil sesuai level
    ImHasil = None
    if level == 1:
        target_shape = LL1.shape
        ImHasil = np.vstack((
            np.hstack((LL1, resize_to_match(HL1, target_shape))),
            np.hstack((resize_to_match(LH1, target_shape), resize_to_match(HH1, target_shape)))
        ))
    elif level == 2:
        target_shape = LL1.shape
        ImHasil_level1 = np.vstack((
            np.hstack((LL1, resize_to_match(HL1, target_shape))),
            np.hstack((resize_to_match(LH1, target_shape), resize_to_match(HH1, target_shape)))
        ))
        
        target_shape = LL2.shape
        ImHasil = np.vstack((
            np.hstack((LL2, resize_to_match(HL2, target_shape))),
            np.hstack((resize_to_match(LH2, target_shape), resize_to_match(HH2, target_shape))),
            resize_to_match(ImHasil_level1, (LL2.shape[0] * 2, LL2.shape[1] * 2))
        ))
    elif level == 3:
        target_shape = LL2.shape
        ImHasil_level2 = np.vstack((
            np.hstack((LL2, resize_to_match(HL2, target_shape))),
            np.hstack((resize_to_match(LH2, target_shape), resize_to_match(HH2, target_shape)))
        ))
        
        target_shape = LL3.shape
        ImHasil = np.vstack((
            np.hstack((LL3, resize_to_match(HL3, target_shape))),
            np.hstack((resize_to_match(LH3, target_shape), resize_to_match(HH3, target_shape))),
            resize_to_match(ImHasil_level2, (LL3.shape[0] * 2, LL3.shape[1] * 2))
        ))
    
    # Tampilkan hasil transformasi Haar
    plt.figure(figsize=(10, 10))
    plt.imshow(ImHasil, cmap='gray')
    plt.title(f'Hasil DWT Haar - Level {level}')
    plt.axis('off')
    plt.show()