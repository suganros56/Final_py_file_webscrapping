#!/usr/bin/env python
# coding: utf-8

# # ipython nbconvert --to=python [HealthyKID_post_august].ipynb

# In[50]:


import requests
import bs4 as BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = Options()
#option.add_argument("--headless")
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

driver = webdriver.Chrome(chrome_options=option)


# In[151]:


file=open('C:/Users/Roshan/Desktop/testingtext.txt','r')


# In[152]:


file.seek(0)
usname=file.readline()
usname[9:-1]
password=file.readline()
password[9:-1]


# In[153]:


url=file.readline()
url=url[4:-1]


# In[154]:


pat1=file.readline()
pat1[5:-1]
pt1=str(pat1[5:-1])
pt1


# In[155]:


pat2=file.readline()
pat2[5:]
pt2=str(pat2[5:-1])
pt2


# In[156]:


path1=file.readline()
path1=path1[6:-1]
path1
path2=file.readline()
path2=path2[6:-1]
path2
path3=file.readline()
path3=path3[6:-1]
path3
img1=file.readline()
img1=img1[5:-1]
img2=file.readline()
img2=img2[5:-1]
img2
final1=file.readline()
final1=final1[7:-1]
final2=file.readline()
final2=final2[7:-1]
final2
num=file.readline()
num=num[15:]
num


# In[57]:


driver.get(url)


# In[58]:


username=driver.find_element_by_xpath('//*[@id="email"]')
username.send_keys(usname[9:-1])
pw=driver.find_element_by_xpath('//*[@id="pass"]')
pw.send_keys(password[9:-1])
driver.find_element_by_xpath('//*[@id="loginbutton"]').click()


# In[59]:


#clicking the newest to oldest comments
time.sleep(10)
#driver.execute_script("scroll(0, 0);")
#time.sleep(5)
#clicking the newest to oldest comments
#ele=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[3]/div/div/div[1]/div/div[4]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[5]/div/div/div[2]/div[2]/div/div/span')
ele=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[5]/div/div/div[2]/div[2]/div/div')
driver.execute_script("arguments[0].click();", ele)
time.sleep(10)
element=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div')
driver.execute_script("arguments[0].click();", element)


# In[ ]:





# In[61]:


#x=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[5]/div/div/div[2]/div[3]/div[2]/span').text
#num=x[-4:]
loop=int((int(num)/50))+2
print(loop)


# In[62]:


#for clicking the view comments multiple times
import time
time.sleep(10)
for i in range(1,loop,1):
    #driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[5]/div/div/div[2]/div[3]/div[1]/div[2]').click()
    el=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[5]/div/div/div[2]/div[3]/div[1]/div[2]')
    driver.execute_script("arguments[0].click();", el)
    time.sleep(8)
    print(i)


# In[ ]:





# In[63]:


names=[]
comment=[]
links=[]
def scrape():
    for i in range(1,int(num)):
        try:
            nm=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[5]/div/div/div[2]/ul/li['+str(i)+']/div[1]/div/div[2]/div/div[1]/div/div/div/div/div[1]/a/span/span').text
            names.append(nm)
        except:
            names.append('NO text')
        try:
            co=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[5]/div/div/div[2]/ul/li['+str(i)+']/div[1]/div/div[2]/div/div[1]/div/div/div/div/div[2]/span/div/div').text
            comment.append(co)
        except:
            comment.append('No text')
        try:
            lk=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[5]/div/div/div[2]/ul/li['+str(i)+']/div[1]/div/div[2]/div/div[1]/div/div/div/div/div[1]/a').get_attribute('href')
            links.append(lk)
        except:
            links.append('NO link')
        
        
scrape()    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[64]:


import pandas as pd
dic={'Name':names,'Comments':comment,'Link':links}
sol1=pd.DataFrame(dic)


# In[65]:


sol1


# In[66]:


sol1.to_csv(path1,index=False)


# In[67]:


data=pd.read_csv(path1)


# In[68]:


data


# In[69]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re as r


# In[70]:


data['CAP']=data['Comments'].str.upper()


# In[71]:


def pattern(pat1,pat2):
    data['Vo_MC1']=data['CAP'].apply(lambda x:r.findall(pat1+'[0-9][0-9][0-9]?|'+pat1+' [0-9][0-9][0-9]?|'+pat1+'[0-9][0-9]?|'+pat1+' [0-9][0-9]?',x)[0] if r.findall(pat1+'[0-9][0-9][0-9]?|'+pat1+' [0-9][0-9][0-9]?|'+pat1+'[0-9][0-9]?|'+pat1+' [0-9][0-9]?',x)[:2] else 0)
    data['Vo_MC2']=data['CAP'].apply(lambda x:r.findall(pat1+'[0-9][0-9][0-9]?|'+pat1+' [0-9][0-9][0-9]?|'+pat1+'[0-9][0-9]?|'+pat1+' [0-9][0-9]?',x)[1] if r.findall(pat1+'[0-9][0-9][0-9]?|'+pat1+' [0-9][0-9][0-9]?|'+pat1+'[0-9][0-9]?|'+pat1+' [0-9][0-9]?',x)[1:3] else 0)
    data['Vo_MC3']=data['CAP'].apply(lambda x:r.findall(pat1+'[0-9][0-9][0-9]?|'+pat1+' [0-9][0-9][0-9]?|'+pat1+'[0-9][0-9]?|'+pat1+' [0-9][0-9]?',x)[2] if r.findall(pat1+'[0-9][0-9][0-9]?|'+pat1+' [0-9][0-9][0-9]?|'+pat1+'[0-9][0-9]?|'+pat1+' [0-9][0-9]?',x)[2:3] else 0)
    data['Vo_M1']=data['CAP'].apply(lambda x:r.findall(pat2+'[0-9][0-9][0-9]?|'+pat2+' [0-9][0-9][0-9]?|'+pat2+'[0-9][0-9]?|'+pat2+' [0-9][0-9]?',x)[0] if r.findall(pat2+'[0-9][0-9][0-9]?|'+pat2+' [0-9][0-9][0-9]?|'+pat2+'[0-9][0-9]?|'+pat2+' [0-9][0-9]?',x)[:2] else 0)
    data['Vo_M2']=data['CAP'].apply(lambda x:r.findall(pat2+'[0-9][0-9][0-9]?|'+pat2+' [0-9][0-9][0-9]?|'+pat2+'[0-9][0-9]?|'+pat2+' [0-9][0-9]?',x)[1] if r.findall(pat2+'[0-9][0-9][0-9]?|'+pat2+' [0-9][0-9][0-9]?|'+pat2+'[0-9][0-9]?|'+pat2+' [0-9][0-9]?',x)[1:3] else 0)
    data['Vo_M3']=data['CAP'].apply(lambda x:r.findall(pat2+'[0-9][0-9][0-9]?|'+pat2+' [0-9][0-9][0-9]?|'+pat2+'[0-9][0-9]?|'+pat2+' [0-9][0-9]?',x)[2] if r.findall(pat2+'[0-9][0-9][0-9]?|'+pat2+' [0-9][0-9][0-9]?|'+pat2+'[0-9][0-9]?|'+pat2+' [0-9][0-9]?',x)[2:3] else 0)
    data['Num_1']=data['CAP'].apply(lambda x: r.findall('[0-9][0-9][0-9]?| [0-9][0-9][0-9]?|[0-9][0-9]?| [0-9][0-9]?',x)[0] if r.findall('[0-9][0-9][0-9]?| [0-9][0-9][0-9]?|[0-9][0-9]?| [0-9][0-9]?',x)[:2] else 0)
    data['Num_2']=data['CAP'].apply(lambda x: r.findall('[0-9][0-9][0-9]?| [0-9][0-9][0-9]?|[0-9][0-9]?| [0-9][0-9]?',x)[1] if r.findall('[0-9][0-9][0-9]?| [0-9][0-9][0-9]?|[0-9][0-9]?| [0-9][0-9]?',x)[1:3] else 0)
    data['Num_3']=data['CAP'].apply(lambda x: r.findall('[0-9][0-9][0-9]?| [0-9][0-9][0-9]?|[0-9][0-9]?| [0-9][0-9]?',x)[2] if r.findall('[0-9][0-9][0-9]?| [0-9][0-9][0-9]?|[0-9][0-9]?| [0-9][0-9]?',x)[2:3] else 0)
    #data['Vo_MC1']=data['Vo_MC1'].str.replace(" ","")
    #data['Vo_MC2']=data['Vo_MC2'].str.replace(" ","")
    #data['Vo_MC3']=data['Vo_MC3'].str.replace(" ","")
    #data['Vo_M1']=data['Vo_M1'].str.replace(" ","")
    #data['Vo_M2']=data['Vo_M2'].str.replace(" ","")
    #data['Vo_M3']=data['Vo_M3'].str.replace(" ","")
pattern(pt1,pt2)  


# In[72]:


data.tail(20)


# In[80]:


data.to_csv(path2,index=False)


# In[81]:


#data.drop_duplicates(subset='CAP',keep='last',inplace=True)


# In[82]:


data.drop_duplicates(['Name','Vo_MC1','Vo_MC2','Vo_MC3','Vo_M1','Vo_M2','Vo_M3'],inplace=True)


# In[83]:


df=pd.DataFrame(data.Name.value_counts())
ctr=0
for i in range(0,len(df),1):
    if df.values[i]!=1:
        ctr+=1
        print(ctr)


# In[84]:


a=[]
for i in df.index[:ctr]:
    b=[]
    for index, row in data.iterrows():
        if i==row['Name']:
            b.append(index)
        else:
            None
            
    a.append(b)
        
            
print(a)   


# In[183]:


c=[]
for i in a:
    c.append(i[-1])
for i,j in zip(c,a):
    print(i,j)
    if (len(j)>2)&(data['Vo_MC1'][i]!=data['Vo_MC1'][j[1]])&(data['Vo_M1'][i]!=data['Vo_M1'][j[1]]):
        data['Vo_MC2'][i]=data['Vo_MC1'][j[1]]
        data['Vo_MC3'][i]=data['Vo_MC1'][j[0]]
        data['Vo_MC3'][i]=data['Vo_MC2'][j[1]]
        data['Vo_M2'][i]=data['Vo_M1'][j[1]]
        data['Vo_M2'][i]=data['Vo_M1'][j[0]]
        data['Vo_M3'][i]=data['Vo_M2'][j[1]]
    elif (len(j)>2)&(data['Vo_MC1'][i]==data['Vo_MC1'][j[1]])&(data['Vo_M1'][i]==data['Vo_M1'][j[1]]):
        data['Vo_MC2'][i]=data['Vo_MC2'][j[0]]
        data['Vo_MC3'][i]=data['Vo_MC3'][j[1]]
        data['Vo_M2'][i]=data['Vo_M2'][j[0]]
        data['Vo_M2'][i]=data['Vo_M3'][j[1]]
    elif (2>len(j)>1)&(data['Vo_MC1'][i]!=data['Vo_MC1'][j[0]])&(data['Vo_M1'][i]!=data['Vo_M1'][j[0]]):
        data['Vo_MC1'][i]=data['Vo_MC1'][j[0]]
        data['Vo_M1'][i]=data['Vo_M1'][j[0]]
    elif (2>len(j)>1)&(data['Vo_MC1'][i]==data['Vo_MC1'][j[0]])&(data['Vo_M1'][i]==data['Vo_M1'][j[0]]):
        data['Vo_MC2'][i]=data['Vo_MC2'][j[0]]
        data['Vo_MC3'][i]=data['Vo_MC3'][j[0]]
        data['Vo_M2'][i]=data['Vo_M2'][j[0]]  
        data['Vo_M3'][i]=data['Vo_M3'][j[0]]


# In[85]:


q=data.loc[( data['Vo_MC1'].notnull() ) & ( data['Vo_MC2'].isnull() ) & ( data['Num_2']!=0 ) & ( data['Vo_M2'].isnull())].index
#=str(data['Vo_MC1'][data.index])[:2]+(str(data['Num_2'][data.index]))
ks=data.loc[( data['Vo_MC1'].notnull() )&( data['Vo_M1'].isnull() ) & ( data['Vo_MC3'].isnull() ) & ( data['Num_3']!=0 ) & ( data['Vo_M3'].isnull())].index
ks
for a in q:
    data['Vo_MC2'][a]=str(data['Vo_MC1'][a])[:2]+(str(data['Num_2'][a])) 
for a in ks:
    data['Vo_MC3'][a]=str(data['Vo_MC1'][a])[:2]+(str(data['Num_3'][a]))   


# In[86]:


data


# In[87]:


data['Vo_MC1']=data['Vo_MC1'].str.replace(" ","")
data['Vo_MC2']=data['Vo_MC2'].str.replace(" ","")
#data['Vo_MC3']=data['Vo_MC3'].str.replace(" ","")
data['Vo_M1']=data['Vo_M1'].str.replace(" ","")
data['Vo_M2']=data['Vo_M2'].str.replace(" ","")
#data['Vo_M3']=data['Vo_M3'].str.replace(" ","")


# In[88]:


data.drop_duplicates('Name',keep='last',inplace=True)


# In[89]:


data.to_csv(path3,index=False)


# In[90]:


Win_M=data['Vo_M1'].value_counts()
#print('The winners of the competitions are:')
Win_M.sort_values(ascending=False)


# In[91]:


Win_MC=data['Vo_MC1'].value_counts()
#print('The winners of the competitions are:')
Win_MC.sort_values(ascending=False)


# In[92]:


group_values=list(Win_MC.values)
group_values
group_data=list(Win_MC.keys())
group_data


# In[93]:


group_valM=list(Win_M.values)
group_dataM=list(Win_M.keys())
group_dataM


# In[108]:


fig=plt.figure(figsize=(20,15))
plt.xlabel('No_votes_per_image')
plt.title('VOTE DISTRIBUTION',fontsize=20)
plt.barh(group_data,group_values)
for index, value in enumerate(group_values):
    plt.text(value, index, str(value))
    
plt.savefig(img1)       


# In[109]:


fig=plt.figure(figsize=(20,10))
plt.xlabel('No_votes_per_image')
plt.title('VOTE DISTRIBUTION',fontsize=20)
plt.barh(group_dataM,group_valM)
for index, value in enumerate(group_valM):
    plt.text(value, index, str(value))
    
plt.savefig(img2)    


# In[110]:


dic={'Image_id_JC':group_data,'Votes_JC':group_values}
pd.DataFrame(dic)


# In[111]:


dic2={'Image_ID_F':group_dataM,'Votes_F':group_valM}
pd.DataFrame(dic2)


# In[112]:


#for F
nns=[]
#for d in range(0,len(group_values),1):
    #nns.append(nss[d])'
    
for i,j in zip(group_dataM,range(0,len(group_valM),1)):
    nss=[]
    for index, row in data.iterrows():
        if i==row['Vo_M1']:
            nss.append(row['Name'])
        elif i==row['Vo_M2']:
            nss.append(row['Name'])
        elif i==row['Vo_M3']:
            nss.append(row['Name'])
    nns.append(nss)   


# In[113]:


ns=[]
for i,j in zip(group_data,range(0,len(group_values),1)):
    nn=[]           
    for index, row in data.iterrows():
        if i==row['Vo_MC1']:
            nn.append(row['Name'])
            #print(row['Vo_MC1'])
        elif i==row['Vo_MC2']:
            nn.append(row['Name'])
            #print(row['Vo_MC2'])
        elif i==row['Vo_MC3']:
            #print(row['Vo_MC3'])
            nn.append(row['Name'])
    ns.append(nn)          
        
ns


# In[132]:


dic={'Image_id_JC':group_data,'Votes_JC':group_values,'Name_of_voters':ns}
dfJC=pd.DataFrame(dic)
dfJC
dfJC.to_csv(final1,index=False)


# In[133]:


dic2={'Image_ID_F':group_dataM,'Votes_F':group_valM,'Name_of_Voters':nns}
dff=pd.DataFrame(dic2)
dff
dff.to_csv(final2,index=False)


# In[ ]:




