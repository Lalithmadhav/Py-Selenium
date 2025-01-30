import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"D:\pySelenium\Selenium Drivers\chromedriver-win64"

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/test.html")
driver.implicitly_wait(8)

sum1 = driver.find_element(By.ID, "numA")
sum2 = driver.find_element(By.ID, "numB")

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(15)

btn = driver.find_element(By.CSS_SELECTOR, "button[onclick='calculateTotal()']")
btn.click()

input('Press enter to exit')
driver.quit()