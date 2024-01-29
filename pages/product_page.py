from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.locators import ProductsLocators, Utilities


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_details_name = ProductsLocators.product_name
        self.product_details_description = ProductsLocators.product_description
        self.product_details_price = ProductsLocators.product_price
        self.action_button = Utilities.any_button

    def get_product_page_title(self):
        product_name_text = self.get_text(*self.product_details_name)
        return product_name_text

    def get_product_page_description(self):
        product_description_text = self.get_text(*self.product_details_description)
        return product_description_text

    def get_product_page_price(self):
        product_price_text = self.get_text(*self.product_details_price)
        return product_price_text

    def add_from_item_page_to_cart(self):
        add_button_locator = self.action_button[1].format(button_action="Add to cart")
        self.click((self.action_button[0], add_button_locator))

    def remove_from_item_page_to_cart(self):
        remove_button_locator = self.action_button[1].format(button_action="Remove")
        self.click((self.action_button[0], remove_button_locator))
