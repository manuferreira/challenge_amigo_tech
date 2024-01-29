import pytest
from pages.login_page import LoginPage
from conftest import initialize_driver

@pytest.mark.usefixtures("initialize_driver")
class TestLogin:
    def test_valid_credentials(self, initialize_driver):
        login_page = LoginPage(initialize_driver)
        actual_title = login_page.get_title()
        assert actual_title == "Swag Labs"
