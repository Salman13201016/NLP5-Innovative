from selenium import webdriver
import time
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()


driver.get('https://www.daraz.com.bd/products/-i315680595-s1427153104.html')

driver.refresh()
driver.maximize_window()
height = driver.execute_script('return document.body.scrollHeight')
print("height",height)

for i in range(0,height+500,50):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)

#locator must be same for find_elements

comment = driver.find_elements(By.CLASS_NAME,'content')
print("comment_object_type",type(comment))
print("comment_object",comment)

for i in comment:
    print(i.text)

# print(comment)

time.sleep(60)
driver.quit()
