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
from change_background import *


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
    global filename, bg_filename, root2, root1, canvas, largura, altura, large_font, main_img

    # reading original image, where the effect is going to be apllied,
    # and grayscale, where the segmentation is going to take place

    print(large_font)
    label = tkr.Label(root1, text="Processando...", font=large_font)
    label.grid(row=altura, column=0)
    root1.update()

    img_original = imageio.imread(filename)
    img_gray = imageio.imread(filename, as_gray=True)

    # using median filter to pre-process the image and reduce noise
    img_gray_preprocessed = median_filter(img_gray)

    boolean_img = triangle_threshold(img_gray_preprocessed)

    bg = imageio.imread(bg_filename)

    img_bg_changed = change_background(img_original, bg, boolean_img)

    imageio.imwrite("output_img.png", img_bg_changed)

    destroy_root(root1)

    # fogo = imageio.imread("bg_fogo.jpg")
    output_filename = "output_img_teste_real.png"
    imageio.imwrite(output_filename, img_bg_changed)

    root2 = tkr.Tk()

    canvas = tkr.Canvas(root2, width=largura, height=altura)
    canvas.grid()
    final_img = ImageTk.PhotoImage(Image.open(output_filename))
    canvas.create_image(0, 0, anchor="nw", image=final_img)
    w = tkr.Button(root2, text="Concluir", command=close_interface, height=2, width=30)
    w.grid(row=altura, column=0)

    root2.mainloop()


def motion(event):
    x, y = event.x, event.y
    #  if(onClick):
    print("{}, {}".format(x, y))


#   else:
#       print('solto {}, {}'.format(x, y))


def callback(event):
    #    global onClick
    #    onClick = True
    print("clicked at", event.x, event.y)
    global x, y, colors, tag
    x = event.x
    y = event.y
    im = Image.open("girl1.jpg")
    pixel = im.load()
    colors.append(pixel[x, y])
    print(colors)


def image_interface():
    global filename, colors, root1, canvas, main_img

    root1 = tkr.Tk()

    canvas = tkr.Canvas(root1, width=largura, height=altura)
    canvas.grid()
    img = ImageTk.PhotoImage(Image.open(filename))
    main_img = ImageTk.PhotoImage(Image.open(filename))
    canvas.create_image(0, 0, anchor="nw", image=img)
    root1.bind("<Motion>", motion)
    root1.bind("<Button-1>", callback)
    w = tkr.Button(root1, text="Concluir", command=background_effects, height=2, width=30)
    w.grid(row=altura, column=0)

    root1.mainloop()


def getInput():

    global img_name, bg_name
    img = img_name.get()
    bg = bg_name.get()
    print(img, bg)
    destroy_root(root)
    image_interface()


# filename = str(input()).rstrip()#reads Image File
filename = "girl1.jpg"
bg_filename = "bg_mata.jpg"

# declaring global variables (different master for each graphic interface), global canva
root1 = 0
root2 = 0
canvas = 0
main_img = 0

input_img = imageio.imread(filename)
img = np.array(input_img)
img = img.astype(np.int32)  # casting para realizar as funcoes

# creates mold for final image
"""background_effects(filename)"""
altura, largura, profundidade = img.shape
colors = []
# onClick = False
root = tkr.Tk()

root.geometry("500x500")
small_font = ("Verdana", "10")
large_font = ("Verdana", "13")

# top text: instructions about the program
w = tkr.Label(root, text="Como Usar", font="bold")
w.pack(pady=(10, 0))
w = tkr.Label(
    root,
    text="Insira o nome do arquivo da imagem desejada.\n Depois que a imagem aparecer, clique em todas as áreas\n que você deseja que apareça na foto com o fundo \nalterado e aperte no botão Concluir. A foto\n estará salva no seu computador com o nome output.png",
    anchor=tkr.NW,
    font=small_font,
)
w.pack()

# first input: name of the image with the object to be used in new background
# text
w = tkr.Label(root, text="Insira o nome do arquivo da imagem desejada.", font=large_font)
w.pack(pady=(50, 0))
# input
img_name = w = tkr.Entry(root, width="30", font=large_font)
w.pack(ipady=10, pady=(10, 10))

# second input: name of the new background file
# text
w = tkr.Label(root, text="Insira o nome do arquivo do plano de fundo desejado.", font=large_font)
w.pack()
# input
bg_name = w = tkr.Entry(root, width="30", font=large_font)
w.pack(ipady=10, pady=(10, 10))

w = tkr.Button(root, text="Enviar", command=getInput, height=2, width=30)
w.pack()
root.mainloop()
