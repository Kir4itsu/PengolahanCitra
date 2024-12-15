import cv2
import numpy as np

# Path gambar (ubah sesuai lokasi gambar Anda)
image_path_ref = 'path/to/your/image/kuching.jpeg'
image_path_rek = 'path/to/your/reconstructed/image/kuching_rek.jpg'

# Fungsi PSNR
def psnr(ImRef, ImRek):
    ImRef = ImRef.astype(np.float64)
    ImRek = ImRek.astype(np.float64)
    N, M, L = ImRef.shape
    
    # Hitung error
    Im4 = ((ImRef - ImRek) ** 2).sum(axis=2)  # Total per kanal
    MSE = Im4.sum() / (L * N * M)  # Hitung MSE

    if MSE != 0:
        x = 255 ** 2
        PSNR = 10 * np.log10(x / MSE)
    else:
        PSNR = float('inf')  # Nilai PSNR tak hingga jika MSE=0
    
    return PSNR

# Baca gambar referensi dan rekonstruksi
try:
    ImRef = cv2.imread(image_path_ref)
    ImRek = cv2.imread(image_path_rek)

    if ImRef is None or ImRek is None:
        raise FileNotFoundError("Salah satu gambar tidak ditemukan. Pastikan kedua path benar.")

    # Ubah ukuran gambar rekonstruksi agar sesuai dengan referensi
    if ImRef.shape != ImRek.shape:
        ImRek = cv2.resize(ImRek, (ImRef.shape[1], ImRef.shape[0]))

    # Hitung PSNR
    psnr_value = psnr(ImRef, ImRek)

    # Tampilkan hasil
    print(f"Nilai PSNR: {psnr_value:.2f} dB")

except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(f"Terjadi kesalahan: {e}")