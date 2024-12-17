import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
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

# Fungsi untuk menghitung gradien Prewitt
def compute_prewitt_gradient(image):
    prewitt_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    prewitt_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    grad_x = convolve(image, prewitt_x)
    grad_y = convolve(image, prewitt_y)
    return np.sqrt(grad_x**2 + grad_y**2)

# Memilih video
video_path = select_video_file()
if not video_path:
    print("Tidak ada file yang dipilih.")
    exit()

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Gagal membuka file video.")
else:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        grad_r = compute_prewitt_gradient(frame[:, :, 2])
        grad_g = compute_prewitt_gradient(frame[:, :, 1])
        grad_b = compute_prewitt_gradient(frame[:, :, 0])

        grad_combined = np.stack((grad_r, grad_g, grad_b), axis=-1).astype(np.uint8)
        plt.imshow(grad_combined)
        plt.axis('off')
        plt.show(block=False)
        plt.pause(0.1)
        plt.clf()
cap.release()
print("Proses selesai.")
