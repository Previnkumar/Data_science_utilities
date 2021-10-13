#!/usr/bin/env python
# coding: utf-8

# In[111]:


import matplotlib.pyplot as plt
import numpy as np


# # Basic plotting

# In[112]:


arr = np.array([2,4,6,8,10])
arr


# In[113]:


# default x axis with 0, 1 2, 3, ... values are taken
plt.plot(arr)


# In[114]:


plt.plot(arr, 'o')


# # Styles and customizations

# # Markers ( o  *  .  x  X  +  D  d  H  h  1  2  3  _  |  <  > )

# In[115]:


arr


# In[116]:


plt.plot(arr, marker='D')


# # Line style
# 
# solid  - solid | .<br>
# dotted - dotted | : |(0, (1,1)) <br>
# dashed - dashed | -- |(0, (5,5)) <br>
# dashdotted      | -. |(0, (3,5,1,5)) <br>
# loosely dashed  - (0, (5,10)) <br>
# densely dashed  - (0, (5,1)) <br>

# In[117]:


plt.plot(arr, linestyle=(0, (5, 1)))


# # colors
# 
# RGB  - (0.1, 0.2, 0.5) <br>
# hex RGB - #0f0f0f <br>
# b - blue <br>
# g - green <br>
# r - red <br>
# c - cyan <br>
# m - magenta <br>
# y - tellow <br>
# w - white <br>
# k - black <br>

# In[118]:


plt.plot(arr, color=(0.1,0.2,0.5))


# # format strings (fmt)
# ## marker | line | color

# In[119]:


plt.plot(arr, 'o:r')


# # marker size | ms

# In[120]:


plt.plot(arr, 'D-b', markersize=15)


# # Marker face color | mfc

# In[121]:


plt.plot(arr,'o-.b', ms=15, mfc='r')


# # Line width

# In[122]:


plt.plot(arr, 'o-g', markersize=40, mfc='b', linewidth='20')


# # Labels

# In[123]:


x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])


# In[124]:


plt.plot(x1, y1)
plt.plot(x2, y2)
plt.xlabel("X axis")
plt.ylabel("Y axis")


# # Title

# In[125]:


plt.plot(x1, y1)
plt.plot(x2, y2)
plt.title("Graph with title")


# In[126]:


plt.plot(x1, y1)
plt.plot(x2, y2)
plt.title("Graph with title on left",loc='left')


# # Font

# In[127]:


plt.plot(x1, y1)
plt.plot(x2, y2)
font = {'family':'serif','color':'blue','size':20}
plt.title("Graph with title", fontdict=font)


# # Grid

# In[128]:


plt.plot(x1, y1)
plt.plot(x2, y2)
plt.grid()


# In[129]:


plt.plot(x1, y1)
plt.plot(x2, y2)
plt.grid(axis='x')


# In[130]:


plt.plot(x1, y1)
plt.plot(x2, y2)
plt.grid(axis='y')


# In[ ]:




