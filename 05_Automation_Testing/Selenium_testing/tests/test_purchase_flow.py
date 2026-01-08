import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.sign_up import SignUp
from pages.log_in import LogIn
from pages.search_product import SearchProduct
from pages.add_to_cart import AddToCart
from pages.check_out import CheckOut



def test_complete_purchase_flow(driver):    
    home_page = HomePage(driver)
    sign_up_page = SignUp(driver)
    log_in_page = LogIn(driver)
    search_product = SearchProduct(driver)
    add_to_cart_page = AddToCart(driver)
    check_out_page = CheckOut(driver)
    wait = WebDriverWait(driver, 8)
    # Visit home page
    home_page.visit()
    assert home_page.is_home_page_visible()

    # Sign up a new user
    home_page.click_login_signup()
    assert sign_up_page.is_signup_page_visible()
    temp = int(time.time())
    email = f"example+{temp}@email.com"
    sign_up_page.enter_name("Test User")
    sign_up_page.enter_email(email)
    sign_up_page.click_signup()
    assert sign_up_page.is_account_info_page_loaded()
    sign_up_page.enter_account_information()
    assert "Account Created!" in driver.page_source
    sign_up_page.click_continue()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Logged in as')]")))
    assert "Logged in as" in driver.page_source
    
    #logout and log back in
    home_page.click_logout()
    home_page.click_login_signup()
    assert log_in_page.is_login_page_visible()
    log_in_page.enter_email(email)
    log_in_page.enter_password("TestPassword123")
    log_in_page.click_login()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Logged in as')]")))     # "//" means choose from anywhere in the page and "*" means any tag
    assert "Logged in as" in driver.page_source

    # Search for a product
    home_page.click_products()
    search_product.enter_search_term("Tshirt")
    search_product.click_search()
    assert search_product.is_search_results_visible()
    search_product.clear_search_term()
    search_product.enter_search_term("NonExistentProduct")
    search_product.click_search()
    assert search_product.is_search_results_empty()
    search_product.clear_search_term()
    search_product.enter_search_term("Jeans")
    search_product.click_search()
    assert search_product.is_search_results_visible()

    # Add product to cart
    add_to_cart_page.add_first_seached_product_to_cart()
    wait.until(EC.element_to_be_clickable(add_to_cart_page.VIEW_CART_BUTTON)).click()
    assert add_to_cart_page.is_cart_not_empty()

    # Proceed to checkout
    check_out_page.click_proceed_to_checkout()
    assert check_out_page.verify_address_details_are_visible()
    assert check_out_page.verify_products_in_order_summary()
    check_out_page.click_place_order()
    assert check_out_page.is_payment_page_visible()
    check_out_page.enter_card_details(
        name_on_card="Test User",
        card_number="4111111111111111",
        cvc="123",
        exp_month="12",
        exp_year="2025"
    )
    check_out_page.click_confirm_order()
    assert check_out_page.is_order_placed_successfully()
    check_out_page.click_continue()

    # Delete account
    assert home_page.is_home_page_visible()
    home_page.click_delete_account()
    assert "Account Deleted!" in driver.page_source

