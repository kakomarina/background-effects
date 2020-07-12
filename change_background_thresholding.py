import numpy as np
import matplotlib.pyplot as plt
from skimage import transform


def resize_background(background, N, M, C):
    background_resized = np.zeros((N, M, C))
    for i in range(C):
        background_resized[:, :, i] = np.resize(background[:, :, i], (N, M))

    return background_resized


def left_to_right(img, background, bool_img):
    N, M = bool_img.shape

    for x in range(0, N):
        y = 0
        while y < M and bool_img[x][y] == False:
            y += 1
        for y in range(y, M):
            if bool_img[x][y] == False:
                break
            else:
                img[x][y] = background[x][y]

    return img


def right_to_left(img, background, bool_img):
    N, M = bool_img.shape

    for x in range(N - 1, 0, -1):
        y = M - 1
        while y >= 0 and bool_img[x][y] == False:
            y -= 1
        for y in range(y, 0, -1):
            if bool_img[x][y] == False:
                break
            else:
                img[x][y] = background[x][y]

    return img


def change_background(img, background, bool_img):

    N, M, C = img.shape
    background = resize_background(background, N, M, C)
    img = left_to_right(img, background, bool_img)
    img = right_to_left(img, background, bool_img)

    return img
