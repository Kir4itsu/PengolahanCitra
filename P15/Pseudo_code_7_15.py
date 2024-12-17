import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fungsi utama untuk memproses video
def motion_detection():
    root = tk.Tk()
    root.withdraw()
    video_path = filedialog.askopenfilename(title="Pilih File Video", filetypes=[("Video Files", "*.mp4;*.avi")])
    if not video_path:
        print("File video tidak dipilih.")
        return

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Gagal membuka file video.")
        return

    print("Memulai proses video...")
    ret, frame1 = cap.read()
    if not ret:
        print("Gagal membaca frame pertama.")
        cap.release()
        return

    im1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    stop = True

    while stop:
        ret, frame2 = cap.read()
        if not ret:
            print("Video selesai atau tidak ada frame.")
            break

        im2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        Edif = cv2.absdiff(im1, im2)

        plt.imshow(Edif, cmap='gray')
        plt.title("Perbedaan Frame (Motion Detection)")
        plt.axis('off')
        plt.show(block=False)
        plt.pause(0.1)
        plt.clf()

        im1 = im2
        if input("Tekan [Enter] untuk melanjutkan atau ketik 'q' untuk berhenti: ").lower() == 'q':
            stop = False
    cap.release()
    print("Proses selesai.")

motion_detection()
