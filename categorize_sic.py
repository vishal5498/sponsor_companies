# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 13:28:23 2023

@author: visha
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://resources.companieshouse.gov.uk/sic/"
req = requests.get(url, verify=False)
soup = BeautifulSoup(req.text, "html.parser")
#%%
print(soup.title)
tables = soup.find_all("""table""")
table = pd.read_html(str(tables[0]))[0]
#%%
table['sicInitial'] = table['Code'].str[:2]
table['section'] = ''
section = ''
for index,row in table.iterrows():
    if row['Code'].find('Section')==False:
        section = row['Description']
        print(section)
    else:
        table.loc[index, 'section'] = section
#%%
table = table.rename(columns={'Code':'sic'})
table[['sic','section']].to_csv('out.csv')
#%%