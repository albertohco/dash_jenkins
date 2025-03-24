import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    chrome_path = "/home/local_us/dash/chrome-linux64/chrome"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_path
    driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()
