from selenium.webdriver.common.by import By
from selenium import webdriver
from values.Webdriver import Driver


log_in_header = (By.CSS_SELECTOR, ".last.leaf.login-button")
user_name_field = (By.ID,"account_id")
password_field = (By.ID,"password")
submit_button = (By.ID,"loginbutton")
    