#!/usr/bin/env python
# coding: utf-8

# ## Learn Numpy
# 
# Numpy stands for numberical python. It is one of the most useful scientific libraries available in python. 

# In[229]:


import numpy as np


# # Creating basic arrays

# In[230]:


np.array([1,2,3,4,5])


# In[231]:


np.array([1,2,3,4,5], dtype=np.float32)


# 
# # Creating multi dimentional arrays

# In[232]:


np.array([[1,2,3,4,5],
         [6,7,8,9,10]])


# # Array creation utilities

# In[233]:


np.zeros(5)


# In[234]:


np.zeros((2,5))


# In[235]:


np.ones(5, dtype=np.int32)


# In[236]:


np.ones((2,5), dtype=np.int32)


# In[237]:


np.full(5, 6)


# In[238]:


np.full((2,5), 10)


# In[239]:


np.empty((2,3))


# # Identity matrix 
# Identity matrix will have nxn shape (same number of rows and columns)

# In[240]:


np.eye(5, dtype=np.int32)


# but numpy gives a flexibility to change the diagonal along which values have to be 1 
# 
# Below are such examples, but these matrices are not identity matrices

# In[241]:


np.eye(5, k=1, dtype=np.int32)


# In[242]:


np.eye(5, k=2, dtype=np.int32)


# In[243]:


np.eye(5, k=-2, dtype=np.int32)


# # Random numbers

# In[244]:


np.random.rand(2)


# In[245]:


# np.random.rand((2, 5)) won't work
np.random.rand(2,5)


# In[246]:


np.random.rand(3,3,3)


# In[247]:


np.random.randint(5, 10, size=(4,4), dtype=np.int32)


# # Utility functions

# # arange
# 
# Evenly spaced n-dimensional array <br>
# 
# np.arange(start, end, step)

# In[248]:


np.arange(5)


# In[249]:


np.arange(5, 20)


# In[250]:


np.arange(5, 20, 2)


# # linspace
# 
# Similar to arange, but instead of step it acccepts size <br>
# 
# np.linspace(start, end, size)
# 

# In[251]:


# default size is 50, 
# so if size is not specified linspace splits start and end with 50 even steps

np.linspace(5, 10)


# In[252]:


np.linspace(5, 10, 10)


# In[253]:


# retstep gives the difference between points also along with output given by linspace

np.linspace(5, 10, 10, retstep=True)


# # Dimensions and Shapes

# In[254]:


arr1 = np.zeros(5)
arr1


# In[255]:


arr1.ndim


# In[256]:


arr2 = np.zeros((1,5))
arr2


# In[257]:


arr2.ndim


# In[258]:


arr3 = np.array([np.zeros((1,5)), np.ones((1,5))], dtype=np.int32)
arr3


# In[259]:


arr3.ndim


# In[260]:


arr3.shape


# In[261]:


arr2.shape


# In[262]:


arr3.shape


# In[263]:


arr1.size


# In[264]:


arr2.size


# In[265]:


arr3.size


# # Reshaping

# In[266]:


arr = np.arange(1,26)
arr


# In[267]:


arr.shape


# In[268]:


arr = arr.reshape(5,5)
arr


# In[269]:


arr.shape


# In[270]:


arr.flatten() # returns copy of arr


# In[271]:


arr.ravel() # returns original array, so any change on this return obj will affect actual array


# # Flip and Transpose

# In[272]:


arr


# In[273]:


np.transpose(arr)


# In[274]:


np.flip(arr)


# # Dimention addition and deletion

# # Expanding dimension

# In[275]:


arr = np.ones(5, dtype=np.int32)


# In[276]:


# expanding after adding a column
new_arr = np.expand_dims(arr, axis=0)
new_arr


# In[277]:


new_arr.shape


# In[278]:


new_arr = np.expand_dims(arr, axis=1)
new_arr


# In[279]:


new_arr.shape


# # Squeezing dimensions

# In[280]:


arr = np.array([[[1,2,3],[4,5,6]]])
arr


# In[281]:


arr.shape


# In[282]:


new_arr = np.squeeze(arr, axis=0)
new_arr


# In[283]:


new_arr.shape


# # Indexing and Slicing

# # 1 dimension

# In[284]:


arr = np.array([1,2,3,4,5])
arr


# In[285]:


arr[1]


# In[286]:


arr[1:4]


# In[287]:


arr[1:4:2]


# In[288]:


arr[::-1]


# # 2 dimension

# In[289]:


arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
arr


# In[290]:


arr.shape


# In[291]:


arr[0,2]


# In[292]:


arr[1,3]


# In[293]:


arr[0:3, 0:3]


# In[294]:


arr[0:, 3:]


# In[295]:


arr[0:, 0::2]


# # Stacking and Concatenation

# In[296]:


arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])


# In[297]:


# vertical stacking (or) row addition
np.vstack((arr1, arr2))


# In[298]:


# horizontal stacking (or) column addition
np.hstack((arr1, arr2))


# In[299]:


arr1 = np.arange(0, 5).reshape(1,5)
arr2 = np.arange(5, 10).reshape(1,5)
arr1, arr2


# In[300]:


np.concatenate((arr1, arr2), axis=0)


# In[301]:


np.concatenate((arr1, arr2), axis=1)


# In[302]:


np.append(arr1, arr2, axis=0)


# In[303]:


np.append(arr1, arr2, axis=1)


# # Hsplit and Vsplit

# In[304]:


arr = np.random.randint(5, size=(4,4), dtype=np.int32)
arr


# In[305]:


np.hsplit(arr,2)


# In[306]:


np.hsplit(arr, 4)


# In[307]:


np.vsplit(arr, 2)


# # other functions

# # unique

# In[308]:


arr = np.array([1,1,2,2,2,3,4,5,5])
arr


# In[309]:


np.unique(arr)


# # aggregate functions

# In[310]:


arr


# In[311]:


np.sum(arr)


# In[312]:


np.cumsum(arr, axis=1)


# In[ ]:


np.cumsum(arr, axis=0)


# In[ ]:





# # argmax and argmin

# In[ ]:


arr = np.array([[5,4,3,2,1],
               [6,7,8,9,10]])
arr


# In[ ]:


# returns index of maximum element of array
np.argmax(arr)


# In[ ]:


# column wise
np.argmax(arr, axis=0)


# In[ ]:


# row wise
np.argmax(arr, axis=1)


# In[ ]:


# returns index of minimum element of array
np.argmin(arr)


# In[ ]:


np.argmin(arr, axis=0)


# In[ ]:


np.argmin(arr, axis=1)


# # shuffle

# In[ ]:


arr = np.array([1,2,3,4,5,6,7,8,9,10])
arr


# In[ ]:


np.random.shuffle(arr)
arr


# # count non zero

# In[ ]:


np.count_nonzero(arr)


# # absolute

# In[ ]:


arr = np.random.randint(-5, 5 , size=(4,4), dtype=np.int32)
arr


# In[ ]:


np.abs(arr)


# # sorting

# In[ ]:


arr


# In[ ]:


np.sort(arr, axis=0)


# In[ ]:


np.sort(arr, axis=1)


# In[ ]:


np.sort(arr, kind='mergesort', axis=1)


# In[ ]:


arr

