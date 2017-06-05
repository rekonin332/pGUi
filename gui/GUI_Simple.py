'''
Created on 2017年5月25日

@author: Todd
'''

import tkinter as tk
from tkinter import Menu
from tkinter import ttk # themed Tk
from textwrap import fill
from turtledemo.nim import Stick

#funtions

#exit GUI clearly

def _quit():
    win.quit()
    win.destroy()
    exit()
    
win = tk.Tk()

win.title("Python Projects")

# creating a Menu Bar
menuBar = Menu()
win.config(menu=menuBar)

# add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File",menu=fileMenu)


helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About")

# Tab control / notebook introduce here 

tabControl = ttk.Notebook(win)   #create tab control

tab1 = ttk.Frame(tabControl)      #Create a tab
tabControl.add(tab1, text='Tab 1') #add the tab

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand=1, fill="both") # pack to make visible

# we are creating a container frame to hold all other widgets
weather_conditions_frame = ttk.LabelFrame(tab1, text=' Current Weather Conditions ')

#using the tkinter grid layout manager
weather_conditions_frame.grid(column=0, row=0, padx=8, pady=14)

#Adding a Label
ttk.Label(weather_conditions_frame, text=" Location:").grid(column=0, row=0, sticky='w')


#start GUI

win.mainloop()

    