import os
import booking.constants as CONST
from selenium import webdriver

class Booking(webdriver.Chrome):
    def __init__(self, driver_path = r"D:\pySelenium\Selenium Drivers", teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += driver_path
        super(Booking, self).__init__()

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()
    
    def land_first_page(self): 
        self.get(CONST.BASE_URL)
