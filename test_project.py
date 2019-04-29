import unittest
from selenium import webdriver
from values.Webdriver import Driver
from values import strings
from values import functions
from values.functions import Log_in_page
from pageobjects import elements


class Test_login(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.url)

    def test_login(self):
        log_in_page = Log_in_page()
        log_in_page.navigate_login()
        log_in_page. enter_password_and_username()
        
        #self.assertIsNotNone

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()




