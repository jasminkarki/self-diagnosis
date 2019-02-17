
# coding: utf-8

# In[16]:


import numpy as nd
import pandas as pd


# In[17]:


#data=pd.read_excel("C:/Users/Justin Karki/Desktop/hepatitis.xlsx")
data=pd.read_csv("C:/Users/Justin Karki/Desktop/hepatitis_csv.csv")


# In[5]:


#data.head() #Gives head datas. 
    #We can use head(n) where n is the first n datas.
#data.tail(10) #Gives the tail datas. 
    #Using tail(n) n is the last n datas.
#print(data.info())
#data.describe()
#data['steroid'].value_counts()
#data['steroid'].value_counts(normalize=True)
#data.sort_values(by='age',ascending=True)
#data['steroid'].fillna(False,inplace=True)
#data['bilirubin'].value_counts()
#data['bilirubin'].describe()
#data['bilirubin'].mean()
#data['bilirubin'].mode()
#data['alk_phosphate'].mean()
#data['alk_phosphate'].median()
#data['alk_phosphate'].describe()
#data['class'].describe()
#loc and iloc uses
#data.iloc[0:5]  #First five rows of the data
#data.loc[0]
#data.iloc[:,-1] #First column of the data frame
#Similarly 
#data.loc[55] #Row with index value 55
#data.iloc[3:12,2:10] #data.iloc[<row_selection>,<column_selection>]
#Rows:3 to 12 in array
#Columns: 2 to 10
#data.iloc[:,1:3]

#data[data['alk_phosphate'].isnull()].count()
#data[(data['sex']=='male')& (data['age']>30)]

#for x in range(len(l_columns)):
 #   d = data[l_columns[x]][0]
  #  if(d == True or d == False):
   #     data[l_columns[x]] = data[l_columns[x]].apply(transform)#
#print(data)


# In[6]:


import numpy as np
l_columns = data.columns.tolist()
print(l_columns)
array_columns=np.array(l_columns)
j=len(array_columns)
print(j)


# In[7]:


def transforml(x):
    if x=='male' or x=='live':
        return 1
    if x=="female" or x=="die":
        return 0
    
def transform(x):
    return 1 if x else 0


# In[8]:


data["sex"]=data["sex"].apply(transforml)    
data["steroid"]=data["steroid"].apply(transform)    
data["antivirals"]=data["antivirals"].apply(transform)  
data["fatigue"]=data["fatigue"].apply(transform)    
data["malaise"]=data["malaise"].apply(transform)    
data["anorexia"]=data["anorexia"].apply(transform)    
data["liver_big"]=data["liver_big"].apply(transform)    
data["liver_firm"]=data["liver_firm"].apply(transform)    
data["spleen_palpable"]=data["spleen_palpable"].apply(transform)    
data["spiders"]=data["spiders"].apply(transform) 
data["ascites"]=data["ascites"].apply(transform)    
data["varices"]=data["varices"].apply(transform)
data["histology"]=data["histology"].apply(transform)    
data["class"]=data["class"].apply(transforml)   


# In[9]:


data


# In[10]:


data['sgot'].fillna(22.5,inplace=True)
data['bilirubin'].fillna(0.7,inplace=True)
data['alk_phosphate'].fillna(80,inplace=True)
data['albumin'].fillna(4.25,inplace=True)
data['protime'].fillna(12,inplace=True)


# In[11]:


data


# In[12]:


pd.options.mode.chained_assignment = None
def Scaling_data(col_name):
    
    max_val=max(data[col_name])
    min_val=min(data[col_name])
    
    for i in range(len(data)):
        data[col_name][i]=(data[col_name][i]-min_val)/(max_val-min_val)
        data[col_name][i]="{0:.4f}".format(data[col_name][i])
        
    return data[col_name]
        


# In[13]:


Bilirubin_Scaled=Scaling_data("bilirubin")
Alkaline_Scaled=Scaling_data("alk_phosphate")
Sgot_Scaled=Scaling_data("sgot")
Protime_Scaled=Scaling_data("protime")
Albumin_Scaled=Scaling_data("albumin")
Age_Scaled=Scaling_data("age")


# In[14]:


data


# In[15]:


writer = pd.ExcelWriter('C:/Users/Justin Karki/Desktop/output_hepatitis.xlsx')
data.to_excel(writer,'Sheet1')
writer.save()

