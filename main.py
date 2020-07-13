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
from change_background_clustering import *
from clusteringimgseg import *


# destroy interface
def destroy_root(root):
    root.destroy()


# close last interface page
def close_interface():
    global root2
    destroy_root(root2)

# changes background and gets final image (interfaces pages 1 and 2)


def background_effects():
    global filename, bg_filename, root2, root1, canvas, colors, largura, altura, large_font, img_clustered

    colors.pop()  # takes off last color of array colors (button "Finished" color)

    # warns user tht the program is loading
    label = tkr.Label(root1, text="Loading...", font=large_font)
    label.grid(row=altura, column=0)
    root1.update()

    img_original = imageio.imread(filename)
    bg = Image.open(bg_filename)

    # changes background
    print("Changing background...")
    img_bg_changed = change_background(
        img_original, bg, img_clustered.astype(np.uint8), colors)
    imageio.imwrite("output_img.png", img_bg_changed.astype(np.uint8))

    destroy_root(root1)  # destroy interface page 1

    # saves outputfile
    output_filename = "output_img.png"
    imageio.imwrite(output_filename, img_bg_changed)

    # INTERFACE PAGE 2 (shows image with changed backround)
    root2 = tkr.Tk()  # master of interface page 2

    # defines dimensions to interface
    canvas = tkr.Canvas(root2, width=largura, height=altura)
    canvas.grid()

    # shows final image
    final_img = ImageTk.PhotoImage(Image.open(output_filename))
    canvas.create_image(0, 0, anchor="nw", image=final_img)

    # createsclose button -> calls close_interface
    w = tkr.Button(root2, text="Finish",
                   command=close_interface, height=2, width=30)
    w.grid(row=altura, column=0)

    root2.mainloop()  # loop of interface page 2

# function created to track the mouse in the interface, not necessary but great for debug
# def motion(event):
#    x, y = event.x, event.y
#   print("{}, {}".format(x, y))

# function used to get pixel color name


def getColor(event):
    global filename

    #print("clicked at", event.x, event.y)
    global x, y, colors, tag

    # get location of clicked pixel
    x = event.x
    y = event.y

    im = Image.open("clustered_img.png")  # opens clustered image
    pixel = im.load()  # gets pixel color
    colors.append(pixel[x, y])  # insert color in colors array
    print(colors)


# INTERFACE PAGE 1
def image_interface():
    global root, filename, colors, root1, canvas, img_clustered, altura, largura, profundidade

    label = tkr.Label(
        root, text="Generating clustered image...", font=large_font)
    label.pack(pady=(10, 10))
    root.update()

    img_original = imageio.imread(filename)

    # gets image dimensions and stores height, width and depth (colors of the image)
    temporary_img_original = np.array(img_original)
    temporary_img_original = temporary_img_original.astype(np.int32)
    altura, largura, profundidade = temporary_img_original.shape

    print("Generating clustered image...")
    img_clustered = clustering(img_original)  # generates clustered image
    imageio.imwrite("clustered_img.png", img_clustered.astype(
        np.uint8))  # saves file with clustered image

    destroy_root(root)  # destroys interface page 0

    root1 = tkr.Tk()  # master of interface page 1

    # defines interface dimensions
    canvas = tkr.Canvas(root1, width=largura, height=altura)
    canvas.grid()

    clust_img = ImageTk.PhotoImage(Image.open(
        "clustered_img.png"))  # opens clustered image
    # sets image in interface
    canvas.create_image(0, 0, anchor="nw", image=clust_img)

    # root1.bind("<Motion>", motion) #gets mouse location in the interface
    # if the mouse is clicked, is called a function (getColor) to get the clicked pixel color
    root1.bind("<Button-1>", getColor)

    # creates finish button -> calls background_effects
    w = tkr.Button(root1, text="Finish",
                   command=background_effects, height=2, width=30)
    w.grid(row=altura, column=0)

    root1.mainloop()  # loop of interface page 1


def getInput():  # gets input: filename (file name of person or object image) and bg_filename (file name of backgroud image)

    global filename, bg_filename

    filename = filename.get()
    bg_filename = bg_filename.get()

    image_interface()  # calls next interface page


# INTERFACE PAGE 0: INSTRUCTIONS AND INPUTS
# global variables: masters for each interface page, canva of page 1, original image, clustered image, selected colors of clusteres image, font sizes

root1 = 0  # master of interface page 1
root2 = 0  # master of interface page 2
canvas = 0  # canva of interface page 1
main_img = 0
img_clustered = 0
largura = altura = profundidade = 0
colors = []
small_font = ("Verdana", "10")
large_font = ("Verdana", "13")

# begining of interface page 0

root = tkr.Tk()  # root is the master of interface page 0
root.geometry("500x500")  # defining dimension of interface

# top text: instructions about the program
w = tkr.Label(root, text="Instructions", font="bold")
w.pack(pady=(10, 0))
w = tkr.Label(
    root,
    text="Please write the name of the main image\n After the image appears, please click all areas\n that you wish to replace with the new background \n in the final image and press Finish. \n The image will be saved in your computer with the name output.png",
    anchor=tkr.NW,
    font=small_font,
)
w.pack()

# first input: name of the image with the object to be used in new background
w = tkr.Label(
    root, text="Please write the name of the main image file", font=large_font)
w.pack(pady=(50, 0))  # packs info text
filename = w = tkr.Entry(root, width="30", font=large_font)
w.pack(ipady=10, pady=(10, 10))  # packs input

# second input: name of the new background file
w = tkr.Label(
    root, text="Please write the name of the background image file", font=large_font)
w.pack()  # packs info text
bg_filename = w = tkr.Entry(root, width="30", font=large_font)
w.pack(ipady=10, pady=(10, 10))  # packs input

# submit button -> calls function getInpu
w = tkr.Button(root, text="Finish", command=getInput, height=2, width=30)
w.pack()  # packs button

root.mainloop()  # loop of interface page 0
