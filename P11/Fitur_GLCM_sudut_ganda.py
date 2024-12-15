import numpy as np

def fitur_glcm_sudut_ganda(CM):
    """
    Calculate texture features from the Gray-Level Co-occurrence Matrix 
    using a multi-angle approach.
    
    Parameters:
    CM (numpy.ndarray): Co-occurrence matrix
    
    Returns:
    tuple: Calculated texture features
    """
    # Normalize the co-occurrence matrix
    P = CM / np.sum(CM)
    N, M = P.shape
    
    # Initialize features
    cont, diss, hom, ent, enr = 0, 0, 0, 0, 0
    mean = 0
    
    # Calculate features
    for n in range(N):
        mX = 0
        for m in range(M):
            mX += P[n, m]
            diss += abs(n - m) * P[n, m]  # Dissimilarity
            cont += (n - m) ** 2 * P[n, m]  # Contrast
            hom += P[n, m] / (1 + abs(n - m))  # Homogeneity
            enr += P[n, m] ** 2  # Energy
            
            if P[n, m] > 0:
                ent -= P[n, m] * np.log10(P[n, m])  # Entropy
        
        mean += n * mX  # Mean
    
    # Calculate variance
    var = 0
    for n in range(N):
        mX = 0
        for m in range(M):
            mX += P[n, m]
            var += ((n - mean) ** 2) * mX
    
    # Calculate correlation
    Corr = 0
    for n in range(N):
        for m in range(M):
            Corr += (n * m * P[n, m])
    
    Corr = (Corr - mean ** 2) / var if var != 0 else 0
    
    return mean, var, cont, diss, hom, Corr, ent, enr

# Test case
def main():
    # Test case matrix
    CM = np.array([
        [0, 1, 2],
        [1, 0, 1],
        [2, 1, 0]
    ])
    
    # Calculate GLCM features with multi-angle approach
    mean, var, cont, diss, hom, Corr, ent, enr = fitur_glcm_sudut_ganda(CM)
    
    print("GLCM Features:")
    print(f"Mean: {mean}")
    print(f"Variance: {var}")
    print(f"Contrast: {cont}")
    print(f"Dissimilarity: {diss}")
    print(f"Homogeneity: {hom}")
    print(f"Correlation: {Corr}")
    print(f"Entropy: {ent}")
    print(f"Energy: {enr}")
