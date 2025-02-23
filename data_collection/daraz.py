from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
import re

driver = webdriver.Chrome()
# driver.get('https://www.daraz.com.bd/routers/')


link_list = []

driver.get(f'https://www.daraz.com.bd/routers/?page=1')
driver.maximize_window()
total_number_page = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]').text

# total_number_page = int(total_number_page.split()[0])
# total_number_page = total_number_page
print(f"total:{total_number_page}")
import re
numbers = int(re.findall(r'\d+', total_number_page)[0])
total_page = round(numbers/40)
print(total_page)
for page_no in range(1,3):
    driver.get(f'https://www.daraz.com.bd/routers/?page={page_no}')
    driver.maximize_window()
    for prod in range(1,13):
        type_i = str(prod)
        link = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+type_i+']/div/div/div[2]/div[2]/a').get_attribute('href')
        link_list.append(link)
print(link_list)
print(len(link_list))

# driver.get(link.get_attribute('href'))
time.sleep(100)
driver.quit()
