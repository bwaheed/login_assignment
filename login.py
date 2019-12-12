import time
import unittest
from selenium import webdriver

class StudioCode(unittest.TestCase):

    def setUp(self):
        #Initialize webdriver
        self.driver = webdriver.Firefox()
        # driver = webdriver.Chrome()

    def test_login(self):
        # Open Required page
        self.driver.get('https://studio.code.org/users/sign_in')
        # Check that 'Code.org' is present in browser title
        self.assertIn('Code.org', self.driver.title)
        # Find and fill the email field
        email_field = self.driver.find_element_by_css_selector('#user_login')
        
        email_field.send_keys('bilalw38@yahoo.com')
        #Find and fill the password field
        password_field = self.driver.find_element_by_css_selector('#user_password')
        
        password_field.send_keys('ARBIsoft!@3')
        # Find and click the signin button
        signin_btn = self.driver.find_element_by_css_selector('#signin-button')
        signin_btn.click()
        
        time.sleep(10)
        # Check that 'Code.org' is present in pages browser title
        self.assertIn('Code.org', self.driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

