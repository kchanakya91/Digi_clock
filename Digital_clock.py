#!/usr/bin/env python
# coding: utf-8

# In[6]:


import datetime

now = datetime.datetime.now()
time = now.strftime('%H:%M:%S %p')

print('Current Time:', time)

