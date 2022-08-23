import enum
from logging import exception
from tkinter import N
from tkinter.messagebox import NO
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd

data = {'Gene Symbol': [], 'Gene Symbol Link': [], 'Gene description': [], 'References for Oral cancer': [], 'References for Head & Neck cancer': []}
s = Service(executable_path=ChromeDriverManager().install())
options = Options()
# options.add_argument('--headless')
browser = webdriver.Chrome(service=s, options=options)
browser.maximize_window()
browser.get('http://www.actrec.gov.in/OCDB/genelist.htm')

table = browser.find_element(By.CLASS_NAME, 'MsoNormalTable')
tbody = table.find_element(By.TAG_NAME, 'tbody')
trs = tbody.find_elements(By.TAG_NAME, 'tr')
for tr in trs:
    tds = browser.find_elements(By.TAG_NAME, 'td')
    for index, td in enumerate(tds):
        if index == 0:
            try:
                print(data)
                p = browser.find_element(By.CLASS_NAME, 'MsoNormal')
                font = p.find_element(By.TAG_NAME, 'font')
                b = font.find_element(By.TAG_NAME, 'b')
                spans = b.find_elements(By.TAG_NAME, 'span')
                for ind, k in enumerate(spans):
                    if ind == 0:
                        a = k.find_element(By.TAG_NAME, 'a')
                        data['Gene Symbol'].append(a.text)
                        data['Gene Symbol Link'].append(a.get_attribute('href'))
                    if ind == 2:
                        data['Gene description'].append(k.text)
                    else:
                        data['Gene Symbol'].append(None)
                        data['Gene Symbol Link'].append(None)
                        data['Gene description'].append(None)
            except Exception:
                pass
        elif index == 1:
            try:
                a = td.find_element(By.TAG_NAME, 'a').get_attribute('href')
                data['References for Oral cancer'].append(a)
            except Exception:
                data['References for Oral cancer'].append(None)
        else:
            try:
                p = td.find_element(By.CLASS_NAME, 'MsoNormal')
                a = p.find_element(By.TAG_NAME, 'a')
                data['References for Head & Neck cancer'].append(a.get_attribute('href'))
            except Exception:
                data['References for Head & Neck cancer'].append(None)
    break

print(len(data['Gene Symbol']))
print(len(data['Gene Symbol Link']))
print(len(data['Gene description']))
print(len(data['References for Oral cancer']))
print(len(data['References for Head & Neck cancer']))

df = pd.DataFrame(data)
df.to_csv('Database1.csv')
