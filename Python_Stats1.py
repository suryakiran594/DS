#!/usr/bin/env python
# coding: utf-8

# In[1]:


data=[23,24,32,45,12,43,67,45,32,56,32]


# In[2]:


data


# In[3]:


import seaborn as sns


# In[4]:


sns.histplot(data)


# In[5]:


data_copy=data.copy()


# In[6]:


print(data_copy)


# In[8]:


data_copy.sort()


# In[9]:


data_copy


# In[11]:


sns.histplot(data,kde=True)  # Probability Distribution Function


# In[12]:


import pandas as pd
data2=pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Statistics-With-Python-TheCompleteGuide/main/Iris.csv")


# In[13]:


data2.head()


# In[15]:


sns.histplot(data2["SepalLengthCm"],kde=True)


# In[17]:


sns.histplot(data2["SepalWidthCm"],kde=True) # Perfect Normal Distribution


# In[18]:


sns.histplot(data2["PetalLengthCm"],kde=True)


# In[19]:


data


# In[20]:


data_copy


# In[21]:


data_copy.append(179)


# In[22]:


data_copy.append(210)


# In[23]:


data_copy.append(289)


# In[24]:


data_copy


# In[27]:


sns.histplot(data_copy,kde=True)   # Right Skewed


# In[31]:


data_copy2=data.copy()


# In[29]:


data


# In[32]:


data_copy2


# In[33]:


data_copy2[0]=-10


# In[34]:


data_copy2


# In[35]:


data_copy2[1]=-75


# In[36]:


data_copy2


# In[37]:


sns.histplot(data_copy2,kde=True)  # Left Skwed


# In[38]:


sns.histplot(data2["PetalWidthCm"],kde=True)


# In[42]:


import numpy as np
s=np.random.normal(0.5,0.2,1000)


# In[49]:


sns.histplot(s,kde=True)  # Kernal Destiny Estimation  # Perfect Normal Distribution


# In[46]:


mu,sigma=3.0,1.0
p=np.random.lognormal(mu,sigma,1000)


# In[48]:


sns.histplot(p,kde=True)    # Log Normal Distribution


# In[51]:


sns.histplot(np.log(p),kde=True)  # Converting log distribution to Normal Distribution


# In[ ]:




