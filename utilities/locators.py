from selenium.webdriver.common.by import By


class Utilities:
    pass

class BasePageLocators:
    cart_icon = (By.XPATH, '//a[@class="shopping_cart_link"]')


class ProductsLocators:
    product_button = (By.XPATH, '//div[@class="inventory_item_label"]/a/div[text()="{item_name}"]/../../following-sibling::div//button')


class CartLocators:
    remove_product_button = (By.XPATH, '//div[@class="cart_item_label"]/a/div[text()="{item_name}"]/../../div[@class="item_pricebar"]//button')


class CheckoutLocators:
    warning_message = (By.XPATH, '//h3[@data-test="error"]')
    checkout_item_name = (By.XPATH, '//div[@class="inventory_item_name"]')
    checkout_item_price = (By.XPATH, '//div[text()="{item_name}"]/../../div[@class="item_pricebar"]//div')
    checkout_message = (By.XPATH, '//div[@id="checkout_complete_container"]//h2')