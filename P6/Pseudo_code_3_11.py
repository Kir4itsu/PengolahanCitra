import numpy as np

def rgb2hcl_gambar(R, G=None, B=None):
    # Jika input adalah satu gambar (array 3D), pisahkan ke komponen R, G, dan B
    if G is None and B is None:
        B = R[:, :, 2].astype(np.float64)
        G = R[:, :, 1].astype(np.float64)
        R = R[:, :, 0].astype(np.float64)
    else:
        R = R.astype(np.float64)
        G = G.astype(np.float64)
        B = B.astype(np.float64)

    # Dapatkan ukuran gambar
    N, M = R.shape

    # Inisialisasi matriks untuk H, C, dan L
    H = np.zeros((N, M))
    C = np.zeros((N, M))
    L = np.zeros((N, M))

    # Set nilai gamma
    gamma = 30

    # Loop untuk setiap piksel dalam gambar
    for n in range(N):
        for m in range(M):
            r = R[n, m]
            g = G[n, m]
            b = B[n, m]

            # Hitung Max, Min, dan Q
            Max = max(r, g, b)
            Min = min(r, g, b)
            Q = 1.0 if Max == 0 else np.exp((Min * gamma) / (Max * 100.0))

            # Hitung Chroma (C) dan Lightness (L)
            rg = r - g
            gb = g - b
            C[n, m] = (abs(b - r) + abs(rg) + abs(gb)) * Q / 3.0
            L[n, m] = (Q * Max + (Q - 1.0) * Min) / 2.0

            # Hitung Hue (H)
            if rg == 0:
                H[n, m] = 0  # Menghindari pembagian dengan nol
            else:
                H[n, m] = np.arctan(gb / rg)

            # Kondisi untuk menentukan nilai H
            if C[n, m] == 0:
                H[n, m] = 0.0
            elif rg >= 0 and gb >= 0:
                H[n, m] = 2 * H[n, m] / 3
            elif rg >= 0 and gb < 0:
                H[n, m] = 4 * H[n, m] / 3
            elif rg < 0 and gb >= 0:
                H[n, m] = np.pi + 4 * H[n, m] / 3
            elif rg < 0 and gb < 0:
                H[n, m] = 2 * H[n, m] / 3 - np.pi

    # Gabungkan hasil ke dalam satu array jika hanya satu output yang diminta
    return H, C, L

# Contoh penggunaan:
# Jika memanggil dengan satu parameter gambar 3D
# H, C, L = rgb2hcl_gambar(gambar_rgb_anda)
# Atau jika memiliki tiga array terpisah
# H, C, L = rgb2hcl_gambar(R, G, B)