import cv2
import numpy as np
import matplotlib.pyplot as plt

def region_split_merge():
    # Load image
    image_path = r'C:\Users\Administrator\Pictures\Screenshots\Screenshot 2024-10-15 122623.png'
    I = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE).astype(np.float32)  # Load as grayscale
    if I is None:
        print("Error: Image not found or failed to read.")
        return

    plt.figure(1)
    plt.imshow(I, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    plt.show()

    M, N = I.shape
    Th = 47  # Threshold
    Dim = 2  # Minimum dimension for splitting

    # Perform region splitting and merging
    Im, S = imsplitmerge1(I, Dim, Th)

    plt.figure(2)
    plt.imshow(Im, cmap='gray')
    plt.title('Segmented Image')
    plt.axis('off')
    plt.show()

def imsplitmerge1(I, Dim, Th):
    L = 1
    i = 0
    px = 0  # 0-based index for Python
    py = 0  # 0-based index for Python
    S = []  # List for region processing
    original_M, original_N = I.shape
    M, N = int(original_M), int(original_N)

    if Dim >= min(M, N):
        Dim = min(M, N) // 2

    while i < L:
        P = None
        if M > Dim and N > Dim:
            P = quadtree(I, I[int(py):int(py+M), int(px):int(px+N)], px, py, Th)

        if P is not None and isinstance(P, np.ndarray) and P.size > 0:
            if i == 0:
                S.append(P)
                i += 1
            else:
                S = S[:i] + [P] + S[i+1:]
        else:
            i += 1

        if i < L:
            M = int(S[i][2])
            N = int(S[i][3])
            px = int(S[i][1])
            py = int(S[i][0])

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

def quadtree(Im, sub_I, px, py, Th):
    M, N = sub_I.shape
    Dimy = M // 2
    Dimx = N // 2
    S = []

    if (np.max(sub_I) - np.min(sub_I)) > Th:
        Max1 = np.max(sub_I[:Dimy, :Dimx])
        Min1 = np.min(sub_I[:Dimy, :Dimx])
        Max2 = np.max(sub_I[:Dimy, Dimx:])
        Min2 = np.min(sub_I[:Dimy, Dimx:])
        Max3 = np.max(sub_I[Dimy:, :Dimx])
        Min3 = np.min(sub_I[Dimy:, :Dimx])
        Max4 = np.max(sub_I[Dimy:, Dimx:])
        Min4 = np.min(sub_I[Dimy:, Dimx:])

        if Max1 - Min2 <= Th and Max2 - Min1 <= Th and Max2 - Min4 <= Th and Max4 - Min2 <= Th:
            S = np.array([
                [py, px, Dimy, Dimx],
                [py, px + Dimx, 0, N - Dimx],
                [py + Dimy, px, M - Dimy, Dimx],
                [py + Dimy, px + Dimx, M - Dimy, 0]
            ])
        elif Max4 - Min2 <= Th and Max2 - Min4 <= Th and Max3 - Min4 <= Th and Max4 - Min3 <= Th:
            S = np.array([
                [py, px, Dimy, Dimx],
                [py, px + Dimx, Dimy, N - Dimx],
                [py + Dimy, px, M - Dimy, Dimx],
                [py + Dimy, px + Dimx, 0, 0]
            ])
        elif Max3 - Min1 <= Th and Max1 - Min3 <= Th and Max3 - Min4 <= Th and Max4 - Min3 <= Th:
            S = np.array([
                [py, px, Dimy, Dimx],
                [py, px + Dimx, Dimy, N - Dimx],
                [py + Dimy, px, M - Dimy, 0],
                [py + Dimy, px + Dimx, 0, N - Dimx]
            ])
        elif Max3 - Min1 <= Th and Max1 - Min3 <= Th and Max1 - Min2 <= Th and Max2 - Min1 <= Th:
            S = np.array([
                [py, px, Dimy, Dimx],
                [py, px + Dimx, 0, N - Dimx],
                [py + Dimy, px, M - Dimy, 0],
                [py + Dimy, px + Dimx, M - Dimy, N - Dimx]
            ])
        elif Max1 - Min2 <= Th and Max2 - Min1 <= Th:
            S = np.array([
                [py, px, Dimy, Dimx],
                [py, px + Dimx, 0, N - Dimx],
                [py + Dimy, px, M - Dimy, Dimx],
                [py + Dimy, px + Dimx, M - Dimy, N - Dimx]
            ])
        elif Max2 - Min4 <= Th and Max4 - Min2 <= Th:
            S = np.array([
                [py, px, Dimy, Dimx],
                [py, px + Dimx, Dimy, N - Dimx],
                [py + Dimy, px, M - Dimy, Dimx],
                [py + Dimy, px + Dimx, M - Dimy, 0]
            ])
        elif Max3 - Min4 <= Th and Max4 - Min3 <= Th:
            S = np.array([
                [py, px, Dimy, Dimx],
                [py, px + Dimx, Dimy, N - Dimx],
                [py + Dimy, px, M - Dimy, Dimx],
                [py + Dimy, px + Dimx, 0, N - Dimx]
            ])
        elif Max3 - Min1 <= Th and Max1 - Min3 <= Th:
            S = np.array([
                [py, px, Dimy, Dimx],
                [py, px + Dimx, Dimy, N - Dimx],
                [py + Dimy, px, M - Dimy, 0],
                [py + Dimy, px + Dimx, M - Dimy, N - Dimx]
            ])
        if not S:
            S = np.array([
                [py, px, Dimy, Dimx],
                [py, px + Dimx, Dimy, N - Dimx],
                [py + Dimy, px, M - Dimy, Dimx],
                [py + Dimy, px + Dimx, M - Dimy, N - Dimx]
            ])
    return S

# Call the main function
region_split_merge()
