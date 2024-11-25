import numpy as np
import matplotlib.pyplot as plt

# Initialize the base color matrix for display (solid color background)
RGB_solid = np.full((425, 425, 3), 230, dtype=np.uint8)

sudut = -5 * np.pi / 6  # Angle for display transformation
Q = 8  # Quantization level
Th = round(255 / Q)  # Threshold for quantization range

# Iterate over blue, green, and red intensities from 0 to 255
for b in range(1, 256):
    for g in range(1, 256):
        for r in range(1, 256):
            # Convert 3D coordinates to 2D display coordinates
            j = 150 + int(g + (b * np.sin(sudut)))
            i = 280 - int(b * np.sin(sudut) + r)
            
            # Create a white separating line between two palettes
            if (r % Th == 0 or g % Th == 0 or b % Th == 0 or 
                (r == 255 and g == 255) or (r == 255 and b == 255) or (b == 255 and g == 255)):
                RGB_solid[i, j, 0] = 0
                RGB_solid[i, j, 1] = 0
                RGB_solid[i, j, 2] = 0
            else:  # Form the 3D color map
                RGB_solid[i, j, 0] = int(np.ceil(r / Th) * Th)
                RGB_solid[i, j, 1] = int(np.ceil(g / Th) * Th)
                RGB_solid[i, j, 2] = int(np.ceil(b / Th) * Th)

# Display the 3D color map as a 2D RGB plot
plt.figure(figsize=(8, 8))
plt.title("3D Color Map Projection")
plt.imshow(RGB_solid)
plt.axis('off')  # Hide axes for a cleaner display
plt.show()