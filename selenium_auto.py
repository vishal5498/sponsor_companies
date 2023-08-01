# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 17:02:13 2023

@author: visha
"""
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import Select

def google_search_selenium(browser,search_str):
    try:
        result = pd.DataFrame()
        textbox = browser.find_element(by=By.NAME,value="q")
        for index,row in companies.iterrows():
            company = row['company']
            city = row['city']
            links = []
            print(company)
            textbox.send_keys("'{}' uk {} {}".format(company,city,search_str))
            textbox.send_keys(Keys.ENTER)
            browser.implicitly_wait(0.2)
            text = browser.find_element(by=By.XPATH,value="""//*[@id="r1-0"]/div[1]/div/a""")
            for i in range(0,8):
                try:
                    text = browser.find_element(by=By.XPATH,value="""//*[@id="r1-{}"]/div[1]/div/a""".format(i))
                    links.append(str(text.get_attribute("textContent")).replace(u'\xa0>\xa0', u'/').replace("›", "/").replace(" › ", "/").replace(" ", "").replace(u'\xa0',''))
                except:
                    print("Issue in XPath")
            result = pd.concat([result,pd.DataFrame({"company":company,"city":city,"links":[links]})],ignore_index=True)
            textbox = browser.find_element(by=By.NAME,value="q")
            
            textbox.send_keys(Keys.CONTROL + "a")
            textbox.send_keys(Keys.DELETE)
            browser.implicitly_wait(2)
        result.to_csv('result {}.csv'.format(search_str))
    except:
        result.to_csv('result {}.csv'.format(search_str))

if __name__ == "__main__":
    companies = pd.read_csv("Extracted_companies.csv")[['company','city']][0:70000]
    companies_read = pd.read_csv("result company official website - done.csv")
    companies = companies[companies['city'].str.contains('London')]
    companies = companies[companies['company'].isin(companies_read['company'])==False]
    print(len(companies))
    browser = webdriver.Chrome()
    browser.get("https://duckduckgo.com/settings")
    browser.implicitly_wait(2)
    select = Select(browser.find_element(By.ID,"setting_kl"))
    select.select_by_visible_text('United Kingdom')

    # Find company's website link
    google_search_selenium(browser,"company official website")
    

    # Find company's linkedIn link
    # google_search_selenium(browser,"linkedin")

    
    
    browser.quit()
