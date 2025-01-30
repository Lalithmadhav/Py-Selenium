import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


os.environ['PATH'] += r"D:/pySelenium/SeleniumDrivers/"

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
driver.implicitly_wait(8)

my_element = driver.find_element("id", "downloadButton")
my_element.click()

progress_element = driver.find_element("class name", "progress-label")
print(f"{progress_element.text}")
print(f"{progress_element.text == "Completed"}")

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "progress-label"), # Element Filtration
        "Complete!" # Expected Text
    )
)

input("Press Enter to exit...")
driver.quit()