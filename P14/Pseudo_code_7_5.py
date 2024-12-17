import cv2
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

# Memilih video
video_path = select_video_file()
if not video_path:
    print("Tidak ada file yang dipilih.")
    exit()

# Membuka file video
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Gagal membuka file video.")
else:
    print("Video berhasil dibuka.")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = cap.get(cv2.CAP_PROP_FPS) if cap.get(cv2.CAP_PROP_FPS) > 0 else 30
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter("output_video.avi", fourcc, fps, (frame_width, frame_height))

    Nf = 25  # Jumlah frame yang ingin diproses
    count = 0
    print("Mulai memproses video...")

    while cap.isOpened() and count < Nf:
        ret, frame = cap.read()
        if not ret:
            print("Frame selesai atau video habis.")
            break

        out.write(frame)
        print(f"Frame {count + 1} diproses dan ditambahkan ke video output.")
        count += 1

    cap.release()
    out.release()
    print("Proses selesai. Video baru disimpan di: output_video.avi")
