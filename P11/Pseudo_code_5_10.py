import numpy as np

def calculate_co_occurrence_matrix(I, angle=0):
    I = np.array(I)
    N, M = I.shape
    G = np.max(I) - np.min(I) + 1
    CM = np.zeros((G, G), dtype=int)

    # Set direction based on the specified angle
    if angle == 0:  # 0 degrees
        dx, dy = 1, 0
        N0, N1 = 0, N
        M0, M1 = 0, M - 1
    elif angle == 45:  # 45 degrees
        dx, dy = 1, -1
        N0, N1 = 1, N
        M0, M1 = 0, M - 1
    elif angle == 90:  # 90 degrees
        dx, dy = 0, -1
        N0, N1 = 1, N
        M0, M1 = 0, M
    elif angle == 135:  # 135 degrees
        dx, dy = -1, -1
        N0, N1 = 1, N
        M0, M1 = 1, M
    else:
        raise ValueError("Invalid angle. Supported angles are 0, 45, 90, and 135 degrees.")

    # Compute the co-occurrence matrix
    for n in range(N0, N1):
        for m in range(M0, M1):
            if 0 <= n + dy < N and 0 <= m + dx < M:
                CM[I[n, m], I[n + dy, m + dx]] += 1
                CM[I[n + dy, m + dx], I[n, m]] += 1  # Symmetric update

    return CM

def calculate_glcm_features(CM):
    CM_sum = np.sum(CM)
    if CM_sum == 0:
        return 0, 0, 0, 0, 0, 0, 0, 0
    CM = CM / CM_sum

    G = CM.shape[0]
    meanX, meanY, variance, contrast, dissimilarity, homogeneity, correlation = 0, 0, 0, 0, 0, 0, 0
    entropy, energy = 0, 0

    # Compute the mean of row and column indices
    meanX = np.sum([i * np.sum(CM[i, :]) for i in range(G)])
    meanY = np.sum([j * np.sum(CM[:, j]) for j in range(G)])

    # Compute features
    for i in range(G):
        for j in range(G):
            pij = CM[i, j]
            if pij > 0:
                entropy -= pij * np.log2(pij)
            contrast += (i - j) ** 2 * pij
            dissimilarity += abs(i - j) * pij
            homogeneity += pij / (1 + (i - j) ** 2)
            variance += ((i - meanX) * (j - meanY)) ** 2 * pij
            energy += pij ** 2
            if variance > 0:
                correlation += ((i - meanX) * (j - meanY) * pij) / variance

    return meanX, meanY, variance, contrast, dissimilarity, homogeneity, correlation, entropy, energy

# Example input matrix
I = [
    [1, 1, 5, 6, 8],
    [0, 0, 5, 7, 1],
    [4, 5, 7, 1, 2],
    [8, 5, 1, 2, 0]
]

# Calculate co-occurrence matrix for angle 0 degrees
CM = calculate_co_occurrence_matrix(I, angle=0)
print("Co-occurrence Matrix:")
print(CM)

# Calculate GLCM features
meanX, meanY, variance, contrast, dissimilarity, homogeneity, correlation, entropy, energy = calculate_glcm_features(CM)
print("\nGLCM Features:")
print(f"Mean (X-axis): {meanX}")
print(f"Mean (Y-axis): {meanY}")
print(f"Variance: {variance}")
print(f"Contrast: {contrast}")
print(f"Dissimilarity: {dissimilarity}")
print(f"Homogeneity: {homogeneity}")
print(f"Correlation: {correlation}")
print(f"Entropy: {entropy}")
print(f"Energy: {energy}")
