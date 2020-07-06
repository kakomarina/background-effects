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

def background_effects():
    global filename, bg_filename, tag
    #filename = str(input())
   # reading original image, where the effect is going to be apllied,
    # and grayscale, where the segmentation is going to take place
    input_img = imageio.imread(filename)
    img = imageio.imread(filename)
    img_gray = imageio.imread(filename, as_gray=True)
    # using median filter to pre-process the image and reduce noise
    img_gray_preprocessed = median_filter(img_gray)
    # calculating histogram so it's possible to use histogram based thresholding methods

    boolean_img = triangle_threshold(img_gray_preprocessed)

    #bg_name = str(input())
    bg = imageio.imread(bg_filename)

    img_bg_changed = change_background(img, bg, boolean_img)

    imageio.imwrite("output_img.png", img_bg_changed)
    tag =1


def motion(event):
    x, y = event.x, event.y
  #  if(onClick):
    print('{}, {}'.format(x, y))
 #   else:
 #       print('solto {}, {}'.format(x, y))

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

def callback(event):
#    global onClick
#    onClick = True
    print("clicked at", event.x, event.y)
    global x, y, colors, tag
    x = event.x
    y = event.y
    im = Image.open("girl1.jpg")
    pixel = im.load()
    colors.append(pixel[x,y])
    print(colors)
    

def destroy_root(root):
    root.destroy()
    
def onClickFalse(event):
    global onClick
    onClick = False

def image_interface():
    global filename, colors

    root = tkr.Tk()
    tag = 0
  
    canvas = tkr.Canvas(root, width=largura, height=altura)
    canvas.grid()
    img = ImageTk.PhotoImage(Image.open(filename))  
    canvas.create_image(0, 0, anchor="nw", image=img) 
    root.bind('<Motion>', motion)
    root.bind('<Button-1>', callback)
    w = tkr.Button(root, text = "Concluir", command = background_effects, height = 2, width = 30)
    w.grid(row=altura,column=0)
    if tag == 1:
        print("acabou")
        destroy_root(root)
    
    root.mainloop()
    
def getInput():

    global img_name, bg_name
    img = img_name.get()
    bg = bg_name.get()
    print(img, bg)
    destroy_root(root)
    image_interface()
   

#filename = str(input()).rstrip()#reads Image File
filename = "girl1.jpg"
bg_filename = "bg_mata.jpg"

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
small_font = ('Verdana',"10")
large_font = ('Verdana',"13")

#top text: instructions about the program
w = tkr.Label(root, text = "Como Usar", font='bold')
w.pack(pady=(10,0))
w = tkr.Label(root, text="Insira o nome do arquivo da imagem desejada.\n Depois que a imagem aparecer, clique em todas as área\n que você deseja que apareça na foto com o fundo \nalterado e aperte no botão Concluir. A foto\n estará salva no seu computador com o nome output.png",anchor=tkr.NW, font=small_font)
w.pack()

#first input: name of the image with the object to be used in new background
#text
w = tkr.Label(root, text="Insira o nome do arquivo da imagem desejada.",font=large_font)
w.pack(pady=(50,0))
#input
img_name = w = tkr.Entry(root,width="30", font=large_font)
w.pack(ipady=10, pady=(10,10))

#second input: name of the new background file
#text
w = tkr.Label(root, text="Insira o nome do arquivo do plano de fundo desejada.",font=large_font)
w.pack()
#input
bg_name = w = tkr.Entry(root,width="30", font=large_font)
w.pack(ipady=10, pady=(10,10))

w = tkr.Button(root, text = "Enviar", command = getInput, height = 2, width = 30)
w.pack()
root.mainloop()