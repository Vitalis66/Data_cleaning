#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing Pandas
import pandas as pd


# In[2]:


#Reading in of Data Set
df = pd.read_excel(r"C:\Users\SIMPLE SOLUTIONS\Desktop\Data Science Road map\python\dataset\Customer Call List.xlsx")


# In[3]:


df


# In[8]:


#Dropping duplicates in the DataFrame
df = df.drop_duplicates()
df


# In[20]:


df


# In[31]:


df['Last_Name']=df['Last_Name'].str.strip('./_')


# In[33]:


df


# In[56]:


df['Paying Customer'].replace('Yes', 'Y', inplace=True)



# In[37]:


df['Paying Customer']


# In[51]:


#Formatting the Phone_Number column to be in a uniform manner
#df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]','')
#df['Phone_Number'].apply(lambda x: x[0:3]+'-'+x[3:6]+'-'+x[6:10])
#df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))
#df['Phone_Number']=df['Phone_Number'].apply(lambda x: x[0:3]+'-'+x[3:6]+'-'+x[6:10])
df['Phone_Number'] = df['Phone_Number'].str.replace('nan----','')
df['Phone_Number'] = df['Phone_Number'].str.replace('Na----','')

df['Phone_Number'] = df['Phone_Number'].str.replace('--','-')
df


# In[55]:


#Splitting the street address column into Street_address','State','Zip_Code'
df[['Street_address','State','Zip_Code']]=df['Address'].str.split(',',2, expand=True)
df


# In[59]:


df['Do_Not_Contact'].replace('No', 'N', inplace=True)
df['Do_Not_Contact'].replace('Yes', 'Y', inplace=True)


# In[60]:


df


# In[62]:


#Replacing N/a with NaN 
df = df.replace('N/a','')


# In[67]:


#Dropping Null values in the dataframe
df = df.fillna('')
df


# In[69]:


#dropping all records where 'Do_Not_Contact'=='Y'
for x in df.index:
    if df.loc[x, 'Do_Not_Contact']=='Y':
        df.drop(x, inplace=True)

df    


# In[71]:


#dropping all records with blank phone number
for x in df.index:
    if df.loc[x, 'Phone_Number']=='':
        df.drop(x, inplace=True)

df 


# In[73]:


#Resetting index
df = df.reset_index(drop=True)
df


# In[ ]:




