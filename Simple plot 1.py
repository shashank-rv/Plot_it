#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random


# In[15]:


x = list(range(20))
y = [3,4,5,6,7,1,8,4,7,8,9,3,4,5,6,7,8,3,4,5]
ymax = max(y)
xpos = y.index(ymax)
xmax = x[xpos]
plt.plot(x,y,marker="o",markevery=[xmax],color='g')
plt.grid()
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.annotate("max_value",(xmax,ymax))
plt.title("sample")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




