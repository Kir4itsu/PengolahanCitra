import numpy as np
import matplotlib.pyplot as plt

LCH_solid = np.ones((300, 300, 3), dtype=np.uint8) * 128
Lab_solid = np.ones((300, 300, 3), dtype=np.uint8) * 128
LCH_Edge = np.ones((300, 300, 3), dtype=np.uint8) * 128
Lab_Edge = np.ones((300, 300, 3), dtype=np.uint8) * 128

sudut = -5 * np.pi / 6
Th = 0.00885645
MAT = np.array([[0.412453, 0.357580, 0.180423],
                [0.212671, 0.715160, 0.072169],
                [0.019334, 0.119193, 0.950227]])

for b in range(256):
    for g in range(256):
        for r in range(256):
            RGB = np.array([r / 255, g / 255, b / 255])
            XYZ = MAT @ RGB
            X = XYZ[0] / 0.950456
            Y = XYZ[1]
            Z = XYZ[2] / 1.088754
            XT = X > Th
            YT = Y > Th
            ZT = Z > Th
            fX = np.where(XT, X**(1/3), (7.787 * X + 16/116))
            fY = np.where(YT, Y**(1/3), (7.787 * Y + 16/116))
            fZ = np.where(ZT, Z**(1/3), (7.787 * Z + 16/116))
            L = 116 * fY - 16
            al = 500 * (fX - fY)
            bl = 200 * (fY - fZ)
            C = np.sqrt(al**2 + bl**2)
            H = np.arctan2(bl, al)
            j = 125 + int(round(C * np.cos(H)))
            i = 200 - int(round(C * np.sin(H) + L))
            jj = 150 + int(round(al + bl * np.sin(sudut)))
            ii = 200 - int(round(bl * np.sin(sudut) - L))
            if 0 <= i < 300 and 0 <= j < 300:
                LCH_solid[i, j] = [r, g, b]
            if 0 <= ii < 300 and 0 <= jj < 300:
                Lab_solid[ii, jj] = [r, g, b]
            if ((r == b and g == 255) or (r == g and b == 255) or (b == g and r == 255) or
                (r == 255 and g == 255) or (g == 255 and b == 255) or (b == 255 and r == 255) or
                (b == 0 and g == 0) or (r == 0 and g == 0) or (b == 0 and r == 0) or
                (b == r and g == 0) or (r == g and b == 0) or (b == g and r == 0) or
                (b == 255 and r == 0) or (b == 255 and g == 0) or (g == 255 and r == 0) or
                (g == 255 and b == 0) or (r == 255 and b == 0) or (r == 255 and g == 0) or
                (r == g and g == b)):
                if 0 <= i < 300 and 0 <= j < 300:
                    LCH_Edge[i, j] = [r, g, b]
                if 0 <= ii < 300 and 0 <= jj < 300:
                    Lab_Edge[ii, jj] = [r, g, b]

plt.figure(1)
plt.imshow(LCH_solid)
plt.title("Ruang Warna LCH 3-D Solid")
plt.axis('off')

plt.figure(2)
plt.imshow(Lab_solid)
plt.title("Ruang Warna Lab 3-D Solid")
plt.axis('off')

plt.figure(3)
plt.imshow(LCH_Edge)
plt.title("Ruang Warna LCH 3-D Edge")
plt.axis('off')

plt.figure(4)
plt.imshow(Lab_Edge)
plt.title("Ruang Warna Lab 3-D Edge")
plt.axis('off')

plt.show()