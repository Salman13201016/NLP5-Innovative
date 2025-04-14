from selenium import webdriver
import time
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()







img_list = []

text_list = []
link_list = []
import re
driver.get('https://www.daraz.com.bd/mens-eyeglasses/')
driver.maximize_window()
total_product_text = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]').text
print(total_product_text)
pattern = r"\b\d+\b"
match = re.search(pattern, total_product_text)
bnumber = 0
if match:
    bnumber = match.group()
    print("Bnumber:", type(bnumber))
total = int(bnumber)
total_pages = round(total/40)
print(total_pages)
for page in range(1,total_pages+1):
    p = str(page)
    driver.get(f'https://www.daraz.com.bd/mens-eyeglasses/?page={p}')
    
    driver.maximize_window()

    for i in range(1,5):
        
        j = str(i)
        
        text = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[2]/div[2]/a').text
        link = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[2]/div[2]/a').get_attribute('href')
        img = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/div/img').get_attribute('src')
        text_list.append(text)
        link_list.append(link)
        img_list.append(img)



print(text_list)
print(link_list)
print(img_list)

time.sleep(60)

driver.quit()