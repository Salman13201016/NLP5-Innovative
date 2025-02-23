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

driver.get('https://www.google.com/')



driver.refresh()
search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("Laptop Shop Near Mirpur")

from selenium.webdriver.common.keys import Keys
search_box.send_keys(Keys.RETURN)
time.sleep(200)
recaptcha_checkbox = driver.find_element(By.CLASS_NAME, "g-recaptcha")
from selenium.webdriver.common.action_chains import ActionChains
# Use ActionChains to click on the reCAPTCHA div
# action = ActionChains(driver)
# action.move_to_element(recaptcha_checkbox).click().perform()
time.sleep(60)

g_map = driver.find_element(By.XPATH,'//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a').click()
time.sleep(60)