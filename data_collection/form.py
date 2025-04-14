from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Test cases: (name, email, password, phone, should_pass)
test_data = [
    ("", "123", "123", "123", False),
    ("John", "john@example.com", "123", "1234567890", False),
    ("John", "john@", "secret123", "1234567890", False),
    ("John", "john@example.com", "secret123", "1234567890", True)
]

# Start browser once
driver = webdriver.Chrome()
driver.get("https://innovativeskillsltd.com/contact")  # <-- Change this to your actual path

for i, (name, email, password, phone, should_pass) in enumerate(test_data, start=1):
    print(f"\nRunning Test Case {i}...{name}{email}")

#     # Clear previous inputs
    driver.find_element(By.NAME, "name").clear()
#     driver.find_element(By.NAME, "email").clear()
#     driver.find_element(By.NAME, "password").clear()
#     driver.find_element(By.NAME, "phone").clear()

#     # Input values
    driver.find_element(By.NAME, "name").send_keys(name)
#     driver.find_element(By.NAME, "email").send_keys(email)
#     driver.find_element(By.NAME, "password").send_keys(password)
#     driver.find_element(By.NAME, "phone").send_keys(phone)

#     # Try to submit the form
    driver.find_element(By.TAG_NAME, "form").submit()
    time.sleep(5)
#     time.sleep(1)

#     # Simple assumption: If still on same page, assume invalid
#     current_url = driver.current_url

#     if should_pass:
#         print(f"✅ Test Case {i} expected to pass.")
#         print(f"Current URL: {current_url}")
#     else:
#         print(f"❌ Test Case {i} expected to fail (validation should prevent submit).")
#         print(f"Current URL: {current_url}")

# # Wait a bit before closing
driver.maximize_window()
time.sleep(100)

driver.quit()
