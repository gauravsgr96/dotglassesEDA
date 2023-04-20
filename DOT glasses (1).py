#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns


# In[23]:


df= pd.read_csv(r"C:\Users\DELL\Desktop\DOT glasses.csv")


# In[24]:


print(df)


# In[25]:


df.head()


# In[26]:


df.tail()


# In[27]:


df.isnull()


# In[28]:


df.isnull().sum()


# In[29]:


#Basic information

df.info()


# In[30]:



#Describe the data

df.describe()


# In[33]:



# Load the data into a DataFrame
df = pd.read_csv(r'C:\Users\DELL\Desktop\DOT glasses.csv')

# Create scatter plots
plt.scatter(df['TV'], df['Sales'])
plt.xlabel('TV advertising ($1000s)')
plt.ylabel('Sales ($1000s)')
plt.show()

plt.scatter(df['Radio'], df['Sales'])
plt.xlabel('Radio advertising ($1000s)')
plt.ylabel('Sales ($1000s)')
plt.show()

plt.scatter(df['Newspaper'], df['Sales'])
plt.xlabel('Newspaper advertising ($1000s)')
plt.ylabel('Sales ($1000s)')
plt.show()


# In[34]:



# Create a correlation matrix
corr = df.corr()

# Create a heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()


# In[35]:


plt.hist(df['Sales'])
plt.xlabel('Sales ($1000s)')
plt.ylabel('Frequency')
plt.show()


# In[ ]:




