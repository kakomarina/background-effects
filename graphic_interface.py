# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:19:20 2020

@author: Fuso
"""

 
import tkinter as tkr
from PIL import ImageTk,Image 
import numpy as np
import imageio

def motion(event):
    x, y = event.x, event.y
    if(onClick):
        print('clicado {}, {}'.format(x, y))
    else:
        print('solto {}, {}'.format(x, y))
    
def callback(event):
    global onClick
    onClick = True
    print("clicked at", event.x, event.y)

def onClickFalse(event):
    global onClick
    onClick = False


#filename = str(input()).rstrip()#reads Image File
input_img = imageio.imread("girl1.jpg")
img = np.array(input_img)
img = img.astype(np.int32) #casting para realizar as funcoes
#creates mold for final image
altura, largura, profundidade = img.shape

onClick = False
root = tkr.Tk()
canvas = tkr.Canvas(root, width=largura, height=altura)
canvas.grid()
img = ImageTk.PhotoImage(Image.open("girl1.jpg"))  
canvas.create_image(0, 0, anchor=NW, image=img) 
root.bind('<Motion>', motion)
root.bind('<Button-1>', callback)
root.bind('<ButtonRelease-1>', onClickFalse)


root.mainloop()