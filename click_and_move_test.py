# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:22:19 2020

@author: Fuso
"""

from tkinter import  *

tk =Tk()
canvas = Canvas(tk, width=500,  height=500,)
tk.title("Drawing")

def clickL(event):
    xbat = -1
    print(xbat)
    xmove(bat,xbat)
    


def clickR(event):
    xbat = 1
    print(xbat)
    xmove(bat,xbat)

def xmove(object,x):
    canvas.move(object,x,0)


canvas.bind("<Button-1>", clickL)
canvas.bind("<Button-3>", clickR)


canvas.pack()

bat =  canvas.create_rectangle(150, 500,  300,  480, fill="black")


canvas.mainloop()