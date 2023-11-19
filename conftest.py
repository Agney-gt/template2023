import pytest
import pytest_html
from datetime import datetime
from pathlib import Path
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
import pickle
import pytest
from webdriver_manager.chrome import ChromeDriverManager
import os
current_working_dir = os.getcwd()
driver = None

Baseurl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    now = datetime.now()
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    report_dir = item.config.option.report_dir
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report_dir + "/screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
            driver.save_screenshot(file_name)
            if file_name:
                relative_path = os.path.relpath(file_name, start=report_dir)
                html = '<img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % relative_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.now()
    report_dir = Path('Reports', now.strftime("%H%M%d%m%Y"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"report_{now.strftime('%H%M%S')}.html"
    #pytest_html = f"report_{now.strftime('%H%M%S')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True
    config.option.report_dir = str(report_dir)


def pytest_html_report_title(report):
    report.title = "Automation Report"


@pytest.fixture(scope='class', autouse=True)
def browser(request):
    global action,driver
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chr_options)
    request.cls.action = ActionChains(driver)
    request.cls.driver = driver

