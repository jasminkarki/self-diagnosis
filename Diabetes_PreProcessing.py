
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np


# In[18]:


data=pd.read_csv("C:/Users/Justin Karki/Desktop/diabetes_csv.csv")


# In[ ]:


def Scaling_data(col_name):
    
    max_Val=max(data[col_name])
    min_Val=min(data[col_name])
    
    for i in range(len(data)):
        data[col_name][i]=(data[col_name][i]-float(min_Val))/(float(max_Val)-float(min_Val))
        data[col_name][i]="{:0.4f}".format(data[col_name][i])
        
    return data[col_name]

PregnanciesS=Scaling_data("Pregnancies")
GlucoseS=Scaling_data("Glucose")
BloodPressureS=Scaling_data("BloodPressure")
SkinThicknessS=Scaling_data("SkinThickness")
InsulinS=Scaling_data("Insulin")
BMIS=Scaling_data("BMI")
DiabetesPedigreeFunctionS=Scaling_data("DiabetesPedigreeFunction")
AgeS=Scaling_data("Age")
    


# In[ ]:


#from sklearn import preprocessing
#data[["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]=preprocessing.scale(data[["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]])


# In[ ]:


data


# In[ ]:


writer = pd.ExcelWriter('C:/Users/Justin Karki/Desktop/output_diabetes.xlsx')
data.to_excel(writer,'Sheet1')
writer.save()

