#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo"  />
# </center>
# 

# # **Survey Dataset Exploration Lab**
# 

# Estimated time needed: **30** minutes
# 

# ## Objectives
# 

# After completing this lab you will be able to:
# 

# *   Load the dataset that will used thru the capstone project.
# *   Explore the dataset.
# *   Get familier with the data types.
# 

# ## Load the dataset
# 

# Import the required libraries.
# 

# In[13]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# The dataset is available on the IBM Cloud at the below url.
# 

# In[14]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"


# Load the data available at dataset_url into a dataframe.
# 

# In[38]:


# your code goes here
df = pd.read_csv(url)
df.head()


# ## Explore the data set
# 

# It is a good idea to print the top 5 rows of the dataset to get a feel of how the dataset will look.
# 

# Display the top 5 rows and columns from your dataset.
# 

# In[39]:


# your code goes here
df.head()


# ## Find out the number of rows and columns
# 

# Start by exploring the numbers of rows and columns of data in the dataset.
# 

# Print the number of rows in the dataset.
# 

# In[40]:


# your code goes here
df.shape


# Print the number of columns in the dataset.
# 

# In[41]:


# your code goes here
df.columns


# ## Identify the data types of each column
# 

# Explore the dataset and identify the data types of each column.
# 

# Print the datatype of all columns.
# 

# In[42]:


# your code goes here
df.dtypes


# Print the mean age of the survey participants.
# 

# In[45]:


# your code goes here
mean_age = df['Age'].mean()
print(mean_age)


# The dataset is the result of a world wide survey. Print how many unique countries are there in the Country column.
# 

# In[50]:


# your code goes here
unique_country = df['Country'].unique()
print(unique_country)


# ## Authors
# 

# Ramesh Sannareddy
# 

# ### Other Contributors
# 

# Rav Ahuja
# 

# ## Change Log
# 

# | Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
# | ----------------- | ------- | ----------------- | ---------------------------------- |
# | 2020-10-17        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |
# 

# Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2021-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 
