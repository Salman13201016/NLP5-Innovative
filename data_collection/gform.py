from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options to use your logged-in profile
chrome_options = Options()

#%LOCALAPPDATA%\Google\Chrome\User Data\

#start chrome.exe --user-data-dir="C:\ptempCC"
chrome_options.add_argument(r"--user-data-dir=C:\Users\HP\AppData\Local\Google\Chrome\User Data")

# chrome_options.add_argument(r"--user-data-dir=C:\ptemCC")

#r = raw literal String

chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--headless")  # Run in headless mode
# chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration (may not be needed, but it's a good practice in headless mode)
  # Using your default profile

# Launch Chrome with your profile
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://forms.gle/eJBBse2AshZkyzgBA") 
driver.maximize_window()

time.sleep(5)

try:
    text_input = driver.find_element(By.XPATH, '//input[@type="text"]')
    text_input.send_keys("Test Answer from Selenium")
except:
    print("Text input not found")

time.sleep(5)

#ActionChains = Complex Interaction - drag and drop, double click, click on a div/span/p/,hover,keyup, keydown
#click()

# radio_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'

X= 'Female'
radio_button_xpath = '//*[contains(@aria-label, "Female")]'

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
try:
    # radio = driver.find_ele]ment(By.XPATH, '//div[@role="radio" and @aria-label="Option 1"]')
    # radio.click()
    radio_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, radio_button_xpath))
    )

    actions = ActionChains(driver)

    actions.move_to_element(radio_button).click().perform()
    print("Radio button clicked")
except:
    print("radio button not clicked")


time.sleep(5)

submit_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'  # XPath for the submit button

try:
    # Find the submit button element
    submit_button = driver.find_element(By.XPATH, submit_button_xpath)

    # Initialize ActionChains
    actions = ActionChains(driver)

    # Move to the submit button and click it
    actions.move_to_element(submit_button).click().perform()
    print("Submit button clicked using ActionChains.")
except Exception as e:
    print(f"Error clicking submit button: {e}")

time.sleep(20)
driver.quit()