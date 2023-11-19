import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
import pytest
import pickle
import time
import logging
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import email
import imaplib
from src import helpers



##@pytest.mark.usefixtures("browser")
##def test_driver(browser_2):
##    browser_2.get("https://www.google.com")
##    

    
@pytest.mark.usefixtures("browser")
class Test_browser:
    def test_go_to_website(self):
        """
        Navigates to a website and checks if the page loads correctly.
        """
        self.driver.get("https://www.google.com")
        
        # Write an assertion to test if the page loaded correctly
        assert "About" in self.driver.find_element(By.XPATH, "//body").text

    def test_input_text(self):
        """
        Inputs text into an element identified by its XPath and checks if the input is successful.
        """
        input_text = "234"
        ele=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//textarea")))
        self.action.move_to_element(ele).perform()
        ele.send_keys(input_text)
        
        # Add a delay for testing purposes, you can remove this in production code
        time.sleep(5)
        
        assert ele.get_attribute("value") == 1#input_text
    
    
