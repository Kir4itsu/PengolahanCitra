import numpy as np
import matplotlib.pyplot as plt

# Initialize the display matrix
HSV_solid = np.full((375, 575, 3), 230, dtype=np.float32)

q = 6
Th = round(255/q)
Thpi0 = np.pi/20
Thpi = (np.pi - Thpi0)/10

# First pass: calculate color points
for b in range(256):
    for g in range(256):
        for r in range(256):
            # Calculate HSV values
            Max = max(r, max(g, b))
            Min = min(r, min(g, b))
            C = Max - Min
            V = Max  # Value/Luminance

            # Calculate Saturation
            S = C if Max != Min else 0

            # Calculate Hue
            if Max == Min:
                H = 0
            elif r == Max:
                H = ((g - b)/C)
            elif g == Max:
                H = 2 + (b - r)/C
            elif b == Max:
                H = 4 + (r - g)/C

            H = H * np.pi/3

            # Convert to 2D coordinates
            j = 285 + round((S * np.cos(H)))
            i = 350 - round((S * np.sin(H)/4.0 + V))

            # Store RGB values
            HSV_solid[i, j, 0] = r
            HSV_solid[i, j, 1] = g
            HSV_solid[i, j, 2] = b

# Second pass: mark boundary points
MinH = -360
for b in range(256):
    for g in range(256):
        for r in range(256):
            # Calculate HSV values
            Max = max(r, max(g, b))
            Min = min(r, min(g, b))
            C = Max - Min
            V = Max  # Value/Luminance

            # Calculate Saturation
            S = C if Max != Min else 0

            # Calculate Hue
            if Max == Min:
                H = 0
            elif r == Max:
                H = ((g - b)/C)
            elif g == Max:
                H = 2 + (b - r)/C
            elif b == Max:
                H = 4 + (r - g)/C

            H = H * np.pi/3
            MinH = max(MinH, H)

            # Convert to 2D coordinates
            j = 285 + int(S * np.cos(H))
            i = 350 - int(S * np.sin(H)/4.0 + V)

            # Mark boundary conditions
            if ((C % Th == 0 or (H % Thpi <= 0.012)) and 
                C == V and ((H >= -np.pi/3 and H < -0.15) or H >= np.pi + 0.1)) or \
               (V == 255 and (C % Th == 0 or C == 255)) or \
               ((H % Thpi <= 0.012) and V == 255 and (H >= 0.2 or H <= -0.2)):
                HSV_solid[i, j, 0] = 0
                HSV_solid[i, j, 1] = 0
                HSV_solid[i, j, 2] = 0

# Display the result
plt.figure(1)
plt.imshow(HSV_solid.astype(np.uint8))
plt.axis('off')
plt.show()