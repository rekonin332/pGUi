'''
Created on 2017年5月25日

@author: Todd
'''

import tkinter as tk 

windows = tk.Tk()

windows.title('fuck you')


#=====================
#  functions
#=====================

def get_current_windows_size():
    windows.update()
    print('width  = ', windows.winfo_width())
    print('height = ', windows.winfo_height())
    
def increase_window_width():
    windows.minsize(width=300, height=1)
    windows.resizable(0, 0)
    

get_current_windows_size()    
increase_window_width()
print()
get_current_windows_size()
windows.mainloop()
