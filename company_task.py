# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 14:05:59 2023

@author: visha
"""
import pandas as pd
companies = pd.read_csv("Extracted_companies.csv").drop(['county'],axis=1)
companies = companies[companies['tiers'].str.contains('Skilled Worker')]
companieswsic = companies[companies['sic'].isnull()==False][['company','city','sic']]
#%%
companieswsic['sic'] = companieswsic['sic'].str.replace(' ','').str.replace("'","").str.strip('][').str.split(',')
companieswsic = companieswsic.explode('sic')
#%%
sicdesc = pd.read_csv("out.csv")
companieswsic = pd.merge(companieswsic,sicdesc,on='sic')[['company','city','section']].drop_duplicates()
companieswsic = (companieswsic.groupby(['company','city'])
      .agg({'section': lambda x: x.tolist()}).reset_index())
#%%
companies = pd.merge(companies,companieswsic,on=['company','city'],how='left')
#%%