import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

# Tentukan alamat file gambar
image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'

# Pastikan file gambar ada
if os.path.exists(image_path):
    print("File gambar ditemukan")
    # Baca gambar
    img = cv2.imread(image_path)
    # Konversi BGR ke RGB
    Img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Tampilkan citra warna
    plt.figure(1)
    plt.imshow(Img)
    plt.title("Citra Warna")
    plt.axis('off')
    
    # Tampilkan komponen R
    plt.figure(2)
    plt.imshow(Img[:, :, 0], cmap='gray')
    plt.title("Komponen R")
    plt.axis('off')
    
    # Tampilkan komponen G
    plt.figure(3)
    plt.imshow(Img[:, :, 1], cmap='gray')
    plt.title("Komponen G")
    plt.axis('off')
    
    # Tampilkan komponen B
    plt.figure(4)
    plt.imshow(Img[:, :, 2], cmap='gray')
    plt.title("Komponen B")
    plt.axis('off')
    
    plt.show()
else:
    print("File gambar tidak ditemukan.")