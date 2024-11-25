import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'
Im = cv2.imread(image_path)

if Im is None:
    print("Error: Gambar tidak ditemukan atau gagal dibaca.")
else:
    Im = cv2.cvtColor(Im, cv2.COLOR_BGR2RGB).astype(np.float32)  # Konversi ke RGB
    plt.figure(figsize=(6, 6))
    plt.imshow(Im.astype(np.uint8))
    plt.title('Citra Asli')
    plt.axis('off')
    plt.show()

    x, y = 100, 100  # Contoh koordinat piksel
    RGB = Im[y, x, :]  # Warna referensi dalam RGB
    Th = 47  # Threshold untuk kesamaan warna

    # Konversi warna referensi ke HSV
    RGB_img = np.array([[RGB]], dtype=np.uint8)
    HSV = cv2.cvtColor(RGB_img, cv2.COLOR_RGB2HSV).squeeze()

    # Fungsi bantu konversi RGB ke HCL
    def rgb_to_hcl(rgb):
        r, g, b = rgb / 255.0
        max_c, min_c = max(r, g, b), min(r, g, b)
        l = (max_c + min_c) / 2
        if max_c == min_c:
            h = 0
            c = 0
        else:
            d = max_c - min_c
            c = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
            if max_c == r:
                h = (g - b) / d + (6 if g < b else 0)
            elif max_c == g:
                h = (b - r) / d + 2
            else:
                h = (r - g) / d + 4
            h /= 6
        return np.array([h * 360, c, l])

    HCL = rgb_to_hcl(RGB)

    # Konversi citra ke ruang warna HSV dan HCL
    citra_hsv = cv2.cvtColor(Im.astype(np.uint8), cv2.COLOR_RGB2HSV)
    citra_hcl = np.apply_along_axis(rgb_to_hcl, 2, Im)

    m, n, _ = citra_hsv.shape
    cit_hasilHSV = np.zeros_like(Im, dtype=np.uint8)
    cit_hasilRGB = np.zeros_like(Im, dtype=np.uint8)
    cit_hasilHCL = np.zeros_like(Im, dtype=np.uint8)

    # Segmentasi berdasarkan warna
    for i in range(m):
        for j in range(n):
            dR = (RGB[0] - Im[i, j, 0]) ** 2
            dG = (RGB[1] - Im[i, j,1]) ** 2
            dB = (RGB[2] - Im[i, j,2]) ** 2
            if np.sqrt(dR + dG + dB) <= Th:
                cit_hasilRGB[i, j, :] = Im[i, j, :].astype(np.uint8)

            # Segmentasi HSV
            dH = citra_hsv[i, j, 0] - HSV[0]
            S1, S2 = HSV[1], citra_hsv[i, j, 1]
            dV = (citra_hsv[i, j, 2] - HSV[2]) ** 2
            Dcyl = np.sqrt(dV + S1**2 + S2**2 - 2 * S1 * S2 * np.cos(np.radians(dH)))
            if Dcyl <= Th:
                cit_hasilHSV[i, j, :] = Im[i, j, :].astype(np.uint8)

            # Segmentasi HCL
            dHhcl = citra_hcl[i, j, 0] - HCL[0]
            Chcl1, Chcl2 = HCL[1], citra_hcl[i, j, 1]
            dLhcl = (citra_hcl[i, j, 2] - HCL[2]) ** 2
            Dhcl = np.sqrt(dLhcl + abs(dHhcl))
            if Dhcl <= Th:
                cit_hasilHCL[i, j, :] = Im[i, j, :].astype(np.uint8)

    # Tampilkan hasil
    plt.figure(figsize=(6, 6))
    plt.imshow(cit_hasilRGB)
    plt.title('Segmentasi RGB')
    plt.axis('off')
    plt.show()

    plt.figure(figsize=(6, 6))
    plt.imshow(cit_hasilHSV)
    plt.title('Segmentasi HSV')
    plt.axis('off')
    plt.show()

    plt.figure(figsize=(6, 6))
    plt.imshow(cit_hasilHCL)
    plt.title('Segmentasi HCL')
    plt.axis('off')
    plt.show()
