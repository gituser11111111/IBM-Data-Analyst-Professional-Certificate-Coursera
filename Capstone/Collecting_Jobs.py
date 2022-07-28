#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Import required libraries
import pandas as pd
import json
import requests


# In[13]:


api_url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2021-01-01"
r = requests.get(api_url)
header = r.headers
print(r.headers)
data = r.json()


# In[14]:


df = pd.DataFrame(data)
df.head()


# In[15]:


df.describe()


# In[52]:


df[df['Job Title'] == 'Python']


# In[20]:


def get_number_of_jobs_T(job):
    number_of_jobs = 0
    #your code goes here
    page=1
    new_results=1
    while new_results>0:
        payload={"description":job,"page":page}
        r=requests.get(api_url,payload)
        new_results =len(r.json())
        page+=1
        number_of_jobs+=(len(r.json()))
    #your code goes here
    return job,number_of_jobs


# In[47]:


df[df['Location'] == 'Washington DC']


# In[21]:


get_number_of_jobs_T("python")


# In[48]:


import xlsxwriter


# In[49]:


excel_file_path = r'directory name where file is saved'
writer = pd.ExcelWriter(excel_file_path, engine='xlsxwriter')
df.to_excel(writer, index=False, sheet_name='Jobs_API')
writer.save()


# In[50]:


df2 = df.groupby(['Location']).count()
df2


# In[ ]:




