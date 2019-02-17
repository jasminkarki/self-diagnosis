
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB


# In[6]:


data=pd.read_excel("C:/Users/Justin Karki/Desktop/output_hepatitis.xlsx")
#data=pd.read_csv("C:/Users/Justin Karki/Desktop/hepatitis_csv.csv")


# In[7]:


target_data=data['class'] #To delete the result to be found
del data['class']         #deleted
data=data.values          #New data is array for of (previous data-class)
target_data=target_data.values  #Array for actual target value


# In[8]:


model=GaussianNB()           #Object of Gaussian function
model.fit(data,target_data)  #Object used to fit datas
expected=target_data         #Copy of data
predicted=model.predict(data)
confusion_matrix=metrics.confusion_matrix(expected,predicted)
accuracy=(confusion_matrix[0][0]+confusion_matrix[1][1])/(len(data))

print(confusion_matrix)
print(accuracy*100)

