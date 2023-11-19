import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)


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
from src import helpers

if __name__ == "__main__":
    # Code to be executed when the script is run directly

    driver,action,flag=helpers.setupWebdriver()
    driver.get("https://www.google.com")
    print(driver.find_element(By.XPATH,"//body").text)
