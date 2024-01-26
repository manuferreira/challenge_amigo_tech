import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from utilities.test_data import TestData


@pytest.fixture
def initialize_driver():
    driver = webdriver.Chrome()
    print("Using Chrome")
    driver.get(TestData.url)
    driver.maximize_window()
    yield driver
    print("Closing driver")
    driver.close()

# @pytest.fixture(params="chrome")
# def initialize_driver(request):
#     if request.param == "chrome":
#         driver = webdriver.Chrome()
#         request.cls.driver = driver
#     print("Using Chrome")
#     driver.get(TestData.url)
#     driver.maximize_window()
#     yield
#     print("Closing driver")
#     driver.close()