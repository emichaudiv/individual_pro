#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[2]:


#Importing Scripts


# In[3]:


df = pd.read_csv('supply_chain_data.csv')


# In[4]:


#Importing Data


# In[5]:


df.head()


# In[6]:


#It would appear that there was no need to fix any nulls as all data relevant to my project is accounted for


# In[7]:


df.shape


# In[8]:


del df['Lead times']
del df['Customer demographics']
del df['Transportation modes']
del df['Routes']
del df['Shipping carriers']
del df['Location']
del df['Lead time']
del df['Stock levels']
del df['Order quantities']
del df['Availability']
del df['Shipping times']


# In[9]:


#Removing what isn't relavent to what I'm looking for


# In[10]:


df


# In[11]:


# I have decided to find the best supplier to work with, I will figure out what factors would help determine that


# In[12]:


sns.barplot(x='Supplier name', y='Defect rates', data=df)
plt.show()


# In[13]:


def supplier_defect():
    sns.barplot(x='Supplier name', y='Defect rates', data=df)
    plt.show()


# In[14]:


# 1 seems to have the lowest defect rate while 5 is the highest


# In[15]:


sns.barplot(x='Supplier name', y='Number of products sold', data=df)
plt.show()


# In[16]:


def supplier_sold():
    sns.barplot(x='Supplier name', y='Number of products sold', data=df)
    plt.show()


# In[17]:


# 3 has sold more units and 4 sold the least with 1 not far behind


# In[18]:


sns.barplot(x='Supplier name', y='Revenue generated', data=df)
plt.show()


# In[19]:


def supplier_revenue():
    sns.barplot(x='Supplier name', y='Revenue generated', data=df)
    plt.show()


# In[20]:


# 3 generates the most revenue while 4 generates the least


# In[21]:


sns.barplot(x='Supplier name', y='Manufacturing costs', data=df)
plt.show()


# In[22]:


def supplier_manu_cost():
    sns.barplot(x='Supplier name', y='Manufacturing costs', data=df)
    plt.show()


# In[23]:


# all but 4 seem to be close in being the cheapest with costs with 2 being near the cheapest while two is the most expensive


# In[24]:


sns.barplot(x='Supplier name', y='Manufacturing lead time', data=df)
plt.show()


# In[25]:


def supplier_manu_time():
    sns.barplot(x='Supplier name', y='Manufacturing lead time', data=df)
    plt.show()


# In[26]:


# 1 takes the least amount of time while 5 takes more time to produce


# In[27]:


sns.barplot(x='Supplier name', y='Shipping costs', data=df)
plt.show()


# In[28]:


def supplier_shipping():
    sns.barplot(x='Supplier name', y='Shipping costs', data=df)
    plt.show()


# In[29]:


# 3 has cheaper shipping while 2,4,5 have higher costs


# In[30]:


sns.barplot(x='Supplier name', y='Costs', data=df)
plt.show()


# In[31]:


def supplier_cost():
    sns.barplot(x='Supplier name', y='Costs', data=df)
    plt.show()


# In[32]:


# 3 has cheapest total costs while 1 has the highest 


# In[33]:


sns.barplot(x='Supplier name', y='Production volumes', data=df)
plt.show()


# In[34]:


def supplier_volume():
    sns.barplot(x='Supplier name', y='Production volumes', data=df)
    plt.show()


# In[35]:


# 2,4 produce more products while 1 makes less


# In[36]:


#Final results:
#1:+ less defects, quick producing. - Low revenue, Most costly, produces less volumes
#2:+ cheap manufacturing, most volumes. - Costly shipping
#3:+ sells more units, most profitable, cheap shipping, lowest overall costs. - second highest defect in comparison
#4:+ Makes more units. - Lowest number of units sold, lowest revenue, highest manufacturing costs, high shipping
#5:+ ... - Highest defect rate, high shipping


# In[37]:


sns.barplot(x='Supplier name', y='Price', data=df)
plt.show()


# In[38]:


def supplier_price():
    sns.barplot(x='Supplier name', y='Price', data=df)
    plt.show()


# In[39]:


# Supplier 3 would be a great choice to work with as costs to produce are low and sales are high
# Supplier 4 should be avoided as their product has the highest costs to produce/ship with small returns
# 1 has their products sold at higher prices while 5 and 3 also sold slightly cheaper than 2 and 4


# In[40]:


sup3 = df[df["Supplier name"] == 'Supplier 3']


# In[41]:


#Making it all about Supplier 3


# In[42]:


sup3


# In[43]:


#Next I'm going to see what is their most proitable product and see it's costs, maybe offer a way to help the others
#Will be repeating what was done before.


# In[44]:


sns.barplot(x='Product type', y='Price', data=sup3)
plt.show()


# In[45]:


def price():
    sns.barplot(x='Product type', y='Price', data=sup3)
    plt.show()


# In[46]:


sns.barplot(x='Product type', y='Number of products sold', data=sup3)
plt.show()


# In[47]:


def number_sold():
    sns.barplot(x='Product type', y='Number of products sold', data=sup3)
    plt.show()


# In[48]:


sns.barplot(x='Product type', y='Revenue generated', data=sup3)
plt.show()


# In[49]:


def revenue():
    sns.barplot(x='Product type', y='Revenue generated', data=sup3)
    plt.show()


# In[50]:


sns.barplot(x='Product type', y='Shipping costs', data=sup3)
plt.show()


# In[51]:


def shipping():
    sns.barplot(x='Product type', y='Shipping costs', data=sup3)
    plt.show()


# In[52]:


sns.barplot(x='Product type', y='Production volumes', data=sup3)
plt.show()


# In[53]:


def product_volume():
    sns.barplot(x='Product type', y='Production volumes', data=sup3)
    plt.show()


# In[54]:


sns.barplot(x='Product type', y='Manufacturing lead time', data=sup3)
plt.show()


# In[55]:


def manu_time():
    sns.barplot(x='Product type', y='Manufacturing lead time', data=sup3)
    plt.show()


# In[56]:


sns.barplot(x='Product type', y='Manufacturing costs', data=sup3)
plt.show()


# In[57]:


def manu_cost():
    sns.barplot(x='Product type', y='Manufacturing costs', data=sup3)
    plt.show()


# In[58]:


sns.barplot(x='Product type', y='Costs', data=sup3)
plt.show()


# In[59]:


def product_cost():
    sns.barplot(x='Product type', y='Costs', data=sup3)
    plt.show()


# In[60]:


sns.barplot(x='Product type', y='Defect rates', data=sup3)
plt.show()


# In[61]:


def defect():
    sns.barplot(x='Product type', y='Defect rates', data=sup3)
    plt.show()


# In[62]:


#The most popular product would be their cosmetics as it is priced lowest while also the cheapest to produce.
# It may take longer to produce and is prone to more defects, but it does offer more content per volume.
#haircare, while not terrible, could be selling more, perhaps it is due to the asking price for the product?
# One solution would be to sell at a lower price while also producting more, perhaps maybe increasing the amount
#the product can offer. The defect rate is much lower to the other products.


# In[63]:


#Let's say it's been approved to produce more haircare products, what would the rate be to avoid defects?


# In[64]:


train_size = int(round(sup3.shape[0] * 0.5))
train_size


# In[65]:


validate_size = int(round(sup3.shape[0] * 0.3))
validate_size


# In[66]:


test_size = int(round(sup3.shape[0] * 0.2))
test_size


# In[67]:


validate_end_index = train_size + validate_size
validate_end_index


# In[68]:


#Dividing and checking if the train, test and validate are equal to what Supplier 3 is working with


# In[69]:


train = sup3[:train_size]


# In[70]:


validate = sup3[train_size:validate_end_index]


# In[71]:


test = sup3[validate_end_index:]


# In[72]:


for col in train.columns:
    plt.plot(train[col])
    plt.plot(validate[col])
    plt.plot(test[col])
    plt.ylabel(col)
    plt.title(col)
    plt.show()


# In[73]:


plt.plot(train['Defect rates'])
plt.plot(validate['Defect rates'])
plt.plot(test['Defect rates'])
plt.show()


# In[74]:


def defect_predict():
    plt.plot(train['Defect rates'])
    plt.plot(validate['Defect rates'])
    plt.plot(test['Defect rates'])
    plt.show()


# In[75]:


#Supplier 3 makes the best products at a cheap price. They make great cosmetics and can be sold for a large profit
#They could improve they sales of their haircare by perhaps making more, adding to the existing products, and 
#lower the sales price. Making more would create them with a generally same quallity. 

