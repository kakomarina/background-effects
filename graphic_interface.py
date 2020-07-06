# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:19:20 2020

@author: Fuso
"""

 
import tkinter as tkr
from PIL import ImageTk,Image 
import numpy as np
import imageio
from skimage.color import rgb2gray
from triangle_threshold import *
from change_background import *

def background_effects(filename):
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
    
    img_bg_changed = change_background(img, bg, boolean_img)

    imageio.imwrite("output_img.png", img_bg_changed)


def motion(event):
    x, y = event.x, event.y
  #  if(onClick):
    print('{}, {}'.format(x, y))
 #   else:
 #       print('solto {}, {}'.format(x, y))

def callback(event):
#    global onClick
#    onClick = True
    print("clicked at", event.x, event.y)
    global x, y
    x = event.x
    y = event.y
    im = Image.open("girl1.jpg")
    pixel = im.load()
    colors.append(pixel[x,y])
    print(colors)
    

def onClickFalse(event):
    global onClick
    onClick = False

def image_interface():
    global filename
    root = tkr.Tk()
    canvas = tkr.Canvas(root, width=largura+60, height=altura)
    canvas.grid()
    img = ImageTk.PhotoImage(Image.open(filename))  
    canvas.create_image(0, 0, anchor="nw", image=img) 
    color_frame = tkr.Frame(root, bg = "red")
    root.bind('<Motion>', motion)
    root.bind('<Button-1>', callback)
    w = tkr.Button(root, bg="blue")
    root.mainloop()
  
def destroy_root(root):
    root.destroy()
    
def getInput():

    global e
    a = e.get()
    print(a)
    destroy_root(root)
    image_interface()
   

#filename = str(input()).rstrip()#reads Image File
filename = "girl1.jpg"
input_img = imageio.imread(filename)
img = np.array(input_img)
img = img.astype(np.int32) #casting para realizar as funcoes
#creates mold for final image
'''background_effects(filename)'''
altura, largura, profundidade = img.shape
colors = []
#onClick = False
root = tkr.Tk()
##### codigo ficava aqui
root.geometry("500x500")
large_font = ('Verdana',"13")
w = tkr.Label(root, text="Insira o nome do arquivo da imagem desejada",font=large_font)
w.pack(pady=(180, 0))
e = w= tkr.Entry(root,width="30", font=large_font)
w.pack(ipady=10, pady=(10,10))
w = tkr.Button(root, text = "Enviar", command = getInput, height = 2, width = 30)
w.pack()
root.mainloop()