#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from glob import glob as gb
import os as os

# ### Entering directory path

# In[64]:


dir_root = "/Users/aakas/aa_Machine_Learning/Arem/data"

# In[67]:


os.listdir(dir_root)
## just checking what is present in dir


# In[69]:


folder = os.listdir("/Users/aakas/aa_Machine_Learning/Arem/data")


# In[60]:


df = pd.DataFrame()
buffer = pd.DataFrame()
for i in range(len(folder)):
    dir_path = dir_root + "/" + folder[i] + "/"
    filepath = gb(dir_path + "*.csv")
    if filepath[0]:
        buffer = pd.read_csv(filepath[i], header=4)  ##taking header once
    else:
        buffer = pd.read_csv(filepath[i], header=5)  ##avoiding headers
    buffer["label"] = folder[i]  ## adding folder name as label
    buffer.to_csv('/Users/aakas/aa_Machine_Learning/Arem/master.csv', mode='a', header="False", index="False")



# In[61]:


df = pd.read_csv('/Users/aakas/aa_Machine_Learning/Arem/master.csv')

# In[62]:


print(df)

# ## Data is ready for Logistic Regression

# In[ ]:
