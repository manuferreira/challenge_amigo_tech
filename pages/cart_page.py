from selenium.webdriver.common.by import By
from home_page import Homepage
from utilities.locators import CartLocators


class CartPage(Homepage):
    def __int__(self, webdriver):
        super().__init__(webdriver)
        self.remove_inside_cart_button = CartLocators.remove_product_button
        self.checkout = (By.ID, 'checkout')
        self.continue_shopping = (By.ID, 'continue-shopping')

    def get_product_cart_title(self, index):
        self.get_product_title(index)

    def remove_inside_cart(self, product_name):
        remove_inside_cart_button_xpath = self.remove_inside_cart_button[1].format(product_name)
        remove_inside_cart = self.find(self.remove_inside_cart_button[0], remove_inside_cart_button_xpath)
        self.click(remove_inside_cart)

    def click_to_continue_shopping(self):
        self.click(self.continue_shopping)

    def click_to_checkout(self):
        self.click(self.checkout)
