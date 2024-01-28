import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from pages.login_page import LoginPage
from utilities.test_data import TestData


@pytest.fixture
def initialize_driver():
    driver = webdriver.Chrome()
    print("Using Chrome")
    driver.get(TestData.URL)
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.login(TestData.USERNAME, TestData.PASSWORD)
    yield driver
    print("Closing driver")
    driver.close()

