# Bipin Singh
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import calendar
from datetime import datetime
import seaborn as sns


# In[2]:


bakery_dataset = pd.read_csv("BreadBasket_DMS.csv")
bakery_dataset.dropna()
bakery_dataset = bakery_dataset[bakery_dataset['Item'] != 'NONE']

bakery_dataset['Date'] = pd.to_datetime(bakery_dataset['Date'])
bakery_dataset['Time'] = pd.to_datetime(bakery_dataset['Time'])
bakery_dataset['Year'] = bakery_dataset['Date'].dt.year
bakery_dataset['Month'] = bakery_dataset['Date'].dt.month
bakery_dataset['Day'] = bakery_dataset['Date'].dt.day
bakery_dataset['Weekday'] = bakery_dataset['Date'].dt.weekday
bakery_dataset['Hour'] = bakery_dataset['Time'].dt.hour
# Any results you write to the current directory are saved as output.


# In[3]:


bakery_dataset.head(10)


# In[4]:


bakery_dataset.tail(10)


# In[15]:


def map_indexes_and_values(df, col):
    df_col = df[col].value_counts()
    x = df_col.index.tolist()
    y = df_col.values.tolist()
    return x, y

weekmap = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'}
print('')

# count of the five most popular items
popular_items, popular_items_count = map_indexes_and_values(bakery_dataset, 'Item')
plt.bar(popular_items[:10], popular_items_count[:10])

print("Question 1")
plt.xlabel('Top 10 most popular Items')
plt.ylabel('Number of Transactions')
plt.show()

print("Top 10 most popular items:","\n", popular_items[:10])


# In[14]:


# top items in 2016

print("Question2")
first_year_data = bakery_dataset[bakery_dataset['Year'] == 2016]
x, y = map_indexes_and_values(first_year_data, 'Item')
plt.bar(x[:5], y[:5], color='r', label='2016')
plt.xlabel('Most popular Items')
plt.ylabel('Number of Transactions')
plt.legend()
plt.show()

print("5 most popular items in 2016 is:","\n", first_year_data[:5])


# In[13]:



# top items in 2017
print("Question 3")
second_year_data = bakery_dataset[bakery_dataset['Year'] == 2017]
x, y = map_indexes_and_values(second_year_data, 'Item')
plt.bar(x[:5], y[:5], color='g', label='2017')
plt.xlabel('Most popular Items')
plt.ylabel('Number of Transactions')
plt.legend()
plt.show()

print("5 most popular items in 2017 is:", "\n",second_year_data[:5])


# In[12]:


print("Question 4")
monday_info = bakery_dataset[bakery_dataset['Weekday'] == 0]
item, item_count = map_indexes_and_values(monday_info, 'Item')

plt.bar(item[:5], item_count[:5], color='y', label='Monday')
plt.xlabel('Popular items on Monday')
plt.ylabel('Number of Transactions')
plt.show()

print("5 most popular items sold on monday is:","\n", monday_info[:5])


# In[16]:


print("Question 5")
bakery_dataset.groupby('Month')['Transaction'].nunique().plot(kind='bar', title='Number of items sold per month. ')
plt.xlabel('Months')
plt.ylabel('Number of Transactions')
plt.show()


# In[17]:


print("Question 6")
bakery_dataset.groupby('Weekday')['Transaction'].nunique().plot(kind='bar', title='Number of items sold per weekday.')
plt.xlabel('Days')
plt.ylabel('Number of Transactions')
plt.show()


# In[19]:


print("Question 7")
bakery_dataset.groupby('Hour')['Transaction'].nunique().plot(kind='bar', title='Number of items sold per hour.')
plt.xlabel('Hour')
plt.ylabel('Number of Transactions')
plt.show()


# In[20]:


def coffee_ext(group):
    match = group['Item'].str.contains('Coffee')
    return bakery_dataset.loc[match]

# Let's get the transaction numbers of all the transactions that have coffee.
coffee = bakery_dataset[ bakery_dataset['Item'].str.contains('Coffee')]['Transaction'].unique()


# In[21]:


# Now that we have all the coffee transactions, we can do a left join with coffee
coffee = pd.DataFrame(coffee,columns=['Transaction'])
coffee_m=coffee.merge(bakery_dataset, left_on='Transaction',right_on='Transaction',how='right')
# Remove all the coffee rows, groupby transaction and tally up the items
coffee_m = coffee_m[~coffee_m.Item.str.contains('Coffee')]['Item'].value_counts()


# In[23]:


print("Question 8")
plt.figure(figsize=(10,6))
coffee_m[:5].plot(kind='bar')
plt.show()


# In[24]:


print("Question 9")
bakery_dataset['Date'] = pd.to_datetime(bakery_dataset['Date'], format='%d-%m-%Y', errors='coerce')
bakery_dataset['year'] = bakery_dataset['Date'].dt.year

yearsetup=bakery_dataset.loc[bakery_dataset['year']==2017]

coffee=yearsetup.set_index(['Item'])
onlycoffee=coffee.loc['Coffee']
onlycoffee.reset_index(inplace=True)

popular=onlycoffee['Date'].value_counts()
print(popular.head())
popular.head().plot(kind='line', color='orange', marker='o')
plt.xlabel('Dates')
plt.ylabel('Number of Transactions')
plt.title('Five most Coffee Sales day in 2017.')
plt.show()


# In[30]:
