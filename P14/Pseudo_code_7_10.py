import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
import tkinter as tk
from tkinter import filedialog

# Fungsi untuk menghitung gradien Prewitt
def compute_prewitt_gradient(image):
    """
    Menghitung gradien Prewitt untuk gambar grayscale.
    """
    # Kernel Prewitt
    prewitt_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    prewitt_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

    # Gradien pada sumbu X dan Y
    grad_x = convolve(image, prewitt_x)
    grad_y = convolve(image, prewitt_y)

    # Magnitudo gradien
    gradient = np.sqrt(grad_x**2 + grad_y**2)
    return gradient

# Fungsi untuk memilih file video dari dialog file
def select_video_file():
    root = tk.Tk()
    root.withdraw()  # Menyembunyikan jendela utama
    video_path = filedialog.askopenfilename(title="Pilih file video", filetypes=[("Video files", "*.mp4;*.avi;*.mov;*.mkv")])
    return video_path

# Memilih file video
video_path = select_video_file()

if not video_path:
    print("Tidak ada file video yang dipilih.")
else:
    # Membuka file video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Gagal membuka file video.")
    else:
        print("Memulai proses video...")
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Jumlah frame dalam video

        for i in range(frame_count):
            ret, frame = cap.read()  # Membaca frame ke-i
            if not ret:
                print("Tidak dapat membaca frame.")
                break

            # Hitung gradien Prewitt untuk setiap channel warna
            grad_r = compute_prewitt_gradient(frame[:, :, 2])  # Komponen R
            grad_g = compute_prewitt_gradient(frame[:, :, 1])  # Komponen G
            grad_b = compute_prewitt_gradient(frame[:, :, 0])  # Komponen B

            # Gabungkan ketiga gradien menjadi satu gambar berwarna
            grad_combined = np.stack((grad_r, grad_g, grad_b), axis=-1).astype(np.uint8)

            # Tampilkan hasil gradien
            plt.imshow(grad_combined)
            plt.axis('off')
            plt.title(f"Gradien Prewitt Frame {i+1}")
            plt.show(block=False)
            plt.pause(0.03)  # Waktu jeda antar frame
            plt.clf()  # Bersihkan plot untuk frame berikutnya

        print("Proses selesai.")

    # Tutup video
    cap.release()
