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

def setupWebdriver():
    try:
        '''Set up Selenium Webdriver'''
        chrome_options = Options()
        Options.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
        chrome_options.add_argument("--headless") #For AWS/GCP 
        driver=webdriver.Chrome(options=chrome_options, executable_path=r"C:\Users\agney\Desktop\chromedriver-win32\chromedriver.exe")
##        driver.execute_cdp_cmd('Network.enable', {})
##        cookies = pickle.load(open(r"C:\Users\agney\Desktop\New folder\goCargo\SOLD\vauto-cookies.pkl", "rb"))
##        for cookie in cookies:
##            
##            driver.execute_cdp_cmd('Network.setCookie', cookie)
##        driver.execute_cdp_cmd('Network.disable', {})
        driver.maximize_window()
        action = ActionChains(driver)
        flag=True
    except Exception as e:
        flag=False
        pass
    return driver,action,flag
def get_google(driver):
    driver.get("https://www.google.com")
    if "Sign" in driver.find_element(By.XPATH,"//body").text:
        flag=True
    else:
        flag=False
    return flag

def setLogs(logfile):
    try:
        '''Set Up logging'''
        logging.basicConfig(
        filename=logfile,
        level=20, filemode='w', # You can adjust the log level as needed
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
        log = logging.getLogger("my-logger")
        # Create a console (stream) handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        # Create a formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # Set the formatter for the console handler
        console_handler.setFormatter(formatter)
        # Add the console handler to the logger
        log.addHandler(console_handler)
        assert True
        return log
    except Exception as e:
        assert True
        pass
