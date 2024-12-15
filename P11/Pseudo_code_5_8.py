import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_texture_features(image_path):
    # Load image
    I = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Load as grayscale
    if I is None:
        print("Error: Image not found or failed to read.")
        return
    
    N, M = I.shape  # Image dimensions
    
    plt.figure()
    plt.imshow(I, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    plt.show()
    
    # Compute histogram
    hist = cv2.calcHist([I], [0], None, [256], [0, 256])
    
    hist = hist / (N * M)  # Normalize the histogram
    
    # Calculate mean
    mean = 0
    for zi in range(256):
        mean += zi * hist[zi][0]
    
    # Calculate second-order moment (variance) and standard deviation
    moment2 = 0
    for zi in range(256):
        moment2 += ((zi - mean) ** 2) * hist[zi][0]
    moment2 = np.sqrt(moment2)
    
    # Calculate smoothness (or roughness)
    R = moment2 ** 2 / (1 + moment2 ** 2)
    
    # Calculate skewness (moment of order 3)
    S = 0
    for zi in range(256):
        S += ((zi - mean) ** 3) * hist[zi][0]
    
    # Calculate uniformity
    U = 0
    for zi in range(256):
        U += hist[zi][0] ** 2
    
    # Calculate entropy
    Ent = 0
    for zi in range(256):
        if hist[zi][0] > 0:
            Ent -= hist[zi][0] * np.log2(hist[zi][0])
    
    # Print results
    print(f"Mean: {mean}")
    print(f"Second-order Moment (Standard Deviation): {moment2}")
    print(f"Smoothness (Roughness): {R}")
    print(f"Uniformity: {U}")
    print(f"Entropy: {Ent}")

# Replace with the path to your local image
image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'
calculate_texture_features(image_path)