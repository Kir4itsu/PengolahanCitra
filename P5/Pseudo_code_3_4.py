# HSV Color Space Visualization

import numpy as np
import matplotlib.pyplot as plt

HSV_solid = np.ones((375, 575, 3), dtype=np.uint8) * 128
HSV_Edge = np.ones((375, 570, 3), dtype=np.uint8) * 128

for b in range(256):
    for g in range(256):
        for r in range(256):
            Max = max(r, g, b)
            Min = min(r, g, b)
            C = Max - Min
            V = Max
            S = 0 if Max == Min else C
            if Max == Min:
                H = 0
            elif r == Max:
                H = (g - b) / C
            elif g == Max:
                H = 2 + (b - r) / C
            else:
                H = 4 + (r - g) / C
            H = H * np.pi / 3
            j = 285 + int(S * np.cos(H))
            i = 350 - int(S * np.sin(H) / 4.0 + V)
            if 0 <= i < 375 and 0 <= j < 575:
                HSV_solid[i, j, 0] = r
                HSV_solid[i, j, 1] = g
                HSV_solid[i, j, 2] = b
                if ((r == b and g == 255) or (r == g and b == 255) or (b == g and r == 255) or
                    (r == 255 and g == 255) or (g == 255 and b == 255) or (b == 255 and r == 255) or
                    (b == 0 and g == 0) or (r == 0 and g == 0) or (b == 0 and r == 0) or
                    (b == r and g == 0) or (r == g and b == 0) or (b == g and r == 0) or
                    (b == 255 and r == 0) or (b == 255 and g == 0) or (g == 255 and r == 0) or
                    (g == 255 and b == 0) or (r == 255 and b == 0) or (r == 255 and g == 0) or
                    (r == g and g == b)):
                    HSV_Edge[i, j, 0] = r
                    HSV_Edge[i, j, 1] = g
                    HSV_Edge[i, j, 2] = b

plt.figure(1)
plt.imshow(HSV_solid)
plt.title("Ruang Warna HSV 3-D Solid")
plt.axis('off')

plt.figure(2)
plt.imshow(HSV_Edge)
plt.title("Ruang Warna HSV 3-D Edge")
plt.axis('off')

plt.show()