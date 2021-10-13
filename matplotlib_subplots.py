#!/usr/bin/env python
# coding: utf-8

# In[42]:


import matplotlib.pyplot as plt
import numpy as np


# # subplots ( rows, cols, index )

# In[43]:


plt.suptitle("sub plots")
plt.subplot(2,2,1)
plt.plot(np.arange(5, 10))
plt.title("index 1")

plt.subplot(2,2,2)
plt.plot(np.random.rand(5))
plt.title("index 2")

plt.subplot(2,2,3)
plt.plot(np.array([5,4,3,2,1]))
plt.title("index 3")


# # subplots with figure and axis

# In[44]:


fig, ax = plt.subplots(2, 2)


# In[45]:


y1 = np.random.randn(10)
y2 = np.random.randn(10)
y3 = np.random.randn(10)
y4 = np.random.randn(10)

fig, ax = plt.subplots(2, 2)
ax[0][0].plot(y1)
ax[0][1].plot(y2)
ax[1][0].plot(y3)
ax[1][1].plot(y4)
fig


# # Custom layouts

# ## without layouts, title is not visible below

# In[46]:


y1 = np.random.randn(10)
y2 = np.random.randn(10)
y3 = np.random.randn(10)
y4 = np.random.randn(10)

fig, ax = plt.subplots(2, 2)
ax[0][0].plot(y1)
ax[0][0].set_title("plot 1")
ax[0][1].plot(y2)
ax[0][1].set_title("plot 2")
ax[1][0].plot(y3)
ax[1][0].set_title("plot 3")
ax[1][1].plot(y4)
ax[1][1].set_title("plot 4")


# ## Using tight layout

# In[47]:


y1 = np.random.randn(10)
y2 = np.random.randn(10)
y3 = np.random.randn(10)
y4 = np.random.randn(10)

fig, ax = plt.subplots(2, 2)
ax[0][0].plot(y1)
ax[0][0].set_title("plot 1")
ax[0][1].plot(y2)
ax[0][1].set_title("plot 2")
ax[1][0].plot(y3)
ax[1][0].set_title("plot 3")
ax[1][1].plot(y4)
ax[1][1].set_title("plot 4")
plt.tight_layout()
#plt.tight_layout(pad=3.5)


# In[ ]:




