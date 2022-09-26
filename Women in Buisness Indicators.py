#!/usr/bin/env python
# coding: utf-8

# In[70]:


# import all needed packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode, iplot
import chart_studio as py
import plotly.express as px
import openpyxl
import geopandas
import statistics


# In[2]:


# import the WBL index
wbl_df = pd.read_excel("/Users/izzyabate/Desktop/Research Sanchari/WBL Panel.xlsx")


# # What is the index?
# WBL index  measures the extent of legal equality women have with men in various dimensions of their lives (including marriage, mobility, work, pay etc.)

# In[7]:


# Understanding the data 
print(wbl_df.columns)
print(wbl_df.describe())


# # The geographical distribution of the average WBL index
# - Regions: High income: OECD, Middle East & North Africa, Sub-Saharan Africa, East Asia & Pacific, Europe & Central Asia, Latin America & Caribbean, South Asia

# In[60]:


# Subset data frame for region and WBL index
geo_index = wbl_df[['Region', 'WBL INDEX']]
geo_index.head()

# Find the average WBL index by Region
avgWBL = geo_index.groupby(['Region']).mean()


# In[40]:


# Show the geographical distribution of the average WBL index
fig = px.bar(avgWBL,
             labels={'value':'Average WBL Index'}, title='Geographical Distribution of the Average WBL Index')
fig.update_traces(marker_color='hotpink')
fig.show()


# ## How this distribution has changed over decades ?

# In[83]:


# Create an index including: Region, WBL Index, Report Year
year_index = wbl_df[['Region', 'WBL INDEX', 'Report Year']]

# Create a pivot table showing the WBL index for each region by year
year_index1 = pd.pivot_table(year_index, index=['Report Year'], columns=['Region'], values=['WBL INDEX'])
year_index1


# In[101]:


# Create a multiple line plot showing the distribution over time
ax = year_index1.plot(xticks=year_index1.index, ylabel='WBL INDEX',  figsize=(18,5))
plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
ax.legend(bbox_to_anchor=(1.1, 1.05))
plt.show()


# In[ ]:




