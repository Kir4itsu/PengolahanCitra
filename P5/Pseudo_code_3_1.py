# RGB Color Space Visualization
import numpy as np
import matplotlib.pyplot as plt

RGB_solid = np.ones((425, 425, 3), dtype=np.uint8) * 128
RGB_Edge = np.ones((425, 425, 3), dtype=np.uint8) * 128
Imax = 255
sudut = -5 * np.pi / 6

for b in range(Imax + 1):
    for g in range(Imax + 1):
        for r in range(Imax + 1):
            j = 150 + int(g + (b * np.sin(sudut)))
            i = 280 - int(b * np.sin(sudut) + r)
            if 0 <= i < 425 and 0 <= j < 425:
                RGB_solid[i, j, 0] = r
                RGB_solid[i, j, 1] = g
                RGB_solid[i, j, 2] = b
                if ((r == b and g == Imax) or (r == g and b == Imax) or (b == g and r == Imax) or
                    (r == Imax and g == Imax) or (g == Imax and b == Imax) or (b == Imax and r == Imax) or
                    (b == 0 and g == 0) or (r == 0 and g == 0) or (b == 0 and r == 0) or
                    (b == r and g == 0) or (r == g and b == 0) or (b == g and r == 0) or
                    (b == Imax and r == 0) or (b == Imax and g == 0) or (g == Imax and r == 0) or
                    (g == Imax and b == 0) or (r == Imax and b == 0) or (r == Imax and g == 0) or
                    (r == g and g == b)):
                    RGB_Edge[i, j, 0] = r
                    RGB_Edge[i, j, 1] = g
                    RGB_Edge[i, j, 2] = b

plt.figure(1)
plt.imshow(RGB_solid)
plt.title("Ruang Warna RGB 3-D Solid")
plt.axis('off')

plt.figure(2)
plt.imshow(RGB_Edge)
plt.title("Ruang Warna RGB 3-D Edge")
plt.axis('off')

plt.show()