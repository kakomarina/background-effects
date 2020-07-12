import numpy as np
import matplotlib.pyplot as plt
from skimage import transform


def resize_background(background, N, M, C):
    background_resized = np.zeros((N, M, C))
    for i in range(C):
        background_resized[:, :, i] = np.resize(background[:, :, i], (N, M))

    return background_resized


def change_background(img_original, background, clustered_img, colors_to_change):

    N, M, C = img_original.shape
    background = resize_background(background, N, M, C)
    img_bg_changed = np.array(img_original, copy=True)

    for color in colors_to_change:
        img_bg_changed = np.where(
            clustered_img == color, background, img_bg_changed)

    return img_bg_changed
