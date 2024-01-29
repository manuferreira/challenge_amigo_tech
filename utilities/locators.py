from selenium.webdriver.common.by import By


class Utilities:
    any_button = (By.XPATH, '//button[text()="{button_action}"]')

class BasePageLocators:
    cart_icon = (By.XPATH, '//a[@class="shopping_cart_link"]')


class ProductsLocators:
    product_button = (By.XPATH, '//div[@class="inventory_item_label"]/a/div[text()="{item_name}"]/../../following-sibling::div//button')
    product_name = (By.XPATH, '//div[contains(@class, "inventory_details_name")]')
    product_description = (By.XPATH, '//div[contains(@class, "inventory_details_desc ")]')
    product_price = (By.CLASS_NAME, 'inventory_details_price')
    product_name_home = (By.XPATH, '//div[contains(text(), "{item_name}")]')

class CartLocators:
    remove_product_button = (By.XPATH, '//div[@class="cart_item_label"]/a/div[text()="{item_name}"]/../../div[@class="item_pricebar"]//button')


class CheckoutLocators:
    warning_message = (By.XPATH, '//h3[@data-test="error"]')
    checkout_item_name = (By.XPATH, '//div[@class="inventory_item_name"]')
    checkout_item_price = (By.XPATH, '//div[text()="{item_name}"]/../../div[@class="item_pricebar"]//div')
    checkout_message = (By.XPATH, '//div[@id="checkout_complete_container"]//h2')