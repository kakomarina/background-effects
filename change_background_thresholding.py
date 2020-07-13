import numpy as np
import matplotlib.pyplot as plt
from skimage import transform
from PIL import Image
import imageio


def resize_background(background, M, N, C):

    background_resized = np.zeros((N, M, C))
    background_resized = background.resize((N, M))

    return background_resized


# go from left to right, changing the background
def left_to_right(img, background, bool_img):
    N, M = bool_img.shape

    for x in range(0, N):
        y = 0
        # ignoring the first part for better results
        while y < M and bool_img[x][y] == False:
            y += 1
        for y in range(y, M):
            if bool_img[x][y] == False:
                break
            else:
                img[x][y] = background[x][y]

    return img


# go from right to left, changing the background
def right_to_left(img, background, bool_img):
    N, M = bool_img.shape

    for x in range(N - 1, 0, -1):
        y = M - 1
        # ignoring the first part for better results
        while y >= 0 and bool_img[x][y] == False:
            y -= 1
        for y in range(y, 0, -1):
            if bool_img[x][y] == False:
                break
            else:
                img[x][y] = background[x][y]

    return img


def change_background_thresholding(img, background, bool_img):

    N, M, C = img.shape
    background = resize_background(background, N, M, C)

    imageio.imwrite("output_converting.jpg", background)

    background1 = imageio.imread("output_converting.jpg")

    img = left_to_right(img, background1, bool_img)
    img = right_to_left(img, background1, bool_img)

    return img
