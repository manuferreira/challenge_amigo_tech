from selenium.webdriver.common.by import By
from pages.home_page import Homepage
from utilities.locators import CartLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(Homepage):
    def __init__(self, driver):
        super().__init__(driver)
        self.remove_item_cart = CartLocators.remove_product_button
        self.checkout = (By.ID, 'checkout')
        self.continue_shopping = (By.ID, 'continue-shopping')

    def get_product_cart_title(self, index):
        self.get_product_title(index)

    def delete_from_cart(self, product_name):
        remove_item_cart_locator = self.remove_item_cart[1].format(item_name=product_name)
        self.click((self.remove_item_cart[0], remove_item_cart_locator))

    def click_to_continue_shopping(self):
        self.click(self.continue_shopping)

    def click_to_checkout(self):
        self.click(self.checkout)

    def item_not_present(self, index):
        try:
            self.get_product_cart_title(index)
            return True

        except Exception as e:
            return False