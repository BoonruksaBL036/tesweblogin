import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class browserstackTest(unittest.TestCase):

    def setUp(self):
        s = Service(r'D:\\chromedriver\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        self.driver.set_window_size(1072, 816)

    def tearDown(self):
        self.driver.quit()

    def test_open_google_bing(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        
        self.driver.find_element(By.ID,"username").send_keys("student")
        self.driver.find_element(By.ID,"password").send_keys("Password123")
        self.driver.find_element(By.ID,"submit").click()
        time.sleep(5)
        
       
if __name__ == '__main__':
    unittest.main()