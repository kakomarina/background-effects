#Testing Clustering technique for image segmentation

import imageio
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

def normalize(img, max_value, min_value): 
    return ((img - np.min(img)) * (max_value - min_value)) / (
        (np.max(img) - np.min(img)) + min_value)


def clustering(img):
    img = img / 255  # dividing by 255 to bring the pixel values between 0 and 1
    img_n = img.reshape(img.shape[0]*img.shape[1], img.shape[2])

    kmeans = KMeans(n_clusters=5, random_state=0).fit(img_n)
    img2show = kmeans.cluster_centers_[kmeans.labels_]

    cluster_img = img2show.reshape(img.shape[0], img.shape[1], img.shape[2])

    return normalize(cluster_img, 255, 0)
