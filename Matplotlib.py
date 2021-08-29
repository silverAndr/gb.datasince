#!/usr/bin/env python
# coding: utf-8

# ### Задание 1

# In[4]:


from matplotlib import pyplot


# In[5]:


import numpy as np


# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")


# In[8]:


x = [1, 2, 3, 4, 5, 6, 7]


# In[9]:


y = [3.5, 3.8, 4.2, 4.5, 5, 5.5, 7]


# In[10]:


pyplot.plot(x, y)
pyplot.show()


# In[11]:


pyplot.scatter(x, y)
pyplot.show()


# ### Задание 2

# In[12]:


t = np.linspace(0, 10, 51)
t


# In[13]:


f = np.cos(t)
f


# In[14]:


title_font = {
    "fontsize": 16,
    "fontweight": "bold",
    "color": "#808080",
    "family": "serif",
}


# In[15]:


label_dict = title_font
label_dict['fontsize'] = 12


# In[16]:


pyplot.plot(t, f, color="green")
pyplot.title('График f(t)', loc="left", fontdict=title_font)
pyplot.xlabel('Значения t', fontdict=label_dict, loc='right')
pyplot.ylabel('Значения f', fontdict=label_dict, loc='top')
pyplot.axis([0.5, 9.5, -2.5, 2.5])
pyplot.show()


# ### Задание 3

# In[17]:


x = np.linspace(-3, 3, 51)
x


# In[18]:


y1 = x**2
y1


# In[19]:


y2 = 2 * x + 0.5
y2


# In[20]:


y3 = -3 * x - 1.5
y3


# In[21]:


y4 = np.sin(x)
y4


# In[22]:


fig, ax = pyplot.subplots(nrows=2, ncols=2)
ax1, ax2, ax3, ax4 = ax.flatten()
ax1.plot(x,y1)
ax1.set_title('График y1')
ax1.set_xlim([-5, 5])

ax2.plot(x,y2)
ax2.set_title('График y2')

ax3.plot(x,y3)
ax3.set_title('График y3')

ax4.plot(x,y4)
ax4.set_title('График y4')

fig.set_size_inches(8,6)
pyplot.subplots_adjust(wspace=0.3, hspace=0.3)


# ### Задание 4

# In[23]:


import pandas as pd


# In[24]:


pyplot.style.use('fivethirtyeight')


# In[36]:


df = pd.read_csv('creditcard.csv')
df


# In[37]:


classes = df['Class'].value_counts()
classes


# In[34]:


classes.plot(kind="bar")
pyplot.show()


# In[35]:


classes.plot(kind="bar", logy=True)
pyplot.show()


# ### Повторение

# In[44]:


a = np.linspace(12, 23, 12)
a = np.int32(a)
a


# In[48]:


a1 = a.reshape(2,6)
a1


# In[49]:


a2 = a.reshape(3,4)
a2


# In[50]:


a3 = a.reshape(4,3)
a3


# In[51]:


a4 = a.reshape(6,2)
a4


# In[52]:


a5 = a.reshape(1,12)
a5


# In[53]:


b1 = a.reshape(-1,6)
b1


# In[55]:


b2 = a.reshape(-1,4)
b2


# In[56]:


b3 = a.reshape(4,-1)
b3


# In[57]:


b4 = a.reshape(6,-1)
b4


# In[58]:


b5 = a.reshape(-1,12)
b5


# Это одноколочная матрица, но массив все-таки двумерный, так как есть массив в котором одно значение - внутренний массив

# In[62]:


ar = np.random.normal(size = (3,4))
ar


# In[65]:


c = ar.flatten()
c


# In[67]:


a = np.arange(20, 0, -2)
a


# In[68]:


b = np.arange(20, 1, -2)
b


# In[ ]:




