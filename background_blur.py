#
# Background blur function 
# 
# Unfortunately this function was not used in the final results
#


import numpy as np
import math
from copy import copy


def gaussian_kernel_equation(x, sigma):
    return (1.0 / (2.0 * np.pi * (np.power(sigma, 2)))) * (
        np.exp(-(np.power(x, 2)) / (2.0 * (np.power(sigma, 2))))
    )


def create_spatial_gaussian_component(sigmaS, n):
    spatial_gaussian = np.zeros((n, n), dtype=np.float32)

    for x in range(0, n):
        for y in range(0, n):
            spatial_gaussian[x][y] = gaussian_kernel_equation(
                euclidian_distance(int((n - 1) / 2), int((n - 1) / 2), x, y), sigmaS
            )

    return spatial_gaussian


def euclidian_distance(cx, cy, x, y):
    return np.sqrt((x - cx) ** 2 + (y - cy) ** 2)


def bilateral_filter(f, spatial_gaussian, sigmaR, bool_img):
    N, M = f.shape
    n, m = spatial_gaussian.shape

    a = int((n - 1) / 2)
    b = int((m - 1) / 2)

    # new image to store filtered pixels
    g = copy(f)

    # calculating padded image
    padded = np.pad(f, max(a, b), mode="constant")

    # for every pixel
    for x in range(a, N + a):
        y1 = 0
        while y1 < M and x < N and bool_img[x][y1] == False:
            y1 += 1
        for y in range(y1, M + b):
            if x < N and y < M and bool_img[x][y] == False:
                break
            # passo 1: calcular a range Gaussian
            range_gaussian = np.zeros((n, m), dtype=np.float32)
            Wp = 0
            If = 0.0
            # para cada vizinho
            for xi in range(x - a, x + a + 1):
                for yi in range(y - b, y + b + 1):
                    # calcular a range gaussian
                    range_gaussian[xi - (x - a)][yi - (y - b)] = gaussian_kernel_equation(
                        (padded[xi][yi] * 1.0) - (padded[x][y] * 1.0), sigmaR
                    )
                    # calcular wi para o pixel correspondente
                    wi = (
                        range_gaussian[xi - (x - a)][yi - (y - b)]
                        * spatial_gaussian[xi - (x - a)][yi - (y - b)]
                    )
                    Wp = float(Wp + wi)
                    If = If + float(wi * padded[xi][yi])
            g[x - a][y - b] = int(If / Wp)

    return g


def background_blur(img, bool_img, n=5, sigmaS=150.0, sigmaR=150.0):

    spatial_gaussian = create_spatial_gaussian_component(sigmaS, n)
    output_image = bilateral_filter(img, spatial_gaussian, sigmaR, bool_img)

    return output_image
