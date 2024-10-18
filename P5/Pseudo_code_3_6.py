# HCL Color Space Visualization

import numpy as np
import matplotlib.pyplot as plt

HCL_solid = np.ones((275, 400, 3), dtype=np.uint8) * 128
HCL_Edge = np.ones((275, 400, 3), dtype=np.uint8) * 128

gamma = 10

for b in range(256):
    for g in range(256):
        for r in range(256):
            Max = max(r, g, b)
            Min = min(r, g, b)
            Q = 1.0 if Max == 0 else np.exp((Min * gamma) / (Max * 100.0))
            L = (Q * Max + (Q - 1.0) * Min) / 2.0
            rg = r - g
            gb = g - b
            C = (abs(b - r) + abs(rg) + abs(gb)) * Q / 3.0
            H = np.arctan2(gb, rg)
            if C == 0:
                H = 0.0
            elif rg >= 0 and gb >= 0:
                H = 2 * H / 3
            elif rg >= 0 and gb < 0:
                H = 4 * H / 3
            elif rg < 0 and gb >= 0:
                H = np.pi + 4 * H / 3
            elif rg < 0 and gb < 0:
                H = 2 * H / 3 - np.pi
            j = 200 + int(round(C * np.cos(H)))
            i = 250 - int(round(C * np.sin(H) / 4.0 + L))
            if 0 <= i < 275 and 0 <= j < 400:
                HCL_solid[i, j] = [r, g, b]
                if ((r == b and g == 255) or (r == g and b == 255) or (b == g and r == 255) or
                    (r == 255 and g == 255) or (g == 255 and b == 255) or (b == 255 and r == 255) or
                    (b == 0 and g == 0) or (r == 0 and g == 0) or (b == 0 and r == 0) or
                    (b == r and g == 0) or (r == g and b == 0) or (b == g and r == 0) or
                    (b == 255 and r == 0) or (b == 255 and g == 0) or (g == 255 and r == 0) or
                    (g == 255 and b == 0) or (r == 255 and b == 0) or (r == 255 and g == 0) or
                    (r == g and g == b)):
                    HCL_Edge[i, j] = [r, g, b]

plt.figure(1)
plt.imshow(HCL_solid)
plt.title("Ruang Warna HCL 3-D Solid")
plt.axis('off')

plt.figure(2)
plt.imshow(HCL_Edge)
plt.title("Ruang Warna HCL 3-D Edge")
plt.axis('off')

plt.show()