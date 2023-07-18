# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 17:02:13 2023

@author: visha
"""
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
companies = pd.read_csv("Extracted_companies.csv")['company'][:10]
print(companies)
browser = webdriver.Chrome()
browser.get("https://www.google.co.in/")
browser.implicitly_wait(2)
textbox = browser.find_element(by=By.NAME,value="q")
for company in companies:
    # print(textbox)
    textbox.send_keys("{} linkedin".format(company))
    textbox.send_keys(Keys.RETURN)
    text = browser.find_element(by=By.XPATH,value="""//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div/div""")
    print(text.get_attribute("textContent"))
    textbox = browser.find_element(by=By.NAME,value="q")
    # print(textbox)
    textbox.send_keys(Keys.CONTROL + "a")
    textbox.send_keys(Keys.DELETE)
    browser.implicitly_wait(2)
browser.quit()
