from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.locators import CheckoutLocators


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name = (By.ID, 'first-name')
        self.last_name = (By.ID, 'last-name')
        self.zip_code = (By.ID, 'postal-code')
        self.continue_checkout = (By.ID, 'continue')
        self.error_message = CheckoutLocators.warning_message
        self.item_name_checkout = CheckoutLocators.checkout_item_name
        self.item_price_checkout = CheckoutLocators.checkout_item_price
        self.subtotal = (By.CLASS_NAME, 'summary_subtotal_label')
        self.finish_checkout = (By.ID, 'finish')
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
        return self.get_text(*self.error_message)

    def get_item_price(self, product_name):
        item_price_xpath = self.item_price_checkout[1].format(item_name=product_name)
        item_price = self.get_text(self.item_price_checkout[0], item_price_xpath)
        item_price_clean = ''

        for char in item_price:
            if char.isdigit() or char == '.':
                item_price_clean += char

        item_price_clean = float(item_price_clean)
        return item_price_clean

    def get_total_price_cart(self):
        subtotal_element = self.find(*self.subtotal)
        subtotal_value = subtotal_element.text
        subtotal_value_clean = ''

        for char in subtotal_value:
            if char.isdigit() or char == '.':
                subtotal_value_clean += char

        return float(subtotal_value_clean)

    def click_to_finish_checkout(self):
        self.click(self.finish_checkout)

    def get_success_checkout_message(self):
        success_message_checkout = self.get_text(*self.success_checkout_message)
        return success_message_checkout
