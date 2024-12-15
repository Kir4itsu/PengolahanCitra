import cv2
import numpy as np
import matplotlib.pyplot as plt

def regiongsplit():
    # Load image
    image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'
    I = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE).astype(np.float32)  # Load as grayscale
    if I is None:
        print("Error: Gambar tidak ditemukan atau gagal dibaca.")
        return

    plt.figure(1)
    plt.imshow(I, cmap='gray')
    plt.title('Citra Asli')
    plt.axis('off')
    plt.show()

    M, N = I.shape
    Th = 47  # Threshold
    Dim = 2  # Minimum dimension for splitting

    # Perform region splitting
    Im, S = imsplit(I, Dim, Th)

    plt.figure(2)
    plt.imshow(Im, cmap='gray')
    plt.title('Citra Hasil')
    plt.axis('off')
    plt.show()

def imsplit(I, Dim, Th):
    L = 1
    i = 0
    px = 0  # Set to 0-based index for Python
    py = 0  # Set to 0-based index for Python
    S = []  # List for region processing
    original_M, original_N = I.shape  # Use these as fixed original dimensions
    M, N = int(original_M), int(original_N)  # Ensure M and N are integers

    if Dim >= min(M, N):
        Dim = min(M, N) // 2

    while i < L:
        P = None
        if isinstance(M, int) and isinstance(N, int) and M > Dim and N > Dim:  # Ensure M and N are integers
            Im = I[int(py):int(py+M), int(px):int(px+N)]
            M1, N1 = Im.shape
            Dimy = M1 // 2
            Dimx = N1 // 2
            # If not homogeneous, divide the region
            if (np.max(Im) - np.min(Im)) > Th:
                P = np.array([
                    [py, px, Dimy, Dimx],
                    [py, px + Dimx, Dimy, N - Dimx],
                    [py + Dimy, px, M - Dimy, Dimx],
                    [py + Dimy, px + Dimx, M - Dimy, N - Dimx]
                ])

        if P is not None and P.size > 0:
            if i == 0:
                S.append(P)
                i += 1
            else:
                S = S[:i] + [P] + S[i+1:]
        else:
            i += 1

        if i < L:
            M = int(S[i][2])  # Ensure M is an integer
            N = int(S[i][3])  # Ensure N is an integer
            px = int(S[i][1])  # Ensure px is an integer
            py = int(S[i][0])  # Ensure py is an integer

        L = len(S)

    # Map the regions formed to the original image
    for region in S:
        for sub_region in region:
            m, n = int(sub_region[0]), int(sub_region[1])
            Vy, Vx = int(sub_region[2]), int(sub_region[3])
            I[m:m+Vy, n] = 255
            I[m, n:n+Vx] = 255

    I[-1, :] = 255
    I[:, -1] = 255
    return I, S

# Call the main function
regiongsplit()
