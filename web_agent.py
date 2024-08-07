# web_automation_helper.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random
from faker import Faker
from enum import Enum

fake = Faker()

class WebAgent:
    
    class SELECTOR(Enum):
        ID = By.ID
        NAME = By.NAME
        CSS = By.CSS_SELECTOR

    def __init__(self):
        self.driver = webdriver.Chrome()

    def navigate_to(self, url):
        self.driver.get(url)
        self.wait(1)

    def generate_email(self, domain="mailinator.com"):
        username = fake.user_name()
        return f"{username}@{domain}"
    
    
    def generate_name(self):
        return fake.name()

    def enter_input_value(self, locator_type, locator_value, text):
        element = self.driver.find_element(locator_type.value, locator_value)
        element.send_keys(text)
        return text

    def select_dropdown_value(self, locator_type, locator_value, select_count=1, specific_value=None):
        select = Select(self.driver.find_element(locator_type.value, locator_value))
        all_options = select.options
        
        if specific_value == None:
            random_options = random.sample(all_options[1:], select_count)
            for option in random_options:
                select.select_by_visible_text(option.text)
            return [option.text for option in random_options]
        else:
            select.select_by_visible_text(specific_value)
            return specific_value

    def click_button(self, locator_type, locator_value, wait=1):
        button = self.driver.find_element(locator_type.value, locator_value)
        button.click()
        if(wait > 0):
            self.wait(wait)
        return True
    
    def wait(self, seconds):
        time.sleep(seconds)

    def close_browser(self):
        self.driver.quit()
