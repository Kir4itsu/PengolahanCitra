import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pywt

# Fungsi Subsampling
def sub_sampling(YCbCr):
    Y = YCbCr[:, :, 0]  # Komponen Y
    Cb = YCbCr[::2, ::2, 1]  # Subsampling komponen Cb
    Cr = YCbCr[::2, ::2, 2]  # Subsampling komponen Cr
    return Y, Cb, Cr

# Transformasi Wavelet Daubechies
def wavelet_transform(im):
    coeffs = pywt.dwt2(im, 'db1')
    A, (H, V, D) = coeffs
    return A, H, V, D

# Invers Transformasi Wavelet
def wavelet_inverse(A, H, V, D):
    coeffs = (A, (H, V, D))
    return pywt.idwt2(coeffs, 'db1')

# Rekonstruksi Subsampling
def reconstruct_sampling(Y, Cb, Cr):
    Cb_resized = cv2.resize(Cb, (Y.shape[1], Y.shape[0]), interpolation=cv2.INTER_LINEAR)
    Cr_resized = cv2.resize(Cr, (Y.shape[1], Y.shape[0]), interpolation=cv2.INTER_LINEAR)
    iYCbCr = np.zeros((Y.shape[0], Y.shape[1], 3), dtype=np.uint8)
    iYCbCr[:, :, 0] = Y
    iYCbCr[:, :, 1] = Cb_resized
    iYCbCr[:, :, 2] = Cr_resized
    return cv2.cvtColor(iYCbCr, cv2.COLOR_YCrCb2RGB)

# Menampilkan Hasil
def display_results(YCbCr, imWavY, imWavCb, imWavCr, imR):
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 4, 1)
    plt.imshow(np.abs(imWavY), cmap='gray')
    plt.title("Wavelet Y")
    plt.axis('off')
    plt.subplot(2, 4, 2)
    plt.imshow(np.abs(imWavCb), cmap='gray')
    plt.title("Wavelet Cb")
    plt.axis('off')
    plt.subplot(2, 4, 3)
    plt.imshow(np.abs(imWavCr), cmap='gray')
    plt.title("Wavelet Cr")
    plt.axis('off')
    plt.subplot(2, 4, 5)
    plt.imshow(cv2.cvtColor(YCbCr, cv2.COLOR_YCrCb2RGB))
    plt.title("Citra YCbCr Asli")
    plt.axis('off')
    plt.subplot(2, 4, 6)
    plt.imshow(imR)
    plt.title("Citra RGB Rekonstruksi")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# Fungsi utama untuk memproses video
def process_video():
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
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Video selesai atau tidak ada frame.")
            break

        YCbCr = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
        Y, Cb, Cr = sub_sampling(YCbCr)
        A1, H1, V1, D1 = wavelet_transform(Y)
        A2, H2, V2, D2 = wavelet_transform(Cb)
        A3, H3, V3, D3 = wavelet_transform(Cr)

        imRY = wavelet_inverse(A1, H1, V1, D1)
        imRCb = wavelet_inverse(A2, H2, V2, D2)
        imRCr = wavelet_inverse(A3, H3, V3, D3)
        imR = reconstruct_sampling(imRY, imRCb, imRCr)

        display_results(YCbCr, A1, A2, A3, imR)
        if input("Tekan [Enter] untuk melanjutkan atau ketik 'q' untuk berhenti: ").lower() == 'q':
            break
    cap.release()
    print("Proses selesai.")

process_video()
