from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()

driver.maximize_window()

driver.get('https://www.daraz.com.bd/products/mercusys-ac12-ac1200-i373299504.html?spm=a2a0e.searchlistcategory.list.22.42433d8flZeCvA')



driver.refresh()
height = driver.execute_script('return document.body.scrollHeight')

print(height)



for i in range(0,height+300,30):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)

 




# element = driver.find_element(By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div')))


# if(total_page>=4):

loop_list = []
global element
for i in range(1,6):
    
    if(i>=4 and i<5):
        j='4'
        print(4)
        element = driver.find_element(By.XPATH, f'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[{j}]')
        loop_list.append(4)
    elif(i==5):
        element = driver.find_element(By.XPATH, '//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[5]')
        loop_list.append(5)
    else:
        element = driver.find_element(By.XPATH, f'//*[@id="module_product_review"]/div/div/div[3]/div[2]/div/div/button[{i}]')
        print(i)
        loop_list.append(i)
    element.click()
    time.sleep(5)


# for i in all_comments:
#     print(i.text)    
# print(loop_list)

# Click the element

time.sleep(60)
driver.quit()
