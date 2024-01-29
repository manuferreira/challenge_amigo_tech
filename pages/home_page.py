from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.locators import ProductsLocators


class Homepage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_title = (By.CLASS_NAME, 'inventory_item_name ')
        self.product_description = (By.CLASS_NAME, 'inventory_item_desc')
        self.add_button = ProductsLocators.product_button
        self.remove_button = ProductsLocators.product_button

    def get_product_title(self, index):
        all_products_t = self.find_elements(*self.product_title)
        return all_products_t[index].text

    def get_product_description(self, index):
        all_products_d = self.find_elements(*self.product_description)
        return all_products_d[index].text

    def add_to_cart(self, product_name):
        add_button_locator = self.add_button[1].format(item_name=product_name)
        self.click((self.add_button[0], add_button_locator))

    def remove_from_cart(self, product_name):
        remove_button_locator = self.remove_button[1].format(item_name=product_name)
        self.click((self.remove_button[0], remove_button_locator))



