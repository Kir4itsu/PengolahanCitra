# HSL Color Space Visualization

import numpy as np
import matplotlib.pyplot as plt

HSL_solid = np.ones((325, 350, 3), dtype=np.uint8) * 128
HSL_Edge = np.ones((325, 350, 3), dtype=np.uint8) * 128

for b in range(256):
    for g in range(256):
        for r in range(256):
            Max = max(r, g, b)
            Min = min(r, g, b)
            C = Max - Min
            L = (Max + Min) / 2.0
            if Max == Min:
                S = 0
            elif L >= 127:
                S = C / (2 * L / 255)
            else:
                S = C / (2 - 2 * L / 255)
            if C == 0:
                H = 0
            elif r == Max:
                H = ((g - b) / C) % 6
            elif g == Max:
                H = 2 + (b - r) / C
            else:
                H = 4 + (r - g) / C
            H = H * np.pi / 3
            j = 175 + int((S / 2) * np.cos(H))
            i = 285 - int((S / 2) * np.sin(H) / 8.0 + L)
            if 0 <= i < 325 and 0 <= j < 350:
                HSL_solid[i, j, 0] = r
                HSL_solid[i, j, 1] = g
                HSL_solid[i, j, 2] = b
                if ((r == b and g == 255) or (r == g and b == 255) or (b == g and r == 255) or
                    (r == 255 and g == 255) or (g == 255 and b == 255) or (b == 255 and r == 255) or
                    (b == 0 and g == 0) or (r == 0 and g == 0) or (b == 0 and r == 0) or
                    (b == r and g == 0) or (r == g and b == 0) or (b == g and r == 0) or
                    (b == 255 and r == 0) or (b == 255 and g == 0) or (g == 255 and r == 0) or
                    (g == 255 and b == 0) or (r == 255 and b == 0) or (r == 255 and g == 0) or
                    (r == g and g == b)):
                    HSL_Edge[i, j, 0] = r
                    HSL_Edge[i, j, 1] = g
                    HSL_Edge[i, j, 2] = b

plt.figure(1)
plt.imshow(HSL_solid)
plt.title("Ruang Warna HSL 3-D Solid")
plt.axis('off')

plt.figure(2)
plt.imshow(HSL_Edge)
plt.title("Ruang Warna HSL 3-D Edge")
plt.axis('off')

plt.show()