# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 17:02:13 2023

@author: visha
"""
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
#%%
companies = pd.read_csv("Extracted_companies.csv")[['company','city']][:3]
browser = webdriver.Chrome()
browser.get("https://duckduckgo.com/")
browser.implicitly_wait(2)
textbox = browser.find_element(by=By.NAME,value="q")
result = pd.DataFrame()
for index,row in companies.iterrows():
    company = row['company']
    city = row['city']
    links = []
    print(company)
    textbox.send_keys("'{}' uk website".format(company))
    textbox.send_keys(Keys.ENTER)
    browser.implicitly_wait(0.2)
    text = browser.find_element(by=By.XPATH,value="""//*[@id="r1-0"]/div[1]/div/a""")
    print(text.get_attribute("textContent"))
    for i in range(0,5):
        try:
            text = browser.find_element(by=By.XPATH,value="""//*[@id="r1-{}"]/div[1]/div/a""".format(i))
            print(text.get_attribute("textContent"))
            links.append(str(text.get_attribute("textContent")).replace(u'\xa0>\xa0', u'/').replace(" › ", "/").replace(" › ", "/").replace(u'\xa0',''))
        except:
            print("Issue in XPath")
    result = pd.concat([result,pd.DataFrame({"company":company,"city":city,"links":[links]})],ignore_index=True)
    textbox = browser.find_element(by=By.NAME,value="q")
    
    textbox.send_keys(Keys.CONTROL + "a")
    textbox.send_keys(Keys.DELETE)
    browser.implicitly_wait(2)
browser.quit()
#%%
result.to_csv('result.csv')
#%%