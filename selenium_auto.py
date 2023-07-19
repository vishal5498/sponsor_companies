# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 17:02:13 2023

@author: visha
"""
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def finding_company_website(browser):
    result = pd.DataFrame()
    textbox = browser.find_element(by=By.NAME,value="q")
    for index,row in companies.iterrows():
        company = row['company']
        city = row['city']
        links = []
        print(company)
        textbox.send_keys("'{}' uk {} company website".format(company,city))
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
    result.to_csv('result.csv')


def finding_company_linkedin(browser):
    result = {'company':[],'city':[],'link1':[],'link2':[],'link3':[],'link4':[],'link5':[],'link6':[],'link7':[],'link8':[],'link9':[],'link10':[]}
    textbox = browser.find_element(by=By.NAME,value="q")
    for index,row in companies.iterrows():
        company = row['company']
        city = row['city']
        links = []
        print(company)
        textbox.send_keys("linkedin '{}' uk {} company".format(company,city))
        textbox.send_keys(Keys.ENTER)
        browser.implicitly_wait(0.2)
        text = browser.find_element(by=By.XPATH,value="""//*[@id="r1-0"]/div[1]/div/a""")
        print(text.get_attribute("textContent"))
        result['company'].append(company)
        result['city'].append(city)
        for i in range(0,10):
            try:
                text = browser.find_element(by=By.XPATH,value="""//*[@id="r1-{}"]/div[1]/div/a""".format(i))
                print(text.get_attribute("textContent"))
                textContent = text.get_attribute("textContent")
                print(textContent)
                if len(textContent) > 0:
                    url = textContent.replace(' › ','/').replace(' › ','/')
                    print(url)
                    result[f'link' + str(i+1)].append(url)
            except:
                print("Issue in XPath")
                result[f'link' + str(i+1)].append(None)
        textbox = browser.find_element(by=By.NAME,value="q")
        
        textbox.send_keys(Keys.CONTROL + "a")
        textbox.send_keys(Keys.DELETE)
        browser.implicitly_wait(2)
    result_df = pd.DataFrame(result)
    result_df.to_csv("./result_linkedin.csv",index=False)


if __name__ == "__main__":
    companies = pd.read_csv("Extracted_companies.csv")[['company','city']][:3]
    browser = webdriver.Chrome(executable_path="./chromedriver.exe")
    browser.get("https://duckduckgo.com/")
    browser.implicitly_wait(2)
    
    
    # Find company's website link
    # finding_company_website(browser)
    

    # Find company's linkedIn link
    finding_company_linkedin(browser)
    
    
    browser.quit()

