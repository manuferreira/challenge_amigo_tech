import pytest
from pages.login_page import LoginPage
from utilities.test_data import TestData
from conftest import initialize_driver

@pytest.mark.usefixtures("initialize_driver")
class TestHomepage:

    def 