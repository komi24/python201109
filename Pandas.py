#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("train.csv")
df


# In[3]:


df.describe()


# In[4]:


df.columns


# In[5]:


df["Age"].describe()


# In[8]:


df[["Age", "Survived"]]


# In[9]:


df[["Age", "Survived"]].describe()


# In[11]:


df[["Age", "Survived"]].head(100)


# In[14]:


df.iloc[20:40]["Age"]


# In[15]:


df.iloc[20:40]


# In[16]:


df["Age"].head()


# In[17]:


df["Age"] * 2


# In[18]:


df["Age * 2"] = df["Age"] * 2
df


# In[24]:


df[["Age * 2"] + list(df.columns)[:-1]]


# In[22]:


df.columns.values


# In[30]:


df[df["Survived"] == 0] # Filtre


# In[31]:


df[df["Survived"] == 0].iloc[0:10]


# In[32]:


df[df["Survived"] == 0].loc[0:10]


# In[34]:


df["Age"].hist()


# In[ ]:


# Afficher la distribution des ages pour les survivants

