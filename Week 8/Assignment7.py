#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("agesex.csv")
df


# In[3]:


df1 = df[df['AGE'].isin([999])]


# In[ ]:





# In[4]:


data_frame = df1.loc[:, ['SEX','AGE', 'POPESTIMATE2010', 'POPESTIMATE2017']]


# In[5]:


data_frame['CHANGE'] = data_frame['POPESTIMATE2017'] - data_frame['POPESTIMATE2010']
percent_change = ((data_frame['POPESTIMATE2017'] - data_frame['POPESTIMATE2010'])/data_frame['POPESTIMATE2010'])*100


# In[6]:


data_frame['PERCENT CHANGE'] = round(percent_change, 2)
df_part1 = data_frame.rename(columns={"POPESTIMATE2010": "2010", "POPESTIMATE2017": "2017"})


# In[9]:


s = pd.Series([1, 2, 3])
#df_part1 = df_part1.set_index(df1['SEX'])
print(df_part1.to_string(index=False))
print("\n\nThe male population changed more.\n\n")
print("---" * 25)
print("\n\n")


# In[10]:


df_part2 = df_part1.loc[:, ['SEX', 'AGE', '2017']]
def proportion(t, a):
    percentA = (a/t)*100
    return round(percentA, 2)
p = [100, proportion(df_part1.iloc[0,3], df_part1.iloc[1,3]), proportion(df_part1.iloc[0,3], df_part1.iloc[2,3])]
df_part2["PROPORTION"] = p
df_part2 = df_part2.set_index(s)
print(df_part2.to_string(index=False))
print("\n\nThe female population has the biggest proportion.\n\n")


# In[ ]:





# In[ ]:




