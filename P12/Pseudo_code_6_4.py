import cv2
import numpy as np
import matplotlib.pyplot as plt

def blok_proses_DCT(image_path, block_size_power=3):
    """
    Fungsi untuk membaca citra, menambah padding jika diperlukan, dan membagi citra menjadi blok-blok.
    
    Args:
    image_path (str): Path ke file gambar.
    block_size_power (int): Ukuran blok sebagai pangkat dari 2 (default: 3, untuk 8x8 blok).
    
    Returns:
    blok_list (list): Daftar blok citra ukuran BxB.
    padded_image (ndarray): Citra setelah ditambah padding.
    """
    # Validasi file
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"File tidak ditemukan: {image_path}")

    # Baca citra
    Im = cv2.imread(image_path)
    if Im is None:
        raise ValueError(f"Gagal membaca gambar dari: {image_path}")
    
    # Konversi ke format RGB
    Im = cv2.cvtColor(Im, cv2.COLOR_BGR2RGB)
    
    n = block_size_power  # Ukuran blok sebagai 2^n
    B = 2 ** n
    
    # Baca ukuran citra
    Mf, Nf, L = Im.shape
    mb = Mf % B
    nb = Nf % B
    
    # Penambahan padding agar citra menjadi kelipatan ukuran blok
    if nb > 0:  # Jika tidak kelipatan, tambahkan kolom
        padding_cols = B - nb
        Im = np.pad(Im, ((0, 0), (0, padding_cols), (0, 0)), 
                    mode='constant', constant_values=0)
    
    if mb > 0:  # Jika tidak kelipatan, tambahkan baris
        padding_rows = B - mb
        Im = np.pad(Im, ((0, padding_rows), (0, 0), (0, 0)), 
                    mode='constant', constant_values=0)
    
    # Tampilkan citra setelah padding
    plt.imshow(Im)
    plt.axis('off')
    plt.title("Citra Setelah Padding")
    plt.show()
    
    # Baca ukuran baru
    Mf, Nf, L = Im.shape
    mb = Mf // B  # Banyaknya blok arah x
    nb = Nf // B  # Banyaknya blok arah y
    
    # Pembacaan citra blok per blok
    blok_list = []
    for l in range(L):  # Loop untuk setiap kanal (RGB)
        for i in range(mb):
            for j in range(nb):
                m1, m2 = B * i, B * (i + 1)
                n1, n2 = B * j, B * (j + 1)
                BlokBxB = Im[m1:m2, n1:n2, l]  # Baca citra per blok BxB
                blok_list.append(BlokBxB)
    
    return blok_list, Im

# Gunakan fungsi (ganti path sesuai lokasi gambar anda)
image_path = 'path/to/your/image.jpg'  # Ganti dengan path gambar Anda
try:
    print("Memproses gambar, mohon tunggu...")
    blok_list, padded_image = blok_proses_DCT(image_path)
    print(f"Jumlah blok yang dihasilkan: {len(blok_list)}")
except FileNotFoundError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error tidak terduga: {e}")