import numpy as np

def calculate_co_occurrence_matrix(I, angle=0):
    I = np.array(I)
    N, M = I.shape  # Size of the input matrix
    G = np.max(I) - np.min(I) + 1  # Range of values in the matrix
    CM = np.zeros((G, G), dtype=int)  # Initialize co-occurrence matrix with zeros

    # Set direction based on the specified angle
    if angle == 0:  # 0 degrees
        dx = 1
        dy = 0
        N0 = 0
        N1 = N
        M0 = 0
        M1 = M - 1
    elif angle == 45:  # 45 degrees
        dx = 1
        dy = -1
        N0 = 1
        N1 = N
        M0 = 0
        M1 = M - 1
    elif angle == 90:  # 90 degrees
        dx = 0
        dy = -1
        N0 = 1
        N1 = N
        M0 = 0
        M1 = M
    elif angle == 135:  # 135 degrees
        dx = -1
        dy = -1
        N0 = 1
        N1 = N
        M0 = 1
        M1 = M
    else:
        raise ValueError("Invalid angle. Supported angles are 0, 45, 90, 135 degrees.")

    # Compute the co-occurrence matrix
    for n in range(N0, N1):
        for m in range(M0, M1):
            if 0 <= n + dy < N and 0 <= m + dx < M:  # Check bounds
                CM[I[n, m], I[n + dy, m + dx]] += 1

    return CM

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
