import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Fungsi untuk memilih beberapa file gambar
def pilih_file_gambar():
    root = tk.Tk()
    root.withdraw()  # Sembunyikan jendela utama
    file_paths = filedialog.askopenfilenames(
        title="Pilih file gambar (minimal dua gambar)",
        filetypes=[("Gambar files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    return file_paths

# Fungsi untuk menampilkan vektor pergerakan
def tampilkan_vektor_pergerakan(I1, I2, blk=8, th_obj=50, th_sim=5):
    """
    Menampilkan pergerakan objek antar dua gambar menggunakan blok 8x8.
    """
    N, M = I1.shape[:2]  # Ukuran gambar
    I1_copy = I1.copy()  # Salinan gambar untuk modifikasi
    
    plt.figure(figsize=(10, 6))
    plt.imshow(I1, cmap='gray')  # Tampilkan gambar pertama sebagai background
    plt.title("Vektor Pergerakan Antar Gambar")
    plt.axis('off')
    
    for n in range(blk, N - blk, blk):  # Pembagian blok baris
        for m in range(blk, M - blk, blk):  # Pembagian blok kolom
            # Hitung rata-rata intensitas blok
            mean_val = np.mean(I1[n:n+blk, m:m+blk])
            if mean_val > th_obj:  # Jika ada objek (intensitas > threshold)
                a = False  # Parameter break
                for n1 in range(n-blk, n+blk+1, blk):
                    for m1 in range(m-blk, m+blk+1, blk):
                        # Cek batas gambar
                        if 0 <= n1 < N-blk and 0 <= m1 < M-blk:
                            # Hitung delta perbedaan absolut antar blok
                            delta = np.sum(np.abs(I2[n1:n1+blk, m1:m1+blk] - I1[n:n+blk, m:m+blk]))
                            if delta < th_sim:  # Jika blok serupa
                                plt.quiver(m+blk//2, n+blk//2, m1-m, n1-n, 
                                           angles='xy', scale_units='xy', scale=1, color='r')
                                a = True  # Set parameter break
                                break
                    if a:  # Keluar dari loop jika ditemukan blok serupa
                        break
    plt.show()

# Fungsi utama
def main():
    print("Pilih file gambar untuk diproses (minimal dua gambar)...")
    image_files = pilih_file_gambar()  # Pilih gambar dari dialog file
    
    # Periksa jumlah gambar yang dipilih
    if len(image_files) < 2:
        print("Jumlah gambar kurang dari dua. Harap pilih minimal dua gambar.")
        return
    
    blk = 8  # Ukuran blok
    th_obj = 50  # Threshold objek
    th_sim = 5  # Threshold kesamaan
    
    # Proses dua gambar berturut-turut
    for k in range(len(image_files) - 1):
        citra_k = image_files[k]  # Gambar ke-k
        citra_k1 = image_files[k+1]  # Gambar ke-(k+1)
        
        # Baca dua gambar berturut-turut
        I1 = cv2.imread(citra_k, cv2.IMREAD_GRAYSCALE)  # Gambar ke-k (grayscale)
        I2 = cv2.imread(citra_k1, cv2.IMREAD_GRAYSCALE)  # Gambar ke-(k+1) (grayscale)
        
        if I1 is None or I2 is None:
            print(f"Gagal membaca {citra_k} atau {citra_k1}.")
            continue
        
        print(f"Memproses {citra_k} dan {citra_k1}...")
        tampilkan_vektor_pergerakan(I1, I2, blk, th_obj, th_sim)  # Tampilkan vektor pergerakan

if __name__ == "__main__":
    main()
