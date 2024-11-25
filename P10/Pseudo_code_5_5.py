import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fungsi bantu konversi RGB ke HCL
def RGB2HCL(rgb):
    rgb = rgb / 255.0
    max_c = np.max(rgb)
    min_c = np.min(rgb)
    l = (max_c + min_c) / 2
    if max_c == min_c:
        h = 0
        c = 0
    else:
        d = max_c - min_c
        c = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
        if max_c == rgb[0]:
            h = (rgb[1] - rgb[2]) / d + (6 if rgb[1] < rgb[2] else 0)
        elif max_c == rgb[1]:
            h = (rgb[2] - rgb[0]) / d + 2
        else:
            h = (rgb[0] - rgb[1]) / d + 4
        h /= 6
    return np.array([h * 360, c, l])

# Fungsi region growing untuk gambar berwarna dalam ruang HCL
def regiongrowingHCL(Im, S, Th):
    Ref = RGB2HCL(S)
    HRef, CRef, LRef = Ref
    HCL = np.apply_along_axis(RGB2HCL, 2, Im)
    m, n = Im.shape[:2]
    RG = np.zeros_like(Im, dtype=np.float32)

    for i in range(m):
        for j in range(n):
            dH = HCL[i, j, 0] - HRef
            C = HCL[i, j, 1]
            dC = C**2 + CRef**2
            dL = (HCL[i, j, 2] - LRef)**2
            Dhcl = np.sqrt(dL + dC - 2 * CRef * C * np.cos(dH))
            if Dhcl <= Th:
                RG[i, j, :] = Im[i, j, :]

    return RG

# Fungsi region growing untuk gambar grayscale
def regiongrowingGray(Im, S, Th):
    m, n = Im.shape
    RG = np.zeros_like(Im, dtype=np.float32)

    for i in range(m):
        for j in range(n):
            if abs(Im[i, j] - S) <= Th:
                RG[i, j] = Im[i, j]

    return RG

# Main code
image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'
Im = cv2.imread(image_path)

if Im is None:
    print("Error: Gambar tidak ditemukan atau gagal dibaca.")
else:
    Im = cv2.cvtColor(Im, cv2.COLOR_BGR2RGB).astype(np.float32)
    plt.figure(1)
    plt.imshow(Im.astype(np.uint8))
    plt.title('Citra Asli')
    plt.axis('off')
    plt.show()

    # Contoh titik seed
    x, y = 100, 100
    RGB = Im[y, x, :]
    Th = 47  # Threshold

    if len(Im.shape) == 3:
        RG = regiongrowingHCL(Im, RGB, Th)
    else:
        RG = regiongrowingGray(Im, RGB, Th)

    plt.figure(2)
    plt.imshow(RG.astype(np.uint8))
    plt.title('Region Growing')
    plt.axis('off')
    plt.show()
