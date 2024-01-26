import pytest
from pages.login_page import LoginPage
from utilities.test_data import TestData
from conftest import initialize_driver

@pytest.mark.usefixtures("initialize_driver")
class TestLogin:
    def test_valid_credentials(self, initialize_driver):
        login_page = LoginPage(initialize_driver)
        login_page.set_username(TestData.USERNAME)
        login_page.set_password(TestData.PASSWORD)
        login_page.click_to_login()
