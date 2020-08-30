#
# Clustering Method
#

import imageio
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans, AffinityPropagation


# Normalization of the image so the image can be saved

def normalize(img, max_value, min_value):
    return ((img - np.min(img)) * (max_value - min_value)) / (
        (np.max(img) - np.min(img)) + min_value)

# Median filter for noise reduction

def median_filter(img, k):
    a = k // 2
    r = np.zeros(img.shape)
    for x in np.arange(a, img.shape[0] - a + 1):
        for y in np.arange(a, img.shape[1] - a + 1):
            med_region = np.median(img[x - a: x + a + 1, y - a: y + a + 1])
            r[x, y] = med_region

    return r

# Clustering method with a kmeans calculation

def clustering(img):
    img = img / 255  # dividing by 255 to bring the pixel values between 0 and 1
    #img = median_filter(img, 5)
    img_n = img.reshape(img.shape[0]*img.shape[1], img.shape[2])

    # kmeans = KMeans(n_clusters=5, random_state=0).fit(img_n) # number of clusters is 5
    affinity = AffinityPropagation().fit(img_n)
    # img2show = kmeans.cluster_centers_[kmeans.labels_]
    img2show = affinity.cluster_centers_[affinity.labels_]

    cluster_img = img2show.reshape(img.shape[0], img.shape[1], img.shape[2])

    return normalize(cluster_img, 255, 0)
