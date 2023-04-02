#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import pickle


# In[4]:


df = pd.read_csv('Iris.csv')


# In[5]:


df.info()


# In[7]:


df.drop(columns = ['Id'],inplace = True)


# In[9]:


# Splitting the target & independent variables
x = df.iloc[:,:-1].values
y = df.iloc[:,-1].values


# In[12]:


# Splitting the data for training & testing
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.30,random_state = 69)


# In[13]:


# Performing feature scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


# In[14]:


# Building the model
from sklearn.tree import DecisionTreeClassifier

classifier = DecisionTreeClassifier(criterion = 'entropy')
classifier.fit(x_train,y_train)


# In[16]:


# Pickling the model
pickle.dump(classifier,open("model.pkl","wb"))

