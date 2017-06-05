
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
weather_conditions_frame.grid(column=0, row=0, padx=8, pady=4)

#Adding a Label
ttk.Label(weather_conditions_frame, text="Location:").grid(column=0, row=0, sticky='E')



#---------------------------------------------------
city = tk.StringVar()
citySelected = ttk.Combobox(weather_conditions_frame, width=12, textvariable=city)
citySelected['values'] = ('Los Angeles', 'London', 'Rio de Janeiro, Brazil')
citySelected.grid(column=1, row=0)
citySelected.current(1) # highligh first city

max_width = max(len(x) for x in citySelected['values'])
new_width = max_width
# new_width = max_width - 4

citySelected.config(width=new_width)


# --------------------------------------------------------------
#=======================================
ENTRY_WIDTH = max_width + 3
#=======================================
# Adding Label & Textbox Entry widgets
#---------------------------------------
ttk.Label(weather_conditions_frame, text="Last Updated:").grid(column=0, row=1, sticky='E')
updated = tk.StringVar()
updateEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
updateEntry.grid(column=1, row=1, sticky='W')

#---------------------------------------
ttk.Label(weather_conditions_frame, text="Weather").grid(column=0, row=2, sticky='E')
weather = tk.StringVar()
weatherEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=weather, state='readonly')
weatherEntry.grid(column=1, row=2, sticky='W')
#---------------------------------------
ttk.Label(weather_conditions_frame, text="Temperature:").grid(column=0, row=3, sticky='E')
temp = tk.StringVar()
tempEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=temp, state='readonly')
tempEntry.grid(column=1, row=3, sticky='W')
#---------------------------------------
ttk.Label(weather_conditions_frame, text="Dewpoint:").grid(column=0, row=4, sticky='E')
dew = tk.StringVar()
dewEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=dew, state='readonly')
dewEntry.grid(column=1, row=4, sticky='W')
#---------------------------------------
ttk.Label(weather_conditions_frame, text="Relative Humidity:").grid(column=0, row=5, sticky='E')
rel_humi = tk.StringVar()
rel_humiEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=rel_humi, state='readonly')
rel_humiEntry.grid(column=1, row=5, sticky='W')

#---------------------------------------
ttk.Label(weather_conditions_frame, text="Wind:").grid(column=0, row=6, sticky='E')
wind = tk.StringVar()
windEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wind, state='readonly')
windEntry.grid(column=1, row=6, sticky='E')
#---------------------------------------
ttk.Label(weather_conditions_frame, text="Visiblity:").grid(column=0, row=7, sticky='E')
visiblity = tk.StringVar()
visiblityEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=visiblity, state='readonly')
visiblityEntry.grid(column=1, row=7, sticky='E')
#---------------------------------------
ttk.Label(weather_conditions_frame, text="MSL Pressure:").grid(column=0, row=8, sticky='E')
msl_pressure = tk.StringVar()
msl_pressureEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=msl_pressure, state='readonly')
msl_pressureEntry.grid(column=1, row=8, sticky='E')
#---------------------------------------
ttk.Label(weather_conditions_frame, text="Altimeter:").grid(column=0, row=9, sticky='E')
altimeter = tk.StringVar()
altimeterEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=altimeter, state='readonly')
altimeterEntry.grid(column=1, row=9, sticky='E')


for child in weather_conditions_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)
#start GUI

win.mainloop()

    