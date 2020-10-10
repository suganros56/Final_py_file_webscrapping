#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd 
import numpy as np
import re as r


# In[3]:


data=pd.read_excel('C:/Users/Roshan/Desktop/Aug 2020 ID VotingFinalResultFromGoogleForm.xlsx')


# In[10]:


data.columns


# In[8]:


pt1='AC'
pt2='ID'


# In[19]:


def pattern(pat1,pat2):
    data['Vo_MC1']=data['Vote (Select maximum 2 drawings to vote. For example  : #ID1, #AC1)'].apply(lambda x:r.findall(pat1+'[0-9][0-9][0-9]?|'+pat1+' [0-9][0-9][0-9]?|'+pat1+'[0-9][0-9]?|'+pat1+' [0-9][0-9]?',x)[0] if r.findall(pat1+'[0-9][0-9][0-9]?|'+pat1+' [0-9][0-9][0-9]?|'+pat1+'[0-9][0-9]?|'+pat1+' [0-9][0-9]?',x)[:2] else 0)
    data['Vo_MC2']=data['Vote (Select maximum 2 drawings to vote. For example  : #ID1, #AC1)'].apply(lambda x:r.findall(pat1+'[0-9][0-9][0-9]?|'+pat1+' [0-9][0-9][0-9]?|'+pat1+'[0-9][0-9]?|'+pat1+' [0-9][0-9]?',x)[1] if r.findall(pat1+'[0-9][0-9][0-9]?|'+pat1+' [0-9][0-9][0-9]?|'+pat1+'[0-9][0-9]?|'+pat1+' [0-9][0-9]?',x)[1:3] else 0)
    data['Vo_MC3']=data['Vote (Select maximum 2 drawings to vote. For example  : #ID1, #AC1)'].apply(lambda x:r.findall(pat1+'[0-9][0-9][0-9]?|'+pat1+' [0-9][0-9][0-9]?|'+pat1+'[0-9][0-9]?|'+pat1+' [0-9][0-9]?',x)[2] if r.findall(pat1+'[0-9][0-9][0-9]?|'+pat1+' [0-9][0-9][0-9]?|'+pat1+'[0-9][0-9]?|'+pat1+' [0-9][0-9]?',x)[2:3] else 0)
    data['Vo_M1']=data['Vote (Select maximum 2 drawings to vote. For example  : #ID1, #AC1)'].apply(lambda x:r.findall(pat2+'[0-9][0-9][0-9]?|'+pat2+' [0-9][0-9][0-9]?|'+pat2+'[0-9][0-9]?|'+pat2+' [0-9][0-9]?',x)[0] if r.findall(pat2+'[0-9][0-9][0-9]?|'+pat2+' [0-9][0-9][0-9]?|'+pat2+'[0-9][0-9]?|'+pat2+' [0-9][0-9]?',x)[:2] else 0)
    data['Vo_M2']=data['Vote (Select maximum 2 drawings to vote. For example  : #ID1, #AC1)'].apply(lambda x:r.findall(pat2+'[0-9][0-9][0-9]?|'+pat2+' [0-9][0-9][0-9]?|'+pat2+'[0-9][0-9]?|'+pat2+' [0-9][0-9]?',x)[1] if r.findall(pat2+'[0-9][0-9][0-9]?|'+pat2+' [0-9][0-9][0-9]?|'+pat2+'[0-9][0-9]?|'+pat2+' [0-9][0-9]?',x)[1:3] else 0)
    data['Vo_M3']=data['Vote (Select maximum 2 drawings to vote. For example  : #ID1, #AC1)'].apply(lambda x:r.findall(pat2+'[0-9][0-9][0-9]?|'+pat2+' [0-9][0-9][0-9]?|'+pat2+'[0-9][0-9]?|'+pat2+' [0-9][0-9]?',x)[2] if r.findall(pat2+'[0-9][0-9][0-9]?|'+pat2+' [0-9][0-9][0-9]?|'+pat2+'[0-9][0-9]?|'+pat2+' [0-9][0-9]?',x)[2:3] else 0)
    data['Num_1']=data['Vote (Select maximum 2 drawings to vote. For example  : #ID1, #AC1)'].apply(lambda x: r.findall('[0-9][0-9][0-9]?| [0-9][0-9][0-9]?|[0-9][0-9]?| [0-9][0-9]?',x)[0] if r.findall('[0-9][0-9][0-9]?| [0-9][0-9][0-9]?|[0-9][0-9]?| [0-9][0-9]?',x)[:2] else 0)
    data['Num_2']=data['Vote (Select maximum 2 drawings to vote. For example  : #ID1, #AC1)'].apply(lambda x: r.findall('[0-9][0-9][0-9]?| [0-9][0-9][0-9]?|[0-9][0-9]?| [0-9][0-9]?',x)[1] if r.findall('[0-9][0-9][0-9]?| [0-9][0-9][0-9]?|[0-9][0-9]?| [0-9][0-9]?',x)[1:3] else 0)
    data['Num_3']=data['Vote (Select maximum 2 drawings to vote. For example  : #ID1, #AC1)'].apply(lambda x: r.findall('[0-9][0-9][0-9]?| [0-9][0-9][0-9]?|[0-9][0-9]?| [0-9][0-9]?',x)[2] if r.findall('[0-9][0-9][0-9]?| [0-9][0-9][0-9]?|[0-9][0-9]?| [0-9][0-9]?',x)[2:3] else 0)
    data['Vo_MC1']=data['Vo_MC1'].str.replace(" ","")
    data['Vo_MC2']=data['Vo_MC2'].str.replace(" ","")
    #data['Vo_MC3']=data['Vo_MC3'].str.replace(" ","")
    data['Vo_M1']=data['Vo_M1'].str.replace(" ","")
    data['Vo_M2']=data['Vo_M2'].str.replace(" ","")
    #data['Vo_M3']=data['Vo_M3'].str.replace(" ","")
pattern(pt1,pt2)  


# In[20]:


data


# In[13]:


data.head(60)


# In[21]:


data['Email address'].unique


# In[22]:


Win_M=data['Vo_M1'].append(data['Vo_M2']).value_counts()
#print('The winners of the competitions are:')
Win_M.sort_values(ascending=False)


# In[23]:


Win_MC=data['Vo_MC1'].append(data['Vo_MC2']).value_counts()
#print('The winners of the competitions are:')
Win_MC.sort_values(ascending=False)


# In[24]:


group_values=list(Win_MC.values)
group_values
group_data=list(Win_MC.keys())
group_data


# In[25]:


group_valM=list(Win_M.values)
group_dataM=list(Win_M.keys())
group_dataM


# In[27]:


#for ID
nns=[]
#for d in range(0,len(group_values),1):
    #nns.append(nss[d])'
    
for i,j in zip(group_dataM,range(0,len(group_valM),1)):
    nss=[]
    for index, row in data.iterrows():
        if i==row['Vo_M1']:
            nss.append(row['Your Name (who is voting)'])
        elif i==row['Vo_M2']:
            nss.append(row['Your Name (who is voting)'])
        elif i==row['Vo_M3']:
            nss.append(row['Your Name (who is voting)'])
    nns.append(nss) 


# In[28]:





# In[30]:


ns=[]
for i,j in zip(group_data,range(0,len(group_values),1)):
    nn=[]           
    for index, row in data.iterrows():
        if i==row['Vo_MC1']:
            nn.append(row['Your Name (who is voting)'])
            #print(row['Vo_MC1'])
        elif i==row['Vo_MC2']:
            nn.append(row['Your Name (who is voting)'])
            #print(row['Vo_MC2'])
        elif i==row['Vo_MC3']:
            #print(row['Vo_MC3'])
            nn.append(row['Your Name (who is voting)'])
    ns.append(nn)          
        
ns


# In[31]:


dic={'Image_id_AC':group_data,'Votes_AC':group_values,'Name_of_voters':ns}
dfAC=pd.DataFrame(dic)
dfAC
dfAC.to_csv('C:/Users/Roshan/Desktop/final1_Aug_30.csv',index=False)


# In[32]:


dic2={'Image_ID':group_dataM,'Votes_ID':group_valM,'Name_of_Voters':nns}
dff=pd.DataFrame(dic2)
dff
dff.to_csv('C:/Users/Roshan/Desktop/final2_Aug_30.csv',index=False)


# In[ ]:




