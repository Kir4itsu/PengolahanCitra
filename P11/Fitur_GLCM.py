import numpy as np

def calculate_glcm_features(CM):
    """
    Calculate texture features from the Gray-Level Co-occurrence Matrix.
    
    Parameters:
    CM (numpy.ndarray): Co-occurrence matrix
    
    Returns:
    tuple: Calculated texture features
    """
    # Normalize the co-occurrence matrix
    P = CM / np.sum(CM)  # Compute probabilities
    N, M = P.shape
    
    cont, diss, hom, ent, enr = 0, 0, 0, 0, 0
    meanX, meanY = 0, 0
    
    for n in range(N):
        mX, mY = 0, 0
        for m in range(M):
            mX += P[n, m]
            mY += P[m, n]
            diss += abs(n - m) * P[n, m]  # Dissimilarity
            cont += (n - m) ** 2 * P[n, m]  # Contrast
            hom += P[n, m] / (1 + abs(n - m))  # Homogeneity
            enr += P[n, m] ** 2  # Energy
            
            if P[n, m] > 0:
                ent -= P[n, m] * np.log10(P[n, m])  # Entropy
        
        meanX += n * mX  # Mean X
        meanY += n * mY  # Mean Y
    
    # Calculate variance
    varX, varY = 0, 0
    for n in range(N):
        mX, mY = 0, 0
        for m in range(M):
            mX += P[n, m]
            mY += P[m, n]
            varX += ((n - meanX) ** 2) * mX  # Variance X
            varY += ((n - meanY) ** 2) * mY  # Variance Y
    
    # Calculate correlation
    Corr = 0
    for n in range(N):
        for m in range(M):
            Corr += ((n - meanY) * (m - meanX) * P[n, m])
    
    if varX > 0 and varY > 0:
        Corr = Corr / (np.sqrt(varX) * np.sqrt(varY))
    else:
        Corr = 0
    
    return meanX, meanY, varX, varY, cont, diss, hom, ent, enr, Corr

# Test case
def main():
    CM = np.array([
        [0, 1, 2],
        [1, 0, 1],
        [2, 1, 0]
    ])
    
    meanX, meanY, varX, varY, cont, diss, hom, ent, enr, Corr = calculate_glcm_features(CM)
    
    print("GLCM Features:")
    print(f"Mean (X-axis): {meanX}")
    print(f"Mean (Y-axis): {meanY}")
    print(f"Variance (X-axis): {varX}")
    print(f"Variance (Y-axis): {varY}")
    print(f"Contrast: {cont}")
    print(f"Dissimilarity: {diss}")
    print(f"Homogeneity: {hom}")
    print(f"Entropy: {ent}")
    print(f"Energy: {enr}")
    print(f"Correlation: {Corr}")
