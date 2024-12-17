import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Fungsi untuk menampilkan frame I, B, dan P
def tampil(I, B1, B2, P1, B3, B4, P2, B5, B6, Ip):
    """
    Menampilkan frame I, B, dan P dalam subplot.
    """
    plt.figure(figsize=(12, 8))
    plt.subplot(3, 4, 1), plt.imshow(I, cmap='gray'), plt.title("Frame I")
    plt.subplot(3, 4, 2), plt.imshow(np.abs(B1), cmap='gray'), plt.title("Frame B1")
    plt.subplot(3, 4, 3), plt.imshow(np.abs(B2), cmap='gray'), plt.title("Frame B2")
    plt.subplot(3, 4, 4), plt.imshow(np.abs(P1), cmap='gray'), plt.title("Frame P1")
    plt.subplot(3, 4, 5), plt.imshow(np.abs(B3), cmap='gray'), plt.title("Frame B3")
    plt.subplot(3, 4, 6), plt.imshow(np.abs(B4), cmap='gray'), plt.title("Frame B4")
    plt.subplot(3, 4, 7), plt.imshow(np.abs(P2), cmap='gray'), plt.title("Frame P2")
    plt.subplot(3, 4, 8), plt.imshow(np.abs(B5), cmap='gray'), plt.title("Frame B5")
    plt.subplot(3, 4, 9), plt.imshow(np.abs(B6), cmap='gray'), plt.title("Frame B6")
    plt.subplot(3, 4, 10), plt.imshow(Ip, cmap='gray'), plt.title("Frame Ip")
    plt.tight_layout()
    plt.show()

# Fungsi untuk memilih file video
def pilih_file_video():
    root = tk.Tk()
    root.withdraw()  # Sembunyikan jendela utama
    video_path = filedialog.askopenfilename(
        title="Pilih file video",
        filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")]
    )
    return video_path

# Fungsi utama
def main():
    # Parameter Group of Pictures (GoP) dan jumlah grup
    GoP = 9  # Jumlah Group of Pictures
    NG = 20  # Jumlah grup
    N = NG * GoP + 1  # Total jumlah frame yang akan diproses

    # Pilih file video
    print("Silakan pilih file video Anda...")
    video_path = pilih_file_video()
    if not video_path:
        print("Tidak ada file yang dipilih. Keluar dari program.")
        return

    # Membuka file video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Gagal membuka file video.")
        return
    else:
        print("Memulai proses video...")
    
    frames = []  # List untuk menyimpan frame video
    
    # Membaca frame video
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Konversi ke grayscale
        frames.append(gray_frame)
    cap.release()  # Tutup file video

    # Periksa jumlah frame
    if len(frames) < N:
        print(f"Jumlah frame video ({len(frames)}) kurang dari {N}. Kurangi jumlah frame.")
        return

    # Pemrosesan frame
    for i in range(0, N - 1, GoP):
        I = frames[i].astype(float)
        P1 = frames[i].astype(float) - frames[i + 3].astype(float)
        jum = (frames[i].astype(float) + frames[i + 3].astype(float)) / 2
        B1 = frames[i + 1].astype(float) - jum
        B2 = frames[i + 2].astype(float) - jum

        P2 = frames[i + 3].astype(float) - frames[i + 6].astype(float)
        jum = (frames[i + 3].astype(float) + frames[i + 6].astype(float)) / 2
        B3 = frames[i + 4].astype(float) - jum
        B4 = frames[i + 5].astype(float) - jum

        jum = (frames[i + 6].astype(float) + frames[i + GoP].astype(float)) / 2
        B5 = frames[i + 7].astype(float) - jum
        B6 = frames[i + 8].astype(float) - jum

        Ip = frames[i + GoP].astype(float)

        # Tampilkan hasil
        tampil(I, B1, B2, P1, B3, B4, P2, B5, B6, Ip)

    print("Proses selesai.")

if __name__ == "__main__":
    main()
