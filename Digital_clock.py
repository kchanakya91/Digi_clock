#!/usr/bin/env python
# coding: utf-8

# In[6]:


import datetime

now = datetime.datetime.now()
time = now.strftime('%H:%M:%S %p')

print('Current Time:', time)


# Advanced digital code

# In[10]:


#Digital clock that updates time every second
#tkiter is a GUI programming in Python. You can find the tutorial page in this link: https://www.pythontutorial.net/tkinter/

import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000,time)
    
lbl = tk.Label(root,font =('calibri',40,'bold'),
              background ='black',
              foreground = 'white')

lbl.pack(anchor = 'center')
time()

root.mainloop()
    

