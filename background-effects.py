import numpy as np
import imageio
from triangule_threshold import *


filename = str(input())
# reading original image, where the effect is going to be apllied,
# and grayscale, where the segmentation is going to take place
input_img = imageio.imread(filename)
grayscale_img = imageio.imread(filename, as_gray=True)
# using median filter to pre-process the image and reduce noise
grayscale_img_preprocessed = median_filter(grayscale_img)
# calculating histogram so it's possible to use histogram based thresholding methods

boolean_img = triangule_threshold(grayscale_img_preprocessed)
