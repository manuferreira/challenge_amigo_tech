from selenium import webdriver
from utilities.locators import BasePageLocators


class BasePage:
    """
    Essa classe contem metodos comuns a todas as páginas
    """
    def __init__(self, webdriver):
        self.webdriver = webdriver

    def find(self, *locator):
        return self.webdriver.find_element(*locator)

    def find_elements(self, *locator):
        return self.webdriver.find_elements(*locator)

    def click(self, locator):
        self.find(*locator).click()

    def set(self, locator, value):
        # self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, *locator):
        return self.find(*locator).text

    def go_to_cart(self):
        self.find(BasePageLocators.cart_icon).click()
