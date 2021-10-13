#!/usr/bin/env python
# coding: utf-8

# In[70]:


import matplotlib.pyplot as plt
import numpy as np


# # Line Plot

# In[71]:


x1 = np.array([1,2,3,4,5])
y1 = np.random.rand(5)
x2 = np.array([2,4,6,8,10])
y2 = np.random.rand(5)

plt.plot(x1, y1, label="line1")
plt.plot(x2, y2, label="line2")
plt.legend()


# # Scatter plot

# In[72]:


plt.scatter(x1, y1, marker="o", color="r")

plt.scatter(x2, y2, marker="D", color="g")


# In[73]:


x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()


# In[74]:


x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

sizes = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, s=sizes, color='g')


# # Bar plot

# In[75]:


x = np.array(['a','b','c','d'])
y = np.array([3,8,1,10])
plt.bar(x, y)


# In[76]:


x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.barh(x, y, color='r')


# In[77]:


x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y, color='hotpink', width=0.3)


# # Histograms
# A histogram is a graph showing frequency distributions.
# 
# It is a graph showing the number of observations within each given interval.

# In[78]:


# Say you ask for the height of 250 people, you might end up with a histogram like this

x = np.random.normal(170, 10, 250)
plt.hist(x)


# # Pie plot

# In[79]:


y = np.array([35, 25, 25, 15, 16])
plt.pie(y)


# In[80]:


y = np.array([35, 25, 25, 15])
labels = ["Apples", "Bananas", "Cherries", "Dates"]
explode = [0.2, 0, 0, 0]
plt.pie(y, labels=labels, explode=explode)
plt.legend()


# # 3D plotting

# In[81]:


from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection="3d")
x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])
z = np.array([6,7,8,9,10])
ax.plot(x, y, z)


# # contour plotting

# In[82]:


feature_x = np.linspace(-5.0, 3.0, 70)
feature_y = np.linspace(-5.0, 3.0, 70)
  

[X, Y] = np.meshgrid(feature_x, feature_y)
Z = X ** 2 + Y ** 2
plt.contour(X, Y, Z)
plt.title("contour plot")
plt.xlabel('X')
plt.ylabel('Y')


# # plotting images

# In[83]:


import matplotlib.image as mpimg
img = mpimg.imread('data_files/car_image.jpg')
plt.imshow(img)


# In[ ]:




