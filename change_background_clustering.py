import numpy as np
import matplotlib.pyplot as plt
from skimage import transform


# resize background to the same size of the given image
def resize_background(background, M, N, C):

    background_resized = np.zeros((N, M, C))
    background_resized = background.resize((N, M))

    return background_resized


def change_background(img_original, background, clustered_img, colors_to_change):
    print(colors_to_change)
    N, M, C = img_original.shape

    # background in the same size of the given image
    background = resize_background(background, N, M, C)
    # copy of the original image
    img_bg_changed = np.array(img_original, copy=True)

    for color in colors_to_change:
        # where the clustered image matches with the given color, change to the background pixel
        # the other positions keep the img_bg_changed pixel color
        img_bg_changed = np.where(
            clustered_img == color, background, img_bg_changed)

    return img_bg_changed
