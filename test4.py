import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
 
class SauceDemoTest(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Chrome()
 
    def test_login(self):
        self.driver.get("https://www.saucedemo.com/")
 
        #login
        username_input = self.driver.find_element(By.ID, 'user-name')
        password_input = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.CSS_SELECTOR, '.btn_action')
 
        username_input.send_keys('standard_user')
        time.sleep(1)
        password_input.send_keys('secret_sauce')
        time.sleep(1)
        login_button.click()
        time.sleep(3)
 
    def tearDown(self):
        self.driver.close()
 
if __name__ == "__main__":
    unittest.main()