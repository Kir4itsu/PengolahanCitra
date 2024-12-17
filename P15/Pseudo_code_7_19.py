import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# **1. Fungsi Segmentasi RGB**
def segm_rgb_pixel(im, Wref, Th):
    """
    Segmentasi warna menggunakan ruang RGB.
    """
    diff = np.sqrt(np.sum((im - Wref) ** 2, axis=2))
    mask = diff < Th
    segmented = np.zeros_like(im)
    segmented[mask] = im[mask]
    return segmented

# **2. Fungsi Segmentasi HCL (HSL)**
def segm_hcl_pixel(im, Wref, Th):
    """
    Segmentasi warna menggunakan ruang HCL (HSL).
    """
    # Konversi RGB ke HSL
    im_hcl = cv2.cvtColor(im.astype(np.uint8), cv2.COLOR_RGB2HLS)
    Wref_hcl = cv2.cvtColor(np.uint8([[Wref]]), cv2.COLOR_RGB2HLS)[0, 0]
    diff = np.sqrt(np.sum((im_hcl - Wref_hcl) ** 2, axis=2))
    mask = diff < Th
    segmented = np.zeros_like(im)
    segmented[mask] = im[mask]
    return segmented

# **3. Fungsi untuk memilih file video**
def pilih_file_video():
    root = tk.Tk()
    root.withdraw()  # Sembunyikan jendela utama
    video_path = filedialog.askopenfilename(
        title="Pilih file video",
        filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")]
    )
    return video_path

# **4. Fungsi Utama**
def main():
    # **Pilih file video**
    print("Silakan pilih file video Anda...")
    video_path = pilih_file_video()
    if not video_path:
        print("Tidak ada file yang dipilih. Program dihentikan.")
        return

    # **Membuka video**
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Gagal membuka file video.")
        return
    else:
        print("Memulai proses video...")

    # **Baca frame pertama untuk mengambil warna referensi**
    ret, frame = cap.read()
    if not ret:
        print("Gagal membaca frame pertama.")
        cap.release()
        return

    # Konversi frame ke RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    h, w, _ = frame_rgb.shape
    x, y = w // 2, h // 2  # Koordinat tengah frame
    Wref = frame_rgb[y, x].astype(float)  # Warna referensi
    print(f"Warna referensi otomatis diambil dari tengah gambar: (R, G, B) = {Wref}")

    # **Parameter Segmentasi**
    Th = 47  # Threshold segmentasi
    Nframe = 10  # Jumlah frame untuk diproses

    # **Proses Segmentasi dan Visualisasi**
    for k in range(Nframe):
        ret, frame = cap.read()
        if not ret:
            print("Frame habis atau tidak terbaca.")
            break

        # Konversi frame ke RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Segmentasi menggunakan ruang RGB
        segmented_rgb = segm_rgb_pixel(frame_rgb, Wref, Th)

        # Segmentasi menggunakan ruang HCL (HSL)
        segmented_hcl = segm_hcl_pixel(frame_rgb, Wref, Th)

        # Tampilkan hasil segmentasi
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 3, 1)
        plt.imshow(frame_rgb)
        plt.title("Frame Asli")
        plt.axis("off")

        plt.subplot(1, 3, 2)
        plt.imshow(segmented_rgb)
        plt.title("Segmentasi (RGB)")
        plt.axis("off")

        plt.subplot(1, 3, 3)
        plt.imshow(segmented_hcl)
        plt.title("Segmentasi (HCL)")
        plt.axis("off")

        plt.tight_layout()
        plt.show()

    print("Proses selesai.")
    cap.release()

if __name__ == "__main__":
    main()
