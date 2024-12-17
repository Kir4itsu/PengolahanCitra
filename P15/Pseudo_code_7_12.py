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

# Fungsi Histogram Equalization
def histogram_equalization(image):
    """
    Melakukan histogram equalization untuk setiap channel warna (R, G, B).
    """
    equalized = np.zeros_like(image)
    for channel in range(3):  # Proses untuk setiap channel warna
        equalized[:, :, channel] = cv2.equalizeHist(image[:, :, channel])
    return equalized

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
stop = True  # Kondisi loop

# Loop untuk memproses setiap frame video
while stop:
    ret, frame = cap.read()  # Membaca satu frame
    if not ret:
        print("Video selesai atau tidak ada frame yang tersedia.")
        break

    # Lakukan histogram equalization pada frame
    frame_equalized = histogram_equalization(frame)

    # Tampilkan frame hasil histogram equalization
    plt.imshow(cv2.cvtColor(frame_equalized, cv2.COLOR_BGR2RGB))  # Konversi BGR ke RGB
    plt.axis('off')
    plt.title("Hasil Histogram Equalization")
    plt.show(block=False)
    plt.pause(0.1)  # Jeda untuk melihat hasil
    plt.clf()  # Bersihkan tampilan untuk frame berikutnya

    # Kondisi untuk menghentikan loop
    user_input = input("Tekan [Enter] untuk melanjutkan atau ketik 'q' untuk berhenti: ").lower()
    if user_input == 'q':
        stop = False

print("Proses selesai.")

# Tutup file video
cap.release()
