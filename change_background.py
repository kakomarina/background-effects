import numpy as np
import matplotlib.pyplot as plt
from skimage import transform

def resizeBackground(background,N,M):
    background_resized = np.resize(background,(N,M))
    return background_resized

def left_to_right(img, background, bool_img):
    N, M = bool_img.shape

    for x in range(0, N):
        y = 0
        while y < M and bool_img[x][y] == False:
            y += 1
        for y in range(y, M):
            if bool_img[x][y] == False:
                break
            else:
                img[x][y] = background[x][y]

    return img


def right_to_left(img, background, bool_img):
    N, M = bool_img.shape

    for x in range(N - 1, 0, -1):
        y = M - 1
        while y >= 0 and bool_img[x][y] == False:
            y -= 1
        for y in range(y, 0, -1):
            if bool_img[x][y] == False:
                break
            else:
                img[x][y] = background[x][y]

    return img



#<<<<<<< Updated upstream
#    img = left_to_right(img, background, bool_img) # NAO SEI PRA QUE ISSO SERVE, TAVA NO MERGE Q DEU CONFLITO
#=======
def change_background(img, background, bool_img):
    
    N, M = img.shape
    background = resizeBackground(background,N,M)
    img = left_to_rigth(img, background, bool_img)
    img = right_to_left(img, background, bool_img)

    return img
