import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# **1. Fungsi untuk memilih file video**
def pilih_file_video():
    root = tk.Tk()
    root.withdraw()  # Sembunyikan jendela utama
    video_path = filedialog.askopenfilename(
        title="Pilih file video",
        filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")]
    )
    return video_path

# **2. Fungsi Deteksi Wajah**
def deteksi_wajah(video_path, Nframe=30):
    # Muat Haar Cascade Classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Buka file video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Gagal membuka file video.")
        return

    print("Memulai proses deteksi wajah...")
    frame_count = 0  # Counter frame

    # Loop untuk membaca dan memproses sejumlah frame
    while frame_count < Nframe:
        ret, frame = cap.read()
        if not ret:
            print("Video selesai atau tidak ada frame lagi.")
            break

        # Konversi ke grayscale untuk deteksi wajah
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Deteksi wajah menggunakan Haar Cascade
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Anotasi bingkai pada wajah
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, 'Face', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Konversi BGR ke RGB untuk tampilan Matplotlib
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Tampilkan frame dengan anotasi
        plt.imshow(frame_rgb)
        plt.title(f"Frame {frame_count + 1}")
        plt.axis("off")
        plt.show(block=False)
        plt.pause(0.1)  # Jeda antar frame
        plt.clf()  # Bersihkan tampilan untuk frame berikutnya

        frame_count += 1

    print("Proses selesai.")
    cap.release()

# **3. Fungsi Utama**
def main():
    print("Silakan pilih file video Anda...")
    video_path = pilih_file_video()
    if not video_path:
        print("Tidak ada file yang dipilih. Program dihentikan.")
        return
    
    deteksi_wajah(video_path, Nframe=30)

if __name__ == "__main__":
    main()
