import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


os.environ['PATH'] += r"D:/pySelenium/SeleniumDrivers/" # Selenium Drivers Path

driver = webdriver.Chrome() # Using Chrome 
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html") # Website URL
driver.implicitly_wait(8)

my_element = driver.find_element("id", "downloadButton") # Without By module
my_element.click()

progress_element = driver.find_element("class name", "progress-label") # Finds an element with class name : progress-label 
print(f"{progress_element.text}") # Prints the element in text
print(f"{progress_element.text == "Completed"}") # Prints bool of element and "Completed"(str)

WebDriverWait(driver, 30).until( # Check if the class name : progress-label  gives "Complete!" within 30 seconds
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "progress-label"), # Element Filtration
        "Complete!" # Expected Text
    )
)

input("Press Enter to exit...")
driver.quit()