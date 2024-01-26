from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    def set_username(self, username):
        self.set(*self.username_field, username)

    def set_password(self, password):
        self.set(*self.password_field, password)

    def click_to_login(self):
        self.click(*self.login_button)
