#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ASSIGNMENT 2


# In[ ]:


#1. Create 5*5 matrix with row values ranging from 0 to 4


# In[3]:


import numpy as np
x = np.zeros((5,5))
print("Row values ranging from 0 to 4.")
x += np.arange(5)
print(x)


# In[ ]:


#2. Multiply a 5*3 Matrix by 3*2 matrix (real matrix product)


# In[6]:


import numpy as np
x =np.random.random((5,3))
print("First Array:")
print(x)
y =np.random.random((3,2))
print("Second Array:")
print(y)
z =np.dot(x,y)
print("dot product of two arrays:")
print(z)


# In[ ]:


#3. What is the result of the following Exp.


# In[7]:


0*np.nan


# In[8]:


np.nan==np.nan


# In[9]:


np.inf>np.nan


# In[10]:


np.nan-np.nan


# In[11]:


np.nan in set ([np.nan])


# In[12]:


0.3==3*0.1


# In[ ]:


#4. Create a 10*10 array with random values and find the minimum and maximum values.


# In[2]:


import numpy as np
x = np.random.random((10,10))
print("Original Array:")
print(x) 
xmin, xmax = x.min(), x.max()
print("Minimum and Maximum Values:")
print(xmin, xmax)

