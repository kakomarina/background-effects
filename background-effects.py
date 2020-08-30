#
# Old main : before the graphic interface was implemented
# File out of date
#

import numpy as np
import imageio
from skimage.color import rgb2gray
from triangle_threshold import *
from change_background_thresholding import *


filename = str(input())
# reading original image, where the effect is going to be apllied,
# and grayscale, where the segmentation is going to take place
input_img = imageio.imread(filename)
img = imageio.imread(filename)
img_gray = imageio.imread(filename, as_gray=True)
# using median filter to pre-process the image and reduce noise
img_gray_preprocessed = median_filter(img_gray)
# calculating histogram so it's possible to use histogram based thresholding methods

boolean_img = triangle_threshold(img_gray_preprocessed)

bg_name = str(input())
bg = imageio.imread(bg_name)

img_bg_changed = change_background(
    img, bg, boolean_img)

imageio.imwrite("output_img.png", img_bg_changed)
