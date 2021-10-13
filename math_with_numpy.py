#!/usr/bin/env python
# coding: utf-8

# In[57]:


import numpy as np


# # Basic operations

# In[58]:


arr = np.random.randint(10, size=(5,5))
arr


# In[59]:


# addition
arr + 2


# In[60]:


# subtraction
arr - 4


# In[61]:


# multiplication
arr * 4


# In[62]:


# division
arr / 2


# In[63]:


# power
arr ** 3


# In[64]:


# reminder
arr % 3


# # multiplication & dot product

# In[65]:


arr1 = np.random.randint(10, size=(5,5))
arr1


# In[66]:


arr2 = np.random.randint(10, size=(5,5))
arr2


# In[67]:


vec = np.array([1,2,3,4,5])
vec


# In[68]:


vec.shape


# In[69]:


arr1 * arr2


# In[70]:


np.multiply(arr1, arr2)


# In[71]:


# ideal matrix multiplication done by processing row of mat1 and col of mat2
np.dot(arr1, arr2)


# In[72]:


np.multiply(arr1, vec)


# In[73]:


np.dot(arr1, vec)


# # Basic stats

# In[74]:


arr


# In[75]:


# mean
np.mean(arr)


# In[76]:


# median
np.median(arr)


# In[77]:


# standard deviation
np.std(arr)


# In[78]:


# correlation coefficient
np.corrcoef(arr)


# # Image processing
# Images are made up of pixels that are stored in the form of an array. 
# 
# Each pixel has a value ranging between 0 to 255 => 0 indicating a black pixel and 255 indicating a white pixel. 
# 
# 
# A colored image consists of three 2-D arrays, one for each of the color channels: Red, Green, and Blue, placed back-to-back thus making a 3-D array. Each value in the array constitutes a pixel value. So, the size of the array depends on the number of pixels along each dimension.

# In[79]:


# using matplotlib for visualization
import matplotlib.pyplot as plt
# using pillow for image processing
from PIL import Image


# In[80]:


img = Image.open("data_files/car_image.jpg")
img


# In[81]:


arr = np.asarray(img)
arr


# In[82]:


arr.shape


# In[83]:


plt.imshow(np.flip(arr, axis=1))


# In[84]:


plt.imshow(np.flip(arr, axis=0))


# In[85]:


plt.imshow(arr)


# In[ ]:




