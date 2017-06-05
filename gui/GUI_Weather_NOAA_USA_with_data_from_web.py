
'''
Created on 2017年5月25日

@author: Todd
'''
from urllib import request
import tkinter as tk
from tkinter import Menu
from tkinter import ttk # themed Tk
from email.mime import image

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

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Tab 3')

tabControl.pack(expand=1, fill="both") # pack to make visible

#==========================================================================================
# we are creating a container frame to hold all other widgets
#==========================================================================================    
# 
#create new LabelFrame
    
def _get_station():
    station = station_id_combo.get()
    get_weather_data(station)
    populate_weather_data()
    
weather_cities_frame = ttk.LabelFrame(tab1, text=' Latest Observation for ')
weather_cities_frame.grid(column=0, row=0, padx=8, pady=4)

#Adding a Label
ttk.Label(weather_cities_frame, text="Weather Station ID:").grid(column=0, row=0, sticky='W')

ttk.Button(weather_cities_frame, text='Get Weather', command=_get_station).grid(column=2, row=0)


#---------------------------------------------------
station_id = tk.StringVar()
station_id_combo = ttk.Combobox(weather_cities_frame, width=24, textvariable=station_id)
station_id_combo['values'] = ('KLAX', 'KDEN', 'KNYC')
station_id_combo.grid(column=1, row=0)
station_id_combo.current(0) # highligh first city

max_width = max(len(x) for x in station_id_combo['values'])
new_width = max_width + 3
# new_width = max_width - 4

station_id_combo.config(width=new_width)

weather_conditions_frame = ttk.LabelFrame(tab1, text=' Current Weather Conditions ')

#using the tkinter grid layout manager
weather_conditions_frame.grid(column=0, row=1, padx=8, pady=4)

# --------------------------------------------------------------
#=======================================
ENTRY_WIDTH = max_width + 10
#=======================================
# Adding Label & Textbox Entry widgets
#---------------------------------------
ttk.Label(weather_conditions_frame, text="Last Updated:").grid(column=0, row=1, sticky='E')
updated = tk.StringVar()
updateEntry = ttk.Entry(weather_conditions_frame, textvariable=updated, state='readonly')
updateEntry.grid(column=1, row=1, sticky='W')


# updated.set(weather_data.get("last_update","N/A"))

#---------------------------------------
ttk.Label(weather_conditions_frame, text="Weather").grid(column=0, row=2, sticky='E')
weather = tk.StringVar()
weatherEntry = ttk.Entry(weather_conditions_frame, textvariable=weather, state='readonly')
weatherEntry.grid(column=1, row=2, sticky='W')
#---------------------------------------
ttk.Label(weather_conditions_frame, text="Temperature:").grid(column=0, row=3, sticky='E')
temp = tk.StringVar()
tempEntry = ttk.Entry(weather_conditions_frame, textvariable=temp, state='readonly')
tempEntry.grid(column=1, row=3, sticky='W')
#---------------------------------------
ttk.Label(weather_conditions_frame, text="Dewpoint:").grid(column=0, row=4, sticky='E')
dew = tk.StringVar()
dewEntry = ttk.Entry(weather_conditions_frame, textvariable=dew, state='readonly')
dewEntry.grid(column=1, row=4, sticky='W')
#---------------------------------------
ttk.Label(weather_conditions_frame, text="Relative Humidity:").grid(column=0, row=5, sticky='E')
rel_humi = tk.StringVar()
rel_humiEntry = ttk.Entry(weather_conditions_frame, textvariable=rel_humi, state='readonly')
rel_humiEntry.grid(column=1, row=5, sticky='W')

#---------------------------------------
ttk.Label(weather_conditions_frame, text="Wind:").grid(column=0, row=6, sticky='E')
wind = tk.StringVar()
windEntry = ttk.Entry(weather_conditions_frame, textvariable=wind, state='readonly')
windEntry.grid(column=1, row=6, sticky='E')
#---------------------------------------
ttk.Label(weather_conditions_frame, text="visibility:").grid(column=0, row=7, sticky='E')
visiblity = tk.StringVar()
visiblityEntry = ttk.Entry(weather_conditions_frame, textvariable=visiblity, state='readonly')
visiblityEntry.grid(column=1, row=7, sticky='E')
#---------------------------------------
ttk.Label(weather_conditions_frame, text="MSL Pressure:").grid(column=0, row=8, sticky='E')
msl_pressure = tk.StringVar()
msl_pressureEntry = ttk.Entry(weather_conditions_frame, textvariable=msl_pressure, state='readonly')
msl_pressureEntry.grid(column=1, row=8, sticky='E')
#---------------------------------------
ttk.Label(weather_conditions_frame, text="Altimeter:").grid(column=0, row=9, sticky='E')
altimeter = tk.StringVar()
altimeterEntry = ttk.Entry(weather_conditions_frame, textvariable=altimeter, state='readonly')
altimeterEntry.grid(column=1, row=9, sticky='E')


#===============================================
weather_data = {
        "last_update": "yesterday",
        "temperature": "31 C",
        "visibility": "10 miles"
    }
#===============================================


#===============================================
#  Retrieve the data from live web search
#===============================================

weather_data_tags_dict = {
     'observation_time': ''
    ,'weather': ''
    ,'temp_f':''
    ,'temp_c':''
    ,'dewpoint_f':''
    ,'dewpoint_c':''
    ,'relative_humidity':''
    ,'wind_string':''
    ,'visibility_mi':''
    ,'pressure_string':''
    ,'pressure_in':''
    ,'location':''
    }



def get_weather_data(station_id='KLAX'):
    url_general = 'http://www.weather.gov/xml/current_obs/{}.xml'
    url = url_general.format(station_id)
    print(url)
    with request.urlopen(url) as f:
    
        content = f.read().decode()
    #     print(content)
        import xml.etree.ElementTree as ET
        xml_root = ET.fromstring(content)
    #     print('xml_root: {}\n'.format(xml_root.tag))
    
        for data_point in weather_data_tags_dict.keys():
            weather_data_tags_dict[data_point] = xml_root.find(data_point).text
            
        for key, value in weather_data_tags_dict.items():
            print(key, value)

def populate_weather_data():
    
#     get_weather_data()
    
    updated.set(weather_data_tags_dict.get('observation_time','N/A').replace('Last Updated on ',''))
    temp.set(weather_data_tags_dict.get('temp_f','N/A') 
             + '°F (' +weather_data_tags_dict.get('temp_c','N/A') + '\xb0C)')
    dew.set(weather_data_tags_dict.get('dewpoint_f','N/A') 
             + '°F (' +weather_data_tags_dict.get('dewpoint_c','N/A') + '°C)') # \xb0 == ° 
    wind.set(weather_data_tags_dict.get('wind_string'))
    rel_humi.set(weather_data_tags_dict.get('relative_humidity') + '%')
    visiblity.set(weather_data_tags_dict.get('visibility_mi') + 'miles')
    msl_pressure.set(weather_data_tags_dict.get('pressure_string'))
    altimeter.set(weather_data_tags_dict.get('pressure_in') + 'in Hg')
    weather.set(weather_data_tags_dict.get('weather'))


for child in weather_conditions_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)
    
for child in weather_cities_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)

##################################################################
#     TAB 2
########################
# We are creating a container frame to hold all other widgets

weather_states_frame = ttk.LabelFrame(tab2, text=' Weather Station IDs ')
weather_states_frame.grid(column=0, row=0, padx=8, pady=4)

#-------------------------------------------------------------
# Adding a Label
ttk.Label(weather_states_frame, text='Select a State:').grid(column=0, row=0)

#------------------------------------------------
state = tk.StringVar()
state_combo = ttk.Combobox(weather_states_frame, width=5, textvariable= state)
state_combo['values'] = ('AL','AK','AZ','AR')

state_combo.grid(column=1, row=0)
state_combo.current(0)

def _get_cities():
    state = state_combo.get()
    get_city_station_ids(state)
    

def get_city_station_ids(state='ca'):
    url_general= 'http://w1.weather.gov/xml/current_obs/seek.php?state={}&Find=Find'
    state = state.lower()
    url = url_general.format(state)
    with request.urlopen(url) as f:
        content = f.read().decode()
#         print(content)
        
        parser = WeatherHTMLParser()
        parser.feed(content)
        
        #verify we have  as many stations as cities
        print(len(parser.cities), len(parser.stations))
        
        scr.delete('1.0', tk.END )
        
        for idx in range(len(parser.stations)):
            city_station = parser.cities[idx] + '(' + parser.stations[idx] +')'
#             print(city_station)
            scr.insert(tk.INSERT, city_station + '\n')
            
        station_id_combo['values'] = parser.stations
        station_id_combo.current(0)
        
from html.parser import HTMLParser        
class WeatherHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stations = []
        self.cities = []
        self.grab_data = False
    
    def handle_starttag(self, tag, attrs):
        for att in attrs:
            
            if 'display.php?stid=' in str(att):                
                clean_data = str(att).replace("('href', 'display.php?stid=",'').replace("')",'')
#                 print(clean_data)
                self.stations.append(clean_data)
                self.grab_data = True
    
    def handle_data(self, data):
        if self.grab_data:
#             print('data:',data)
            self.cities.append(data)
            self.grab_data = False
    
    
cityButton = ttk.Button(weather_states_frame, text='Get Cities', command=_get_cities)
cityButton.grid(column=2, row=0)

from tkinter import scrolledtext

scr = scrolledtext.ScrolledText(weather_states_frame, width=30, height=17, wrap=tk.WORD)
scr.grid(column=0, row=1, columnspan=3)


for child in weather_states_frame.winfo_children():
    child.grid_configure(padx=6, pady=6)
    
######################################################################
# Tab 3
#########



# We are creating a container frame to hold all other widgets
weather_image_frame = ttk.LabelFrame(tab3, text=' Weather Images')
weather_image_frame.grid(column=0, row=0, padx=8, pady=4)

import PIL.Image
import PIL.ImageTk

im = PIL.Image.open("few_clouds.png")
photo = PIL.ImageTk.PhotoImage(im)
ttk.Label(weather_image_frame, image=photo).grid(column=0, row=0)

im = PIL.Image.open("night_few_clouds.png")
photo1 = PIL.ImageTk.PhotoImage(im)
ttk.Label(weather_image_frame, image=photo1).grid(column=1, row=0)

im = PIL.Image.open("night_fair.png")
photo2 = PIL.ImageTk.PhotoImage(im)
ttk.Label(weather_image_frame, image=photo2).grid(column=2, row=0)
#start GUI

for chilid in weather_image_frame.winfo_children():
    chilid.grid_configure(padx=8, pady=4)

win.mainloop()

    