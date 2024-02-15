import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import os
import pandas as pd
from os import name
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920x1080')
options.add_argument('--headless')
path = os.path.dirname(os.path.abspath(__file__))
print(path)
print(os.getcwd() + os.path.sep)
options.add_experimental_option("prefs", {
"download.default_directory": os.getcwd() + os.path.sep,
"download.prompt_for_download": False,
"download.directory_upgrade": True,
"safebrowsing_for_trusted_sources_enabled": False,
"safebrowsing.enabled": False
})
driver = webdriver.Chrome(
    executable_path='"C:/chromedriver/chromedriver.exe"')
# driver = webdriver.Chrome('C:/webdriver/chromedriver.exe', options=options)
driver.get("https://glogin.rms.rakuten.co.jp/?sp_id=1")
# identify username, password and signin elements
# first login
driver.find_element_by_name("").send_keys("")
time.sleep(0.2)
driver.find_element_by_name("").send_keys("")
time.sleep(0.4)
driver.find_element_by_class_name("").click()
driver.close
# second login
driver.find_element_by_name(" ").send_keys(" ")
time.sleep(0.2)
driver.find_element_by_name(" ").send_keys(" ")
time.sleep(0.4)
driver.find_element_by_class_name(" ").click()
driver.close
driver.find_element_by_class_name(" ").click()
time.sleep(0.4)
# driver.find_element_by_class_name("btn-reset").click()
# driver.get("https://ad.rms.rakuten.co.jp/cpnadv/download_history")
driver.find_element_by_class_name("btn-reset").click()


url2 = ''
driver.get(url2)
time.sleep(3)
print('[INFO] URL Loaded')

start = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "")))
start.clear()
time.sleep(2)
start.send_keys('2022-01-01' + ' - ' + '2022-01-31')
time.sleep(2)
print('[INFO] Date Selected')

start = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, " "))).click()
time.sleep(2)
start = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, ""))).click()
print('[INFO] Data table loaded')
time.sleep(3)
rows = 1+len(driver.find_elements_by_xpath("")) # total rows

df1 = pd.DataFrame() # dataframe for taking ID column
df = pd.DataFrame() # dataframe for taking ID column
first_td = []
for r in range(1, rows):
    first = driver.find_element_by_xpath("/html/body/table[11]/tbody/tr/td/app-root/div/trend-root/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]/p")
    el = first.get_attribute('innerHTML')
    print('El print')
    print(el)
    first_td.append(el)
df1 = pd.DataFrame(first_td) # dataframe for taking ID column
cols1 = ['ID']
df1.columns = cols1

element = driver.find_element_by_xpath(" ")
element = element.get_attribute('innerHTML')
table_data = [[cell.text.strip() for cell in row("th")] or [cell.text.strip() for cell in row("td")]  for row in BeautifulSoup(element)("tr")]
for data in table_data:
    if data[0] != ' ':
        del data[0]
    if data == ' ':
        del data

print(table_data)
flat_list = [item for sublist in table_data for item in sublist]
print(flat_list)
csv_data = [flat_list[i: i+11] for i in range(0, len(flat_list), 11)]
df = df.append(csv_data)
cols = [  'date', 'del1', 'fg', 'del2', 'h', 'ij', 'dff', 'del3']
df.columns = cols
df[['ff', 'ss']] = df['fg'].str.split('(', expand=True)
df['dd'] = df['dd'].str.replace(')', '') 

df[['dfdf', 'hbaad']] = df['h'].str.split('\n', expand=True) 
 
 

df = pd.concat([df1, df], axis=1)
df = df.reindex(columns=[ '])
print('[ ')
print(f'[INFO] Df {df}')