from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://innovativeskillsltd.com/contact") 

driver.maximize_window()

name ="salman"

#test 1: empty - invalid
#test 2: minimum 3 character - pass
#test 1 for email: empty
#test 2 for email: valid email 

test_data = [
    ("salman", "123", "123", "123", False),
    ("John", "john@example.com", "123", "1234567890", False),
    ("John", "john@", "secret123", "1234567890", False),
    ("John", "john@example.com", "secret123", "1234567890", True)
]

for i, (name, email, password, phone, should_pass) in enumerate(test_data, start=1):
    print(f"\nRunning Test Case {i}: {name} {email}")

    driver.find_element(By.NAME, "name").clear()
    driver.find_element(By.NAME, "email").clear()

    driver.find_element(By.NAME, "name").send_keys(name)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.TAG_NAME, "form").submit()

    time.sleep(5)
time.sleep(20)
driver.quit()


#new.excel = whatsapp er phone number = 150 phone
#ads.excel = 300 phones
#now check new = ads ---->more qualified