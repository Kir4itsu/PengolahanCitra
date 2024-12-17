import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib import pyplot as plt

# Fungsi untuk memilih file video
def pilih_video():
    global video_path
    video_path = filedialog.askopenfilename(
        title="Pilih File Video",
        filetypes=[("Video Files", "*.mp4 *.avi *.mkv")]
    )
    if video_path:
        messagebox.showinfo("File Dipilih", f"File: {video_path}")
        proses_video(video_path)
    else:
        messagebox.showwarning("Tidak Ada File", "Silakan pilih file video.")

# Fungsi untuk memproses video
def proses_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        messagebox.showerror("Error", "Gagal membuka file video.")
        return

    ret, frame1 = cap.read()
    if not ret:
        messagebox.showerror("Error", "Gagal membaca frame pertama.")
        cap.release()
        return

    im1 = frame1  # Frame awal sebagai referensi
    N, M, L = im1.shape  # Dimensi frame
    Mob = np.zeros_like(im1)  # Inisialisasi array untuk menyimpan perbedaan blok
    block_size = 4  # Ukuran blok 4x4

    while True:
        ret, frame2 = cap.read()
        if not ret:
            print("Video selesai atau tidak ada frame.")
            break

        im2 = frame2  # Frame saat ini
        # Hitung perbedaan blok 4x4 antar frame
        for n in range(0, N - block_size, block_size):
            for m in range(0, M - block_size, block_size):
                Mob[n:n+block_size, m:m+block_size, :] = abs(
                    im1[n:n+block_size, m:m+block_size, :] -
                    im2[n:n+block_size, m:m+block_size, :]
                )

        # Tampilkan hasil
        plt.imshow(cv2.cvtColor(Mob, cv2.COLOR_BGR2RGB))
        plt.title("Perbedaan Blok Antar Frame (4x4)")
        plt.axis('off')
        plt.show(block=False)
        plt.pause(0.1)
        plt.clf()

        # Perbarui frame referensi
        im1 = im2

        # Konfirmasi untuk melanjutkan atau berhenti
        if messagebox.askyesno("Hentikan Proses", "Lanjutkan ke frame berikutnya?") == False:
            break

    cap.release()
    plt.close()
    messagebox.showinfo("Proses Selesai", "Video selesai diproses.")

# Menjalankan fungsi memilih video langsung tanpa GUI
pilih_video()
