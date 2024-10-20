import numpy as np

def rgb2lab_gambar(R, G=None, B=None):
    # Jika input adalah satu gambar (array 3D), pisahkan ke komponen R, G, dan B
    if G is None and B is None:
        B = R[:, :, 2].astype(np.float64)
        G = R[:, :, 1].astype(np.float64)
        R = R[:, :, 0].astype(np.float64)
    else:
        R = R.astype(np.float64)
        G = G.astype(np.float64)
        B = B.astype(np.float64)

    # Skala R, G, B jika mereka berada dalam rentang 0-255
    if R.max() > 1.0 or G.max() > 1.0 or B.max() > 1.0:
        R = R / 255.0
        G = G / 255.0
        B = B / 255.0

    # Threshold dan matriks konversi
    Th = 0.008856
    M, N = R.shape
    s = M * N

    # Bentuk ulang R, G, B dan buat matriks RGB
    RGB = np.vstack([R.flatten(), G.flatten(), B.flatten()])

    # Konversi dari ruang warna RGB ke XYZ
    MAT = np.array([
        [0.412453, 0.357580, 0.180423],
        [0.212671, 0.715160, 0.072169],
        [0.019334, 0.119193, 0.950227]
    ])
    XYZ = MAT @ RGB

    # Normalisasi cahaya putih untuk referensi D65
    X = XYZ[0, :] / 0.950456
    Y = XYZ[1, :]
    Z = XYZ[2, :] / 1.088754

    # Kondisi threshold
    TX = X > Th
    TY = Y > Th
    TZ = Z > Th

    # Fungsi f(T)
    fTX = np.where(TX, X ** (1 / 3), 7.787 * X + 16 / 116)
    fTY = np.where(TY, Y ** (1 / 3), 7.787 * Y + 16 / 116)
    fTZ = np.where(TZ, Z ** (1 / 3), 7.787 * Z + 16 / 116)

    # Hitung L, a, b dan bentuk ulang ke ukuran gambar
    L = (116 * fTY - 16).reshape(M, N)
    a = (500 * (fTX - fTY)).reshape(M, N)
    b = (200 * (fTY - fTZ)).reshape(M, N)

    # Gabungkan hasil ke dalam satu array jika hanya satu output yang diminta
    return L, a, b

# Contoh penggunaan:
# Jika memanggil dengan satu parameter gambar 3D
# L, a, b = rgb2lab_gambar(gambar_rgb_anda)
# Atau jika memiliki tiga array terpisah
# L, a, b = rgb2lab_gambar(R, G, B)