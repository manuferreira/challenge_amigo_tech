import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import Homepage
from conftest import initialize_driver

@pytest.mark.usefixtures("initialize_driver")
class TestCartPage:

    def test_add_to_cart(self, initialize_driver):
        cart_page = CartPage(initialize_driver)
        home_page = Homepage(initialize_driver)
        first_item = "Sauce Labs Backpack"
        second_item = "Sauce Labs Bike Light"

        home_page.add_to_cart(first_item)
        home_page.add_to_cart(second_item)

        home_page.go_to_cart()

        expected_first_item = cart_page.get_product_title(0)
        assert first_item == expected_first_item

        expected_second_item = cart_page.get_product_title(1)
        assert second_item == expected_second_item

    def test_remove_items_from_cart(self, initialize_driver):
        cart_page = CartPage(initialize_driver)
        home_page = Homepage(initialize_driver)
        first_item = "Sauce Labs Backpack"
        second_item = "Sauce Labs Bike Light"

        home_page.add_to_cart(first_item)
        home_page.add_to_cart(second_item)

        home_page.go_to_cart()

        cart_page.delete_from_cart(first_item)
        cart_page.delete_from_cart(second_item)

        assert not cart_page.item_not_present(0)

    def test_continue_shopping(self, initialize_driver):
        cart_page = CartPage(initialize_driver)
        home_page = Homepage(initialize_driver)
        first_item = "Sauce Labs Backpack"
        second_item = "Sauce Labs Bolt T-Shirt"

        home_page.add_to_cart(first_item)
        home_page.go_to_cart()

        cart_page.click_to_continue_shopping()

        home_page.add_to_cart(second_item)

        home_page.go_to_cart()

        expected_first_item = cart_page.get_product_title(0)
        assert first_item == expected_first_item

        expected_second_item = cart_page.get_product_title(1)
        assert second_item == expected_second_item

    def test_assert_total_price(self, initialize_driver):
        cart_page = CartPage(initialize_driver)
        home_page = Homepage(initialize_driver)
        checkout = CheckoutPage(initialize_driver)
        first_item = "Sauce Labs Backpack"
        second_item = "Sauce Labs Bolt T-Shirt"

        home_page.add_to_cart(first_item)
        home_page.add_to_cart(second_item)
        home_page.go_to_cart()

        cart_page.click_to_checkout()
        checkout.set_first_name("john")
        checkout.set_last_name("doe")
        checkout.set_zip_code(12345)

        checkout.continue_to_checkout()

        first_item_price = checkout.get_item_price(first_item)
        second_item_price = checkout.get_item_price(second_item)

        total_price_items = first_item_price + second_item_price
        subtotal_price_items = checkout.get_total_price_cart()

        assert total_price_items == subtotal_price_items

    def test_buy_products(self, initialize_driver):
        cart_page = CartPage(initialize_driver)
        home_page = Homepage(initialize_driver)
        checkout = CheckoutPage(initialize_driver)
        first_item = "Sauce Labs Backpack"
        second_item = "Sauce Labs Bolt T-Shirt"

        home_page.add_to_cart(first_item)
        home_page.add_to_cart(second_item)
        home_page.go_to_cart()

        cart_page.click_to_checkout()
        checkout.set_first_name("john")
        checkout.set_last_name("doe")
        checkout.set_zip_code(12345)

        checkout.continue_to_checkout()
        checkout.click_to_finish_checkout()
        actual_success_message = checkout.get_success_checkout_message()
        assert "Thank you for your order!" == actual_success_message

    def test_checkout_without_first_name(self, initialize_driver):
        cart_page = CartPage(initialize_driver)
        home_page = Homepage(initialize_driver)
        checkout = CheckoutPage(initialize_driver)
        first_item = "Sauce Labs Backpack"

        home_page.add_to_cart(first_item)
        home_page.go_to_cart()
        cart_page.click_to_checkout()
        checkout.set_last_name("doe")
        checkout.set_zip_code(12345)

        checkout.continue_to_checkout()
        actual_warning_message = checkout.get_warning_message()
        assert "Error: First Name is required" == actual_warning_message

    def test_checkout_without_last_name(self, initialize_driver):
        cart_page = CartPage(initialize_driver)
        home_page = Homepage(initialize_driver)
        checkout = CheckoutPage(initialize_driver)
        first_item = "Sauce Labs Backpack"

        home_page.add_to_cart(first_item)
        home_page.go_to_cart()
        cart_page.click_to_checkout()
        checkout.set_first_name("john")
        checkout.set_zip_code(12345)

        checkout.continue_to_checkout()
        actual_warning_message = checkout.get_warning_message()
        assert "Error: Last Name is required" == actual_warning_message

    def test_checkout_without_zip_code(self, initialize_driver):
        cart_page = CartPage(initialize_driver)
        home_page = Homepage(initialize_driver)
        checkout = CheckoutPage(initialize_driver)
        first_item = "Sauce Labs Backpack"

        home_page.add_to_cart(first_item)
        home_page.go_to_cart()
        cart_page.click_to_checkout()
        checkout.set_first_name("john")
        checkout.set_last_name("doe")

        checkout.continue_to_checkout()
        actual_warning_message = checkout.get_warning_message()
        assert "Error: Postal Code is required" == actual_warning_message

    def test_checkout_empty_cart(self, initialize_driver):
        #bug here: it's possible to checkout with an empty cart
        pass

