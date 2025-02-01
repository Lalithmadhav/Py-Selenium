import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"D:\pySelenium\Selenium Drivers\chromedriver-win64"

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/2/test.html")
driver.implicitly_wait(8) # a global setting that tells the WebDriver to wait for a specified amount of time (8 sec) before throwing an error (NoSuchElementException) if it can't find an element 

sum1 = driver.find_element(By.ID, "numA")
sum2 = driver.find_element(By.ID, "numB")

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(15)

btn = driver.find_element(By.CSS_SELECTOR, "button[onclick='calculateTotal()']")
btn.click()

input('Press enter to exit...')
driver.quit()