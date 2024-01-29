from utilities.locators import BasePageLocators



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find(*locator).click()

    def set(self, locator, value):
        self.find(*locator).send_keys(value)

    def get_text(self, *locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title

    def go_to_cart(self):
        self.find(*BasePageLocators.cart_icon).click()

    def go_back(self):
        self.driver.back()
