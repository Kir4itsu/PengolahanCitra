import numpy as np

def rgb2hsv_gambar(R, G=None, B=None):
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

    # Inisialisasi matriks untuk H, S, dan V
    H = np.zeros((N, M))
    S = np.zeros((N, M))
    V = np.zeros((N, M))

    # Konversi warna dari RGB ke HSV
    for n in range(N):
        for m in range(M):
            r = R[n, m]
            g = G[n, m]
            b = B[n, m]

            # Hitung Max, Min, dan Chroma
            Max = max(r, g, b)
            Min = min(r, g, b)
            C = Max - Min

            # Hitung Value (V)
            V[n, m] = Max

            # Hitung Saturation (S)
            if Max == Min:
                S[n, m] = 0
            else:
                S[n, m] = C

            # Hitung Hue (H)
            if Max == Min:
                H[n, m] = 0
            elif r == Max:
                H[n, m] = (g - b) / C
            elif g == Max:
                H[n, m] = 2 + (b - r) / C
            else:  # b == Max
                H[n, m] = 4 + (r - g) / C

            # Konversi Hue ke dalam radian
            H[n, m] = H[n, m] * np.pi / 3

    # Gabungkan hasil ke dalam satu array jika hanya satu output yang diminta
    return H, S, V

# Contoh penggunaan:
# Jika memanggil dengan satu parameter gambar 3D
# H, S, V = rgb2hsv_gambar(gambar_rgb_anda)
# Atau jika memiliki tiga array terpisah
# H, S, V = rgb2hsv_gambar(R, G, B)