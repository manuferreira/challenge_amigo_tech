from selenium.webdriver.common.by import By


class BasePageLocators:
    cart_icon = (By.XPATH, '//a[@class="shopping_cart_link"]')
