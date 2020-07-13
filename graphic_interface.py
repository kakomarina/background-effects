# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:36:26 2020

@author: Fuso
"""

import tkinter as tkr
from PIL import ImageTk, Image
import numpy as np
import imageio
from skimage.color import rgb2gray
from triangle_threshold import *
from change_background_clustering import *
from clusteringimgseg import *


def destroy_root(root):
    root.destroy()


def close_interface():
    global root2
    destroy_root(root2)


def clear(root):
    list = root.grid_slaves()
    for l in list:
        l.destroy()


def background_effects():
    global filename, bg_name, root2, root1, canvas, colors, largura, altura, large_font, img_clustered

    colors.pop()

    # reading original image, where the effect is going to be apllied,
    # and grayscale, where the segmentation is going to take place

    print(large_font)
    label = tkr.Label(root1, text="Loading...", font=large_font)
    label.grid(row=altura, column=0)
    root1.update()

    img_original = imageio.imread(filename)
    # img_gray = imageio.imread(filename, as_gray=True)

    # using median filter to pre-process the image and reduce noise
    # img_gray_preprocessed = median_filter(img_gray)

    # boolean_img = triangle_threshold(img_gray_preprocessed)

    # bg = imageio.imread(bg_name)
    bg = Image.open(bg_name)

    # print("Generating clustered image...")
    # img_clustered = clustering(img_original)
    # imageio.imwrite("clustered_img.jpg", img_clustered.astype(np.uint8))

    print("Changing background...")
    img_bg_changed = change_background(
        img_original, bg, img_clustered.astype(np.uint8), colors)
    imageio.imwrite("output_img.png", img_bg_changed.astype(np.uint8))

    destroy_root(root1)

    # fogo = imageio.imread("bg_fogo.jpg")
    output_filename = "output_img.png"
    imageio.imwrite(output_filename, img_bg_changed)

    root2 = tkr.Tk()

    canvas = tkr.Canvas(root2, width=largura, height=altura)
    canvas.grid()
    final_img = ImageTk.PhotoImage(Image.open(output_filename))
    canvas.create_image(0, 0, anchor="nw", image=final_img)
    w = tkr.Button(root2, text="Finish",
                   command=close_interface, height=2, width=30)
    w.grid(row=altura, column=0)

    root2.mainloop()


def motion(event):
    x, y = event.x, event.y
    #  if(onClick):
    print("{}, {}".format(x, y))


#   else:
#       print('solto {}, {}'.format(x, y))


def callback(event):
    global filename

    print("clicked at", event.x, event.y)
    global x, y, colors, tag
    x = event.x
    y = event.y
    im = Image.open("clustered_img.jpg")
    pixel = im.load()
    colors.append(pixel[x, y])
    print(colors)


def image_interface():
    global filename, colors, root1, canvas, img_clustered

    root1 = tkr.Tk()

    canvas = tkr.Canvas(root1, width=largura, height=altura)
    canvas.grid()

    img_original = imageio.imread(filename)
    # img = ImageTk.PhotoImage(Image.open(filename))
    print("Generating clustered image...")
    img_clustered = clustering(img_original)
    imageio.imwrite("clustered_img.jpg", img_clustered.astype(np.uint8))

    clust_img = ImageTk.PhotoImage(Image.open("clustered_img.jpg"))

    canvas.create_image(0, 0, anchor="nw", image=clust_img)
    root1.bind("<Motion>", motion)
    root1.bind("<Button-1>", callback)
    w = tkr.Button(root1, text="Finish",
                   command=background_effects, height=2, width=30)
    w.grid(row=altura, column=0)

    root1.mainloop()


def getInput():

    global img_name, bg_name, largura, altura, profundidade, filename

    img = img_name.get()
    bg = bg_name.get()
    filename = img
    bg_name = bg
    input_img = imageio.imread(filename)
    img = np.array(input_img)
    img = img.astype(np.int32)
    altura, largura, profundidade = img.shape

#    print(img, bg)

    destroy_root(root)
    image_interface()


# filename = str(input()).rstrip()#reads Image File

# filename = "girl1.jpg"
# bg_filename = "bg_mata.jpg"

# declaring global variables (different master for each graphic interface), global canva
root1 = 0
root2 = 0
canvas = 0
main_img = 0
img_clustered = 0

# input_img = imageio.imread(filename)
# img = np.array(input_img)
# img = img.astype(np.int32)  # casting para realizar as funcoes


# creates mold for final image
"""background_effects(filename)"""
# altura, largura, profundidade = img.shape
colors = []
# onClick = False
root = tkr.Tk()

root.geometry("500x500")
small_font = ("Verdana", "10")
large_font = ("Verdana", "13")

# top text: instructions about the program
w = tkr.Label(root, text="Instructions", font="bold")
w.pack(pady=(10, 0))
w = tkr.Label(
    root,
    text="Please write the name of the main image\n After the image appears, please click all areas\n that you wish to be shown in the final image \n with the new background and press Finish. \n The image will be saved in your computer with the name output.png",
    anchor=tkr.NW,
    font=small_font,


)
w.pack()

# first input: name of the image with the object to be used in new background
# text
w = tkr.Label(
    root, text="Please write the name of the main image file", font=large_font)
w.pack(pady=(50, 0))
# input
img_name = w = tkr.Entry(root, width="30", font=large_font)
w.pack(ipady=10, pady=(10, 10))

# second input: name of the new background file
# text
w = tkr.Label(
    root, text="Please write the name of the background image file", font=large_font)
w.pack()
# input
bg_name = w = tkr.Entry(root, width="30", font=large_font)
w.pack(ipady=10, pady=(10, 10))

w = tkr.Button(root, text="Finish", command=getInput, height=2, width=30)
w.pack()
root.mainloop()
