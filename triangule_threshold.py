import numpy as np
import math


def get_y(xi, peak, end, hist):
    m = (hist[end] - hist[peak]) / (end - peak)
    b = hist[end] - m * end

    return (m * xi) + b


def get_x(yi, peak, end, hist):
    m = (hist[end] - hist[peak]) / (end - peak)
    b = hist[end] - m * end

    return (yi - b)/m


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


def triangule_threshold(img):
    hist = histogram(img)
    peak = np.argmax(hist)

    if 255 - peak > peak:
        # peak está mais perto do começo
        end = 254
        index = np.arange(peak + 1, end)
    else:
        # peak está mais perto do final
        end = 0
        index = np.arange(0, peak)

    d_max = -1
    split = 0

    for i in index:
        y1 = abs(get_y(i, peak, end, hist))
        x1 = abs(get_x(hist[i], peak, end, hist))

        a = y1 - hist[i]
        b = x1 - i
        c = float(math.sqrt(a**2 + b**2))
        d = (float(b)*float(a))/c

        if d > d_max:
            d_max = a
            split = i

    return (img) > split
