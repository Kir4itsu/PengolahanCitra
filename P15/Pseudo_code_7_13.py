import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Fungsi untuk memilih file video
def select_video_file():
    root = tk.Tk()
    root.withdraw()  # Menyembunyikan jendela utama
    video_path = filedialog.askopenfilename(
        title="Pilih file video",
        filetypes=[("Video files", ".mp4 .avi .mov .mkv")]
    )
    return video_path

# Fungsi Rekonstruksi Subsampling
def reconstruct_sampling(Y, Cb, Cr, sb, sk):
    """
    Rekonstruksi subsampling dari komponen Y, Cb, Cr menjadi RGB.
    """
    if sb == 1 and sk == 1:  # Format 4:4:4
        iYCbCr = np.stack((Y, Cb, Cr), axis=-1)
    elif sb == 1 and sk == 2:  # Format 4:2:2
        iYCbCr = np.zeros((Y.shape[0], Y.shape[1], 3), dtype=Cb.dtype)
        iYCbCr[:, :, 0] = Y
        iYCbCr[:, 0::2, 1] = Cb
        iYCbCr[:, 1::2, 1] = Cb
        iYCbCr[:, 0::2, 2] = Cr
        iYCbCr[:, 1::2, 2] = Cr
    elif sb == 2 and sk == 2:  # Format 4:2:0
        iYCbCr = np.zeros((Y.shape[0], Y.shape[1], 3), dtype=Cb.dtype)
        iYCbCr[:, :, 0] = Y
        iYCbCr[0::2, 0::2, 1] = Cb
        iYCbCr[1::2, 0::2, 1] = Cb
        iYCbCr[0::2, 1::2, 1] = Cb
        iYCbCr[1::2, 1::2, 1] = Cb
        iYCbCr[0::2, 0::2, 2] = Cr
        iYCbCr[1::2, 0::2, 2] = Cr
        iYCbCr[0::2, 1::2, 2] = Cr
        iYCbCr[1::2, 1::2, 2] = Cr
    return cv2.cvtColor(iYCbCr.astype(np.uint8), cv2.COLOR_YCrCb2BGR)

# Fungsi Menampilkan Hasil
def display_results(frame, YCbCr, Y, Cb, Cr, RGB):
    """
    Menampilkan semua komponen citra: asli, YCbCr, Y, Cb, Cr, dan rekonstruksi.
    """
    plt.figure(figsize=(12, 8))
    plt.subplot(3, 4, 1)
    plt.imshow(cv2.cvtColor(YCbCr, cv2.COLOR_YCrCb2RGB))
    plt.title("Citra YCbCr")
    plt.axis('off')
    plt.subplot(3, 4, 2)
    plt.imshow(Y, cmap='gray')
    plt.title("Komponen Y")
    plt.axis('off')
    plt.subplot(3, 4, 3)
    plt.imshow(Cb, cmap='gray')
    plt.title("Komponen Cb")
    plt.axis('off')
    plt.subplot(3, 4, 4)
    plt.imshow(Cr, cmap='gray')
    plt.title("Komponen Cr")
    plt.axis('off')
    plt.subplot(3, 4, 5)
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.title("Citra Asli")
    plt.axis('off')
    plt.subplot(3, 4, 6)
    plt.imshow(cv2.cvtColor(RGB, cv2.COLOR_BGR2RGB))
    plt.title("Citra Rekonstruksi")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# Pilih file video
print("Silakan pilih file video Anda...")
video_path = select_video_file()

# Periksa apakah file dipilih
if not video_path:
    print("Tidak ada file yang dipilih. Program dihentikan.")
    exit()

# Membuka file video
cap = cv2.VideoCapture(video_path)

# Periksa apakah file video berhasil dibuka
if not cap.isOpened():
    print("Gagal membuka file video.")
    exit()

print("Memulai proses video...")
sk, sb = 2, 2  # Parameter subsampling
stop = True  # Kondisi loop

# Loop untuk memproses setiap frame video
while stop:
    ret, frame = cap.read()  # Membaca satu frame
    if not ret:
        print("Video selesai atau tidak ada frame yang tersedia.")
        break

    # Konversi ke YCbCr dan lakukan subsampling
    YCbCr = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    Y = YCbCr[:, :, 0]
    Cb = YCbCr[0::sb, 0::sk, 1]
    Cr = YCbCr[0::sb, 0::sk, 2]

    # Rekonstruksi dari subsampling
    RGB = reconstruct_sampling(Y, Cb, Cr, sb, sk)

    # Tampilkan hasil
    display_results(frame, YCbCr, Y, Cb, Cr, RGB)

    # Kondisi untuk menghentikan loop
    user_input = input("Tekan [Enter] untuk melanjutkan atau ketik 'q' untuk berhenti: ").lower()
    if user_input == 'q':
        stop = False

print("Proses selesai.")

# Tutup file video
cap.release()
