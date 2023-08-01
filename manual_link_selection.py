# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:33:04 2023

@author: visha
"""
import pandas as pd

companies = pd.read_csv("result company official website - done.csv")
companies2 = pd.read_csv("mainLink.csv")
companies = companies[len(companies2):10]
companies['links'] = companies['links'].str.replace(' ','').str.replace("'","").str.strip('][').str.split(',')
mainlink = []
for index,row in companies.iterrows():
    print('\n')
    print(row['company'])
    for i,each in enumerate(row['links'],start=0):
        print ("{}. {}".format(i,each))
    x=input("\nEnter the main link: ")
    print('\n')
    print(row['links'][int(x)])
    mainlink.append(row['links'][int(x)])
result = pd.DataFrame({"index":companies["index"],"mainLink":mainlink})
result.to_csv('mainLink.csv', mode='a', index=False, header=False)