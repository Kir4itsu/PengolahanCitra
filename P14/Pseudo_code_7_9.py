import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import grey_dilation, grey_erosion
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

# Fungsi morfologi
def morphological_operations(image, se_size=1):
    structure_element = np.ones((se_size * 2 + 1, se_size * 2 + 1))
    dilated = grey_dilation(image, footprint=structure_element)
    eroded = grey_erosion(image, footprint=structure_element)
    return np.abs(dilated - eroded)

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

        edge_result = morphological_operations(frame)
        plt.imshow(edge_result.astype(np.uint8))
        plt.axis('off')
        plt.show(block=False)
        plt.pause(0.1)
        plt.clf()
cap.release()
print("Proses selesai.")
