from pages.home_page import HomePage
from pages.add_to_cart import AddToCart
from pages.search_product import SearchProduct
from pages.log_in import LogIn
from pages.check_out import CheckOut


def test_check_out_process(driver):
    home_page = HomePage(driver)
    search_product = SearchProduct(driver)
    add_to_cart_page = AddToCart(driver)
    log_in_page = LogIn(driver)
    check_out_page = CheckOut(driver)
    home_page.visit()
    home_page.click_login_signup()
    log_in_page.enter_email("crisntdgamer@email.com")
    log_in_page.enter_password("Test@12345678")
    log_in_page.click_login()
    home_page.click_products()
    search_product.enter_search_term("Tshirt")
    search_product.click_search()
    add_to_cart_page.add_first_seached_product_to_cart()
    home_page.click_cart()
    assert add_to_cart_page.is_cart_not_empty()
    check_out_page.click_proceed_to_checkout()
    assert check_out_page.verify_address_details_are_visible()
    assert check_out_page.verify_products_in_order_summary()
    check_out_page.click_place_order()
    assert check_out_page.is_payment_page_visible()
    check_out_page.enter_card_details(
        name_on_card="Cristian Tdgamer",
        card_number="4111111111111111",
        cvc="123",
        exp_month="12",
        exp_year="2025"
    )
    check_out_page.click_confirm_order()
    assert check_out_page.is_order_placed_successfully()
    check_out_page.click_continue()
