#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
dataset=  pd.read_csv("analysenow_updatedsales.csv",index_col = False)
dataset=dataset.drop("store",axis=1)
dataset=dataset.drop("Unnamed: 0",axis=1)
dataset=dataset.drop("geometry",axis=1)
Y=dataset.iloc[:,-3:]
spare=[]
for i in Y.iloc[:,0]:
    spare.append(i/100)
dataset['Ratio of Sales']=''
dataset['Ratio of Sales']=spare


# In[2]:


Y['Ratio of Sales']=''
Y['Ratio of Sales']=spare


# In[3]:


X= dataset.iloc[:,:30]


# In[4]:


abc=[]
for i in Y['Ratio of Sales']:
    abc.append(i)
abc.pop()
abc.append(0)


# In[5]:


Y['Ratio of Sales']=''
Y['Ratio of Sales']=abc


# In[6]:





# In[7]:


arr1=[]
for i  in Y['Ratio of Sales']:
    arr1.append(i)
arr2=[]
for i  in Y['Monthly Sales (in Lakhs)']:
    arr2.append(i)
arr3=[]
for i  in Y['Per Day Sales (in Lakhs)']:
    arr3.append(i)    
                


# In[8]:


cat=[]
cols=pd.read_csv("analysenow_updatedsales.csv", nrows=1,index_col = False).columns

cols=cols.drop("Unnamed: 0")
cols=cols.drop("store")
cols=cols.drop("geometry")

for i in cols:
    cat.append(i)


# In[12]:


dic1={}
dic2={}
num=0
for i in X:
        dic1[i]=num
        num+=1       
for i in Y:
        dic2[i]=num
        num+=1        


# In[27]:


import numpy
#numpy.corrcoef(x, y)[0, 1]
final=[]
for inp1 in dic2:
    for inp2 in dic1:
        
        cat1=dic2[inp1]
        cat2=dic1[inp2]
        ax=[]
        ay=[]
        for i in X[inp2]:
            ax.append(i)
        for i in Y[inp1]:
            ay.append(i)   
        #final.append(numpy.corrcoef(x, y)[0, 1])  


# In[127]:


import pandas
df1=pd.DataFrame(columns=['X1','Y1','Pearson'])
df2=pd.DataFrame(columns=['X1','Y1','Pearson'])
df3=pd.DataFrame(columns=['X1','Y1','Pearson'])
finaldf=pd.DataFrame(columns=['X1','Y1','Pearson'])


# In[128]:


df1['X1']=dic1.keys()
df2['X1']=dic1.keys()
df3['X1']=dic1.keys()




# In[133]:


finaldf=pd.concat([df1,df2,df3]).reset_index()


# In[134]:


for i in range(len(dic1.keys())):
    df1['Y1']='Ratio of Sales'
    df2['Y1']='Monthly Sales (in Lakhs)'
    df3['Y1']='Per Day Sales (in Lakhs)'


finaldf['Pearson']=final
#finaldf.to_csv('final.csv')
