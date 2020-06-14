import numpy as np
import imageio


def histogram(img, no_levels=255):
    hist = np.zeros(no_levels).astype(int)

    # computes for all levels in the range
    for i in range(no_levels):
        # the np.where() function returns the indices for all coordinates
        # in some array matching the condition. In this case, all pixels
        # that have value 'i'
        pixels_value_i = np.where(img == i)

        # by counting how many coordinates the np.where function returned,
        # we can assign it at the respective histogram bin
        # this is done by getting the size of the vector of coordinates
        hist[i] = pixels_value_i[0].shape[0]

    return hist


def median_filter(img, k=5):
    a = k // 2
    r = np.zeros(img.shape)
    for x in np.arange(a, img.shape[0] - a + 1):
        for y in np.arange(a, img.shape[1] - a + 1):
            med_region = np.median(img[x - a: x + a + 1, y - a: y + a + 1])
            r[x, y] = med_region

    return r


filename = str(input())
# reading original image, where the effect is going to be apllied,
# and grayscale, where the segmentation is going to take place
input_img = imageio.imread(filename)
grayscale_img = imageio.imread(filename, as_gray=True)
# using median filter to pre-process the image and reduce noise
grayscale_img = median_filter(grayscale_img)
# calculating histogram so it's possible to use histogram based thresholding methods
hist = histogram(grayscale_img)
peak = np.argmax(hist)

if 255 - pico > pico:
    # pico está mais perto do começo
    end = 254
    index = np.arange(pico, 254)
else:
    # pico está mais perto do final
    index = np.arange(0, pico)
    end = 0


def get_y(xi):
    m = (hist_a[end] - hist_a[pico]) / (end - pico)
    b = hist_a[end] - m * end

    return (m * xi) + b


h = -1
split = 0
for i in index:
    y1 = abs(get_y(i))
    h_temp = y1 - hist_a[i]

    if h_temp > h:
        h = h_temp
        split = i

map = grayscale_img > split