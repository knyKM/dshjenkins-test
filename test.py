import pytest
import time
from selenium import webdriver

@pytest.fixture(scope="module")

def browser():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chromeOptions)
    yield driver
    driver.quit()
