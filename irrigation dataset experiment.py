#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import seaborn as sns; sns.set(font_scale=1.2)


# In[31]:


# beans   1
# chilli  2
# potato  3

df = pd.read_csv('new-irrigation.csv')
df


# In[26]:





# In[ ]:





# In[3]:


# Not muh to see here if we use a pairplot
# sns.pairplot(df, hue='Type')


# In[32]:


# Analyzing the data using Categories

sns.catplot(data=df, x="Type", y="Moisture", hue="Status", kind="swarm")

# You can see in this graph that the dataset needs some work.
# There is not much difference between each crop type


# In[5]:


# investigate the data
# df.loc[:, "Moisture"]


# In[33]:


from sklearn.linear_model import LogisticRegression

# Get the data to train the model
X=df.loc[:, ["Type", "Moisture"]]
y=df.loc[:, "Status"]

# Train the model
clf = LogisticRegression(random_state=0).fit(X.values, y.values)


# In[34]:


clf.predict([[1, 35],[2, 40],[3, 50]])


# In[ ]:


# save the model to disk


# In[35]:


import pickle


# In[36]:


filename = 'irrigate_final_model.sav'


# In[37]:


pickle.dump(clf, open(filename, 'wb'))


# In[ ]:





# In[ ]:




