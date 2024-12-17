import cv2
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Fungsi untuk memilih file video dari dialog file
def select_video_file():
    root = tk.Tk()
    root.withdraw()  # Menyembunyikan jendela utama
    video_path = filedialog.askopenfilename(title="Pilih file video", filetypes=[("Video files", "*.mp4;*.avi;*.mov;*.mkv")])
    return video_path

# Pilih file video menggunakan dialog
video_path = select_video_file()
if not video_path:
    print("File video tidak dipilih. Proses dihentikan.")
    exit()

# Membaca video
cap = cv2.VideoCapture(video_path)
Nf = 30 # Jumlah frame yang ingin diproses
count = 0

print("Mulai memproses video...")
while cap.isOpened() and count < Nf:
    ret, frame = cap.read()
    if not ret:
        break
    # Konversi gambar dari BGR ke RGB untuk ditampilkan
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Tampilkan gambar
    plt.imshow(frame_rgb)
    plt.axis('off') # Hilangkan axis untuk kejelasan
    plt.show(block=False)
    plt.pause(0.1) # Waktu jeda antar frame (dalam detik)
    count += 1

cap.release()
print("Proses selesai.")