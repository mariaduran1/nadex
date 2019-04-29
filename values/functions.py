from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from values.Webdriver import Driver
from selenium.webdriver.common.keys import Keys
from values import strings
from pageobjects import elements


class Log_in_page():  

    
    #driver = webdriver.Chrome('C:\dev1\week5\chromedriver.exe')
    #driver.get("https://demo.nadex.com/")

    

    def navigate_login(self):
        driver = webdriver.Chrome('C:\dev1\week5\chromedriver.exe')
        driver.get("https://demo.nadex.com/")  
        log_in_header = driver.find_element_by_css_selector (".last.leaf.login-button")
        log_in_header.click()
    
    def enter_password_and_username(self):
        driver = webdriver.Chrome('C:\dev1\week5\chromedriver.exe')
        driver.get("https://demo.nadex.com/login")  
        user_name = driver.find_element_by_id ("account_id")
        password_field = driver.find_element_by_id("password") 
        submit_button = driver.find_element_by_id("loginbutton")
        user_name_field = user_name
        user_name_field.send_keys(strings.username)
        password_field.send_keys(strings.password)
        submit_button.click()
      
        
    
      
