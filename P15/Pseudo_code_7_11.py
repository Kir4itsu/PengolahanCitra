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

# Fungsi Koreksi Gamma
def gamma_correction(image, gamma):
    """
    Melakukan koreksi gamma pada sebuah frame.
    """
    gamma_table = np.array([((i / 255.0) ** gamma) * 255 for i in range(256)]).astype("uint8")
    return cv2.LUT(image, gamma_table)

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
gamma = 0.75  # Set nilai gamma pengatur kecerahan
stop = True  # Kondisi loop

# Loop untuk memproses setiap frame video
while stop:
    ret, frame = cap.read()  # Membaca satu frame
    if not ret:
        print("Video selesai atau tidak ada frame yang tersedia.")
        break

    # Lakukan koreksi gamma pada frame
    frame_corrected = gamma_correction(frame, gamma)

    # Tampilkan frame hasil koreksi gamma
    plt.imshow(cv2.cvtColor(frame_corrected, cv2.COLOR_BGR2RGB))  # Konversi BGR ke RGB
    plt.axis('off')
    plt.title("Hasil Koreksi Gamma")
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
