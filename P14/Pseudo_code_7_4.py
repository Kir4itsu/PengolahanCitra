import cv2
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog

# Fungsi untuk memilih file video
def select_video_file():
    root = tk.Tk()
    root.withdraw()
    video_path = filedialog.askopenfilename(
        title="Pilih file video",
        filetypes=[("Video files", "*.mp4;*.avi;*.mov;*.mkv")]
    )
    return video_path

# Membaca video
video_path = select_video_file()
if not video_path:
    print("Tidak ada file yang dipilih.")
    exit()

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Gagal membuka file video.")
else:
    print("Mulai memproses video...")
    os.makedirs("frames", exist_ok=True)
    frame_count = 0
    max_frames = 2

    while cap.isOpened() and frame_count < max_frames:
        ret, frame = cap.read()
        if not ret:
            print("Video selesai diputar.")
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        img.show()

        savename = f"frames/image_{frame_count + 1}.png"
        cv2.imwrite(savename, frame)
        print(f"Frame {frame_count + 1} disimpan sebagai {savename}")

        frame_count += 1

    cap.release()
    print("Proses selesai.")
