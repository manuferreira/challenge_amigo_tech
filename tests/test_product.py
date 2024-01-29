import pytest

from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import Homepage
from pages.product_page import ProductPage
from conftest import initialize_driver

@pytest.mark.usefixtures("initialize_driver")
class TestProductPage:

    def test_check_product_name(self, initialize_driver):
        home_page = Homepage(initialize_driver)
        product_page = ProductPage(initialize_driver)
        item_name = "Sauce Labs Backpack"

        home_page.go_to_product(product_name=item_name)

        actual_product = product_page.get_product_page_title()
        assert item_name == actual_product

    def test_check_product_description(self, initialize_driver):
        home_page = Homepage(initialize_driver)
        product_page = ProductPage(initialize_driver)
        item_name = "Sauce Labs Backpack"
        item_description = "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."

        home_page.go_to_product(product_name=item_name)

        actual_product_description = product_page.get_product_page_description()
        assert item_description == actual_product_description

    def test_check_product_price(self, initialize_driver):
        home_page = Homepage(initialize_driver)
        product_page = ProductPage(initialize_driver)
        item_name = "Sauce Labs Backpack"
        item_price = "$29.99"

        home_page.go_to_product(product_name=item_name)

        actual_product_price = product_page.get_product_page_price()
        assert item_price == actual_product_price

    def test_add_to_cart_from_product_page(self, initialize_driver):
        home_page = Homepage(initialize_driver)
        product_page = ProductPage(initialize_driver)
        cart_page = CartPage(initialize_driver)
        item_name = "Sauce Labs Backpack"
        home_page.go_to_product(product_name=item_name)

        product_page.add_from_item_page_to_cart()
        product_page.go_to_cart()
        actual_product = cart_page.get_product_title(0)
        assert item_name == actual_product

    def test_remove_from_cart_from_product_page(self, initialize_driver):
        home_page = Homepage(initialize_driver)
        product_page = ProductPage(initialize_driver)
        cart_page = CartPage(initialize_driver)
        item_name = "Sauce Labs Backpack"
        home_page.go_to_product(product_name=item_name)

        product_page.add_from_item_page_to_cart()
        product_page.go_to_cart()
        actual_product = cart_page.get_product_title(0)
        assert item_name == actual_product
        cart_page.go_back()
        product_page.remove_from_item_page_to_cart()

        product_page.go_to_cart()
        assert not cart_page.item_not_present(0)
