#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import numpy as np


# In[3]:


import pandas as pd


# In[4]:


os.chdir('D:\data sets') # setting the dirctory


# In[5]:


import datetime as dt # for date and time formats of data 


# In[42]:


work=pd.read_excel('Test Data for Analytics.xlsx')  # importing of data


# In[41]:


## Step 1 converting the different formats of data into single type 


# In[43]:


work['SHOW_START_DATE'] # many different forms of date


# In[7]:


work['SHOW_START_DATE']=pd.to_datetime(work['SHOW_START_DATE']).dt.strftime('%m-%d-%Y,') # converting to single format using dt.strftime


# In[9]:


work['SHOW_END_DATE']=pd.to_datetime(work['SHOW_END_DATE']).dt.strftime('%m-%d-%Y')


# In[10]:


work['SHOW_END_DATE'].unique() # all data is in one format


# In[11]:


work.shape


# In[ ]:


# step 2: same as step 1 for reg date


# In[12]:


work['REG_DATE']=pd.to_datetime(work['REG_DATE']).dt.strftime('%m-%d-%Y')


# In[44]:


work['REG_DATE'].head(1) # head is used to show data of the top rows and number assigned is for how many rows  


# In[15]:


work.columns


# In[ ]:


# step3 


# In[45]:


work['ATTENDED'] #type of data is boolean or binary that is yes or no (binary or boolean is also 0,1 or true or false etc)


# In[16]:


work['ATTENDED']=work['ATTENDED'].apply(lambda x:1 if x=='Yes' else '0') # changing the yes or no type of data into 1,0


# In[17]:


work['ATTENDED']


# In[ ]:


# step4: 


# In[19]:


work['SHOWINFO_SOURCE']


# In[20]:


work


# In[23]:


work['SHOWINFO_SOURCE']=work['SHOWINFO_SOURCE'].str.replace("]","") # removing the ']'(data cleaning)


# In[46]:


work['SHOWINFO_SOURCE'].unique() # unique() is used to identify the differnet data in columns


# In[ ]:


# step 5: (same as step4)


# In[47]:


work['AIRLINE_BOOKED']=work['AIRLINE_BOOKED'].str.strip('With which airline are you planning to take or have you already booked your flight with? ""]')
# data cleaning : strip is used to cut the data or remove the part of data 
# strip is 3 types
   # 1.Rstrip
   # 2.lstrip
    #3.strip


# In[ ]:


# step 6 ; (same as step 5)


# In[26]:


work['HOTEL_BOOKED']=work['HOTEL_BOOKED'].str.strip('Which hotel/apartment are you planning to stay in? ""]')
#data cleaning


# In[ ]:


#step7; data cleaning


# In[27]:


work['NO_NIGHTS_BUSINESS']=work['NO_NIGHTS_BUSINESS'].str.strip('How man  y nights are you planning to stay in Dubai on business? DaysWeek""]')


# In[28]:


work['NO_NIGHTS_BUSINESS'].unique()


# In[30]:


work['festival_indicator']=pd.to_datetime(work["SHOW_START_DATE"]).dt.strftime('%m')


# In[31]:


work['festival_indicator'].str.replace('02','1').replace('03','0')


# In[32]:


work["SHOW_START_DATE"].unique()


# In[33]:


work['NO_NIGHTS_BUSINESS']


# In[34]:


work['NO_NIGHTS_LEISURE']=work['NO_NIGHTS_LEISURE'].str.extract("(\d+)").fillna(0).astype(int)


# In[35]:


work['NO_NIGHTS_LEISURE']


# In[36]:


work['NO_NIGHTS_BUSINESS']=work['NO_NIGHTS_BUSINESS'].str.extract("(\d+)").fillna(0).astype(int)


# In[37]:


work['NO_NIGHTS_BUSINESS'].unique()


# In[38]:


work['REG_DATE01']=pd.to_datetime(work['REG_DATE']).dt.strftime('%m').astype(int)


# In[39]:


work['REG_DATE01'].unique()


# In[ ]:




