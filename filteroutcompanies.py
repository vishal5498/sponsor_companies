# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 14:58:08 2023

@author: visha
"""
import pandas as pd
import time
import re
df=[]
starttime = time.time()
companies = pd.read_csv("result company official website - done.csv")
companies2 = pd.read_csv("mainLink.csv")
companies = companies[len(companies2):50000]
companies['links'] = companies['links'].str.replace(' ','').str.replace("'","").str.strip('][').str.split(',')
mainlink = []
links = []
for index,row in companies.iterrows():
    result = "No match"
    for i,each in enumerate(row['links'],start=0):
        if re.match("[^\r\n]*\.com$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*\.com\/en$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*\.co.uk$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*\.org$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*\.org.uk$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*\.io$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*\.ai$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*\.about_us$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*about-us$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*aboutus$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*about$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*home$",each)!=None:
            result = each
            break
    mainlink.append(result)
result = pd.DataFrame({"index":companies["index"],"mainLink":mainlink})
companies = pd.merge(companies,result,on='index')






companiesextra = companies[companies['mainLink']=='No match']
companies = companies[companies['mainLink']!='No match']
mainlink2 = []
for index,row in companiesextra.iterrows():
    result = "No match"
    for i,each in enumerate(row['links'],start=0):
        if re.match("[^\r\n]*\.uk$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*\.com\/en-gb$",each)!=None:
            result = each
            break
        
        if re.match("[^\r\n]*linkedin",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*contact$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*contactus$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*contact-us$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*contact_us$",each)!=None:
            result = each
            break
    mainlink2.append(result)
result = pd.DataFrame({"index":companiesextra["index"],"mainLink":mainlink2})
companiesextra = pd.merge(companiesextra.drop(['mainLink'],axis=1),result,on='index')
# companies = companies.append(companiesextra[companiesextra['mainLink']!='No match'])
companiesextra2 = companiesextra[companiesextra['mainLink']=='No match']
companiesextra = companiesextra[companiesextra['mainLink']!='No match']
df = pd.concat([companies, companiesextra[companiesextra['mainLink']!='No match']])
df = pd.concat([df, companiesextra2])
# df.to_csv('filteredmainLink.csv', mode='a', index=False, header=False)

#%%
mainlink3 = []

for index,row in companiesextra2.iterrows():
    result = "No match"
    for i,each in enumerate(row['links'],start=0):
        if re.match("[^\r\n]*uk$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*homepage$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*gb$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*en$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*en_gb$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*london$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*en-GB$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*\.net$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*\.co$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*\.biz$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*\.capital$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*team$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*london$",each)!=None:
            result = each
            break
        if re.match("[^\r\n]*\.global$",each)!=None:
            result = each
            break
    mainlink3.append(result)
result2 = pd.DataFrame({"index":companiesextra2["index"],"mainLink":mainlink3})
companiesextra2 = pd.merge(companiesextra2.drop(['mainLink'],axis=1),result2,on='index')
# companies = companies.append(companiesextra[companiesextra['mainLink']!='No match'])
companiesextra3 = companiesextra2[companiesextra2['mainLink']=='No match']
companiesextra2 = companiesextra2[companiesextra2['mainLink']!='No match']
df = pd.concat([companies, companiesextra])
df = pd.concat([df, companiesextra2[companiesextra2['mainLink']!='No match']])
df = pd.concat([df, companiesextra3])
#%%