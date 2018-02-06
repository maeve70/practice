
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib inline')


# In[2]:

import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import seaborn as sns


# In[3]:

df = pd.read_csv('database.csv', low_memory=False)


# In[4]:

df.head()


# In[5]:

df.columns


# In[6]:

df = pd.read_csv('database.csv', low_memory=False,
                na_values=['UNKNOWN', 'NaN'],
                na_filter=True,
                skip_blank_lines=True)


# In[7]:

subset_list = ['Incident Year',
              'Incident Month',
              'Incident Day',
              'Operator',
              'Airport',
              'State',
              'Flight Phase',
              'Species Name']


# In[8]:

df = pd.DataFrame(data=df, columns=subset_list)


# In[9]:

df.head(10)


# In[10]:

df.rename(columns={'Incident Year': 'Incident_Year', 
                   'Incident Month': 'Incident_Month', 
                   'Incident Day': 'Incident_Day', 'Flight Phase': 'Flight_Phase',
                   'Species Name': 'Species_Name'}, inplace=True)


# In[31]:

#thresh=8 means to Drop row if it does not have at least eight values that are **not** NaN

df = df.dropna(thresh=8)

# ...and resetting the index bc of the rows that are dropped.
df = df.reset_index(drop=True)


# In[32]:

df.head(10)


# In[33]:

df["Operator"].value_counts().head(10)


# In[14]:




# In[15]:

df['Operator'].value_counts().head()


# In[16]:

# Get the numnber of occurances of each operator
operator_counts = df.Operator.value_counts()


# In[17]:

# Split and Save the Operator names in a variable

operators = operator_counts.index


# In[18]:

# Split and Save the counts in another variable

counts = operator_counts.get_values()


# In[19]:

#create barplot object that's not very pretty b/c there are too many operators.
barplot = sns.barplot(x=operators, y=counts)


# In[20]:

#result if i limit the x and y values by taking a slice or subset of df. still need to rotate the xticks.
barplot = sns.barplot(x=operators[:11], y=counts[:11])


# In[21]:

#use rotation
plt.xticks(rotation=90)

barplot = sns.barplot(x=operators[:15], y=counts[:15])
my_palette = sns.color_palette('hls')
sns.set_palette(my_palette, 20)
plt.xlabel("Airline-Operator", fontsize=20)
plt.ylabel("Number of Birdstrikes", fontsize=20)
plt.title("Birdstrikes Per Airline Operator", fontsize=20)


# In[22]:

df["Airport"].value_counts().head(10)


# In[23]:

airport_counts = df.Airport.value_counts()


# In[24]:

airports = airport_counts.index


# In[34]:

counts = airport_counts.get_values()


# In[35]:

#barplot = sns.barplot(x=airports, y=counts)


# In[27]:

#barplot = sns.barplot(x=airports[:10], y=counts[:10])
#plt.xticks(rotation=90)


# In[28]:

plt.xticks(rotation=90)

barplot = sns.barplot(x=airports[:15], y=counts[:15])
my_palette = sns.color_palette('bright')
sns.set_palette(my_palette, 15)
plt.xlabel("Airports", fontsize=20)
plt.ylabel("Number of Birdstrikes", fontsize=20)
plt.title("Birdstrikes Per Airport", fontsize=20)


# In[29]:

df["Incident_Year"].value_counts().head(10)


# In[36]:

Incident_Year_counts = df.Incident_Year.value_counts()


# In[37]:

Incident_Year = Incident_Year_counts.index


# In[38]:

counts = Incident_Year_counts.get_values()


# In[50]:

#sns.barplot(x=Incident_Year, y=counts)


# In[ ]:




# In[41]:

plt.xticks(rotation=90)

barplot = sns.barplot(x=Incident_Year[:10], y=counts[:10])
my_palette = sns.color_palette('hls', 10)
sns.set_palette(my_palette, 10)
plt.xlabel("Year", fontsize=20)
plt.ylabel("Number of Birdstrikes", fontsize=20)
plt.title("Birdstrikes Per Year", fontsize=20)


# In[30]:

df["Species_Name"].value_counts().head(10)


# In[43]:

species_name_counts = df.Species_Name.value_counts()


# In[44]:

species_name = species_name_counts.index


# In[45]:

counts = species_name_counts.get_values()


# In[47]:

#sns.barplot(x=species_name, y=counts)


# In[49]:

plt.xticks(rotation=90)
barplot = sns.barplot(x=species_name[:10], y=counts[:10])
my_palette = sns.color_palette('pastel')
sns.set_palette(my_palette, 10)
plt.xlabel("Bird Species", fontsize=20)
plt.ylabel("Number of Deaths Per Year", fontsize=20)
plt.title("Bird Species Involved in Birdstrikes")







# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



