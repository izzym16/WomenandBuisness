#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import all needed packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans
from plotly.subplots import make_subplots
import chart_studio.plotly as py
import plotly.graph_objects as go
import plotly.express as px
import openpyxl
import geopandas
import statistics
import kaleido
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot, plot
import nbconvert


# In[2]:


# import the WBL index
wbl_df = pd.read_excel("/Users/izzyabate/Desktop/Research Sanchari/Book2.xlsx")


# # What is the index?
# WBL index  measures the extent of legal equality women have with men in various dimensions of their lives (including marriage, mobility, work, pay etc.)

# In[3]:


# Understanding the data 
print(wbl_df.columns)
print(wbl_df.describe())


# # The geographical distribution of the average WBL index
# - Regions: High income: OECD, Middle East & North Africa, Sub-Saharan Africa, East Asia & Pacific, Europe & Central Asia, Latin America & Caribbean, South Asia

# In[4]:


# Subset data frame for region and WBL index
geo_index = wbl_df[['Region', 'WBL INDEX']]
geo_index.head()

# Find the average WBL index by Region
avgWBL = geo_index.groupby(['Region']).mean()


# In[5]:


# Show the geographical distribution of the average WBL index
fig = px.bar(avgWBL,
             labels={'value':'Average WBL Index'}, title='Geographical Distribution of the Average WBL Index')
fig.update_traces(marker_color='hotpink')
init_notebook_mode()
fig.show()


# ## How this distribution has changed over decades ?

# In[6]:


# Create an index including: Region, WBL Index, Report Year
year_index = wbl_df[['Region', 'WBL INDEX', 'Report Year']]

# Create a pivot table showing the WBL index for each region by year
year_index1 = pd.pivot_table(year_index, index=['Report Year'], columns=['Region'], values=['WBL INDEX'])
year_index1.head()


# In[7]:


# Create a multiple line plot showing the distribution over time
ax = year_index1.plot(xticks=year_index1.index, ylabel='WBL INDEX',  figsize=(18,5))
plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
ax.legend(bbox_to_anchor=(1.1, 1.05))
plt.show()


# # Distributions for Each Main Indicators 
# ### Main indicators: Mobility, Workplace, Pay, Marriage, Parenthood, Entrepreneurship, Assets, and Pension

# ## Geographical Distribution of Average Mobility, Workplace, Pay, Marriage, Parenthood, Entrepreneurship, Assets, and Pension

# In[8]:


# Show the geographical distribution of the average of each main indicator
# Main indicators: MOBILITY, WORKPLACE, PAY, MARRIAGE, PARENTHOOD, ENTREPRENEURSHIP, ASSETS, PENSION
geo_index2 = wbl_df[['Region', 'MOBILITY', 'WORKPLACE', 
                     'PAY', 'MARRIAGE', 'PARENTHOOD', 'ENTREPRENEURSHIP', 'ASSETS', 'PENSION']]
avgindicators = geo_index2.groupby(['Region']).mean()
print(avgindicators)


# In[9]:


# Visualize through subplots the geographical distribution of each indicator
# Mobility 
figM = px.bar(avgindicators["MOBILITY"], labels={'value':'Average Value'}, 
                     title='Geographical Distribution of the  Mobility Index')
init_notebook_mode()
figM.show()

# Workplace 
figW = px.bar(avgindicators["WORKPLACE"], labels={'value':'Average Value'}, 
                     title='Geographical Distribution of the Workplace Index')
init_notebook_mode()
figW.show()

# Pay
figP = px.bar(avgindicators["PAY"], labels={'value':'Average Value'}, 
                     title='Geographical Distribution of the Pay Index')
init_notebook_mode()
figP.show()

# Marriage
figM = px.bar(avgindicators["MARRIAGE"], labels={'value':'Average Value'}, 
                     title='Geographical Distribution of the Marriage Index')
init_notebook_mode()
figM.show()

# Parenthood
figPH = px.bar(avgindicators["PARENTHOOD"], labels={'value':'Average Value'}, 
                     title='Geographical Distribution of the  Parenthood Index')
init_notebook_mode()
figPH.show()

# Entrepreneurship
figE = px.bar(avgindicators["ENTREPRENEURSHIP"], labels={'value':'Average Value'}, 
                     title='Geographical Distribution of the  Entrepreneurship Index')
init_notebook_mode()
figE.show()

# Assets
figA = px.bar(avgindicators["ASSETS"], labels={'value':'Average Value'}, 
                     title='Geographical Distribution of the Assets Index')
init_notebook_mode()
figA.show()

# Pension
figPN = px.bar(avgindicators["PENSION"], labels={'value':'Average Value'}, 
                     title='Geographical Distribution of the Pension Index')
init_notebook_mode()
figPN.show()


# In[10]:


# Create an index including: Region, Report Year, and all eight main indicators
year_index2 = wbl_df[['Region', 'MOBILITY', 'WORKPLACE', 'PAY', 'MARRIAGE', 'PARENTHOOD',
                     'ENTREPRENEURSHIP', 'ASSETS', 'PENSION', 'Report Year']]

# Create a pivot table showing the index of each major indictor for each region by year
year_indextime = pd.pivot_table(year_index2, index=['Report Year'], columns=['Region'])
year_indextime


# # Geographical Distribution Of Each Main Indicator Average 1970-2020

# In[11]:


# Mobility

sns.lineplot(data=year_indextime["MOBILITY"]).set(title='Mobility over Time')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[12]:


# Workplace
sns.lineplot(data=year_indextime["WORKPLACE"]).set(title='Workplace over Time')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[13]:


# Pay
sns.lineplot(data=year_indextime["PAY"]).set(title='Pay over Time')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[14]:


# Marriage
sns.lineplot(data=year_indextime["MARRIAGE"]).set(title='Marriage over Time')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[15]:


# Parenthood
sns.lineplot(data=year_indextime["PARENTHOOD"]).set(title='Parenthood over Time')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[16]:


# Entrepreneurship
sns.lineplot(data=year_indextime["ENTREPRENEURSHIP"]).set(title='Entrepreneurship over Time')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[17]:


# Assets
sns.lineplot(data=year_indextime["ASSETS"]).set(title='Assets over Time')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[18]:


# Pension
sns.lineplot(data=year_indextime["PENSION"]).set(title='Pension over Time')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[ ]:




