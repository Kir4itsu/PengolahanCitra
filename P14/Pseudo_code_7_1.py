import cv2
import time
import numpy as np
import os

# Fungsi untuk meminta path file secara manual
def get_video_path():
    video_path = input("Masukkan path lengkap ke file video: ")
    if not os.path.exists(video_path):
        print("File tidak ditemukan. Pastikan path benar.")
        return None
    return video_path

def analyze_video_framerate(video_path):
    # Membaca video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Gagal membuka video. Pastikan format video didukung.")
        return

    timestamps = []
    print("Mulai memproses video...")
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        timestamps.append(time.time() - start_time)
    
    cap.release()

    # Hitung frame rate
    if len(timestamps) > 1:
        diffs = np.diff(timestamps)
        diffs = diffs[diffs > 0]  # Ambil hanya nilai selisih waktu yang positif
        if len(diffs) > 0:
            framerate = np.mean(1.0 / diffs)
            print(f"Frame rate: {framerate:.2f} FPS")
        else:
            print("Tidak cukup data untuk menghitung frame rate.")
    else:
        print("Tidak cukup data untuk menghitung frame rate.")
    
    print("Proses selesai.")

# Meminta input dari pengguna
video_path = get_video_path()
if video_path:
    analyze_video_framerate(video_path)
