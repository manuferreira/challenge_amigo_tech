from selenium.webdriver.common.by import By
from base_page import BasePage
from utilities.locators import CheckoutLocators


class CheckoutPage(BasePage):
    def __int__(self, webdriver):
        super().__init__(webdriver)
        self.first_name = (By.ID, 'first-name')
        self.last_name = (By.ID, 'last-name')
        self.zip_code = (By.ID, 'postal-code')
        self.continue_checkout = (By.ID, 'continue')
        self.error_message = CheckoutLocators.warning_message
        self.item_name_checkout = CheckoutLocators.checkout_item_name
        self.item_price_checkout = CheckoutLocators.checkout_item_price
        self.finish_checkout = (By.CLASS_NAME, 'summary_subtotal_label')
        self.success_checkout_message = CheckoutLocators.checkout_message

    def set_first_name(self, firstname):
        self.click(self.first_name)
        self.set(self.first_name, firstname)

    def set_last_name(self, lastname):
        self.click(self.last_name)
        self.set(self.last_name, lastname)

    def set_zip_code(self, zipcode):
        self.click(self.zip_code)
        self.set(self.zip_code, zipcode)

    def continue_to_checkout(self):
        self.click(self.continue_checkout)

    def get_warning_message(self):
        return self.error_message.text

    def get_item_price(self, item_name):
        item_price_xpath = self.item_price_checkout[1].format(item_name)
        item_price = self.get_text(self.item_price_checkout[0], item_price_xpath)
        """
        manipular os dados daqui
        """
        return item_price

    def click_to_finish_checkout(self):
        self.click(self.finish_checkout)

    def get_success_checkout_message(self):
        self.get_text(self.success_checkout_message)
