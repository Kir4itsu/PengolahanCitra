import numpy as np
import matplotlib.pyplot as plt

# Initialize color palettes
R = np.zeros((256, 30, 3), dtype=np.uint8)
G = np.zeros((256, 30, 3), dtype=np.uint8)
B = np.zeros((256, 30, 3), dtype=np.uint8)
Ir = np.zeros(256, dtype=int)
Ig = np.zeros(256, dtype=int)
Ib = np.zeros(256, dtype=int)

Q = 10  # Set quantization level
hitam = 15  # Set intensity of black
Th = (255 - hitam) / (Q - 1)  # Calculate threshold value

# Populate the color palettes
for i in range(255, hitam - 1, -1):
    Indeks = int(np.ceil((i - hitam) / Th))  # Calculate index value
    Ir[256 - i] = Indeks
    Ig[256 - i] = Indeks
    Ib[256 - i] = Indeks
    
    WarnaIndeks = int(Indeks * Th)  # Calculate intensity for color index
    R[256 - i, :, 0] = WarnaIndeks
    G[256 - i, :, 1] = WarnaIndeks
    B[256 - i, :, 2] = WarnaIndeks

# Display the color palettes using matplotlib
plt.figure(1)
plt.title("Palette R")
plt.imshow(R)
plt.axis('off')  # Hide axes

plt.figure(2)
plt.title("Palette G")
plt.imshow(G)
plt.axis('off')

plt.figure(3)
plt.title("Palette B")
plt.imshow(B)
plt.axis('off')

plt.show()