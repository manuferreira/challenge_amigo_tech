import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from utilities.test_data import TestData


@pytest.fixture
def initialize_driver():
    driver = webdriver.Chrome()
    print("Using Chrome")
    driver.get(TestData.URL)
    driver.maximize_window()
    yield driver
    print("Closing driver")
    driver.close()