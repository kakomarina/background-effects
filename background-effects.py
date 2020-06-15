import numpy as np
import imageio
from triangule_threshold import *
from change_background import *


filename = str(input())
# reading original image, where the effect is going to be apllied,
# and grayscale, where the segmentation is going to take place
input_img = imageio.imread(filename)
grayscale_img = imageio.imread(filename, as_gray=True)
# using median filter to pre-process the image and reduce noise
grayscale_img_preprocessed = median_filter(grayscale_img)
# calculating histogram so it's possible to use histogram based thresholding methods

boolean_img = triangule_threshold(grayscale_img_preprocessed)

bg_name = str(input())
bg_grayscale = imageio.imread(bg_name, as_gray=True)

img_bg_changed = change_background(
    grayscale_img_preprocessed, bg_grayscale, boolean_img)

imageio.imwrite("output_img.png", img_bg_changed)
