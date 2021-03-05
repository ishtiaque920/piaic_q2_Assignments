#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import glob


# In[5]:


files = glob.glob(r'C:\Users\Ishtiaque Hussain\Desktop\states'"./*.csv")


us_census = []

for filename in files:
    data = pd.read_csv(filename, index_col=None, header=0)
    us_census.append(data)
    
us_census = pd.concat(us_census)


# In[6]:


print(us_census.columns)
print(us_census.dtypes)


# In[7]:


us_census.head()


# In[8]:


#removing the $
us_census.Income = us_census["Income"].replace("[\$,]","", regex = True)

#converting to number
us_census.Income = pd.to_numeric(us_census.Income)


# In[ ]:



#splitting GenderPop column into Men and Women


# In[9]:


us_census["str_split"] = us_census["GenderPop"].str.split("_")
us_census["Men"] = us_census.str_split.str.get(0)
us_census["Women"] = us_census.str_split.str.get(1)


# In[10]:


#removeing the M and the F so we can convert the data to number for plotting
us_census.Men = us_census["Men"].replace("[M]","", regex = True)
us_census.Women = us_census["Women"].replace("[F]","", regex = True)


# In[11]:


#converting to number
us_census.Men = pd.to_numeric(us_census.Men)
us_census.Women = pd.to_numeric(us_census.Women)
us_census.head()


# In[12]:


print(us_census.dtypes)


# In[13]:


#filling NAN in women column: Women = TotalPop - Men
us_census = us_census.fillna(value={"Women":us_census.TotalPop - us_census.Men})

#print(us_census)
us_census


# In[ ]:





# In[14]:


#removing duplicates
new_census = us_census.drop_duplicates(["State"])
print(new_census)


# In[15]:


#scatterplot
pyplot.scatter(new_census.Men, new_census.Income)
pyplot.scatter(new_census.Women, new_census.Income)
pyplot.show()


# In[43]:


#Creating histogram for each of the races


# In[16]:


new_census.Hispanic = new_census["Hispanic"].replace("[\%,]","", regex = True)
new_census.White = new_census["White"].replace("[\%,]","", regex = True)
new_census.Black = new_census["Black"].replace("[\%,]","", regex = True)
new_census.Native = new_census["Native"].replace("[\%,]","", regex = True)
new_census.Asian = new_census["Asian"].replace("[\%,]","", regex = True)
new_census.Pacific = new_census["Pacific"].replace("[\%,]","", regex = True)

new_census.Hispanic = pd.to_numeric(new_census.Hispanic)
new_census.White = pd.to_numeric(new_census.White)
new_census.Black = pd.to_numeric(new_census.Black)
new_census.Native = pd.to_numeric(new_census.Native)
new_census.Asian = pd.to_numeric(new_census.Asian)
new_census.Pacific = pd.to_numeric(new_census.Pacific)

print(new_census.dtypes)


# In[17]:


pyplot.hist(new_census.Hispanic)
pyplot.show()

pyplot.hist(new_census.White)
pyplot.show()

pyplot.hist(new_census.Black)
pyplot.show()

pyplot.hist(new_census.Native)
pyplot.show()

pyplot.hist(new_census.Asian)
pyplot.show()

pyplot.hist(new_census.Pacific)
pyplot.show()


# #PART 2 
# #Petal Power Inventory

# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot


# In[19]:


inventory = pd.read_csv('inventory/inventory.csv')


# In[20]:


inventory.head(10)


# In[21]:


staten_island = inventory.head(10)


# In[22]:


staten_island


# In[23]:


product_request = staten_island.product_description 


# In[24]:


product_request


# In[25]:


seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]


# In[26]:


seed_request


# In[27]:


inventory["in_stock"] = inventory.apply(lambda row: True if row.quantity > 0 else False, axis = 1)


# In[32]:


inventory


# In[33]:


inventory["total_value"] = inventory.apply(lambda row: row.price * row.quantity, axis = 1) 


# In[35]:


inventory


# In[36]:


combine_lambda = lambda row:     '{} - {}'.format(row.product_type,
                     row.product_description)


# In[37]:


inventory['full_description'] = inventory.apply(combine_lambda, axis = 1)


# In[38]:


inventory


# In[ ]:




