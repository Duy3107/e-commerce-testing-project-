from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.add_to_cart import AddToCart
from pages.search_product import SearchProduct


def test_is_cart_empty_initially(driver):
    add_to_cart_page = AddToCart(driver)
    add_to_cart_page.visit()
    assert add_to_cart_page.is_cart_empty()


def  test_add_searched_product_to_cart(driver):
    home_page = HomePage(driver)
    search_product = SearchProduct(driver)
    add_to_cart_page = AddToCart(driver)
    home_page.visit()
    home_page.click_products()
    #search a product
    search_product.enter_search_term("Jeans")
    search_product.click_search()
    # Add the first searched product to cart
    add_to_cart_page.add_first_seached_product_to_cart()
    wait = WebDriverWait(driver, 5)    #set wait because the button need time to pop-up and become clickable
    wait.until(EC.element_to_be_clickable(add_to_cart_page.VIEW_CART_BUTTON)).click()
    # Verify that the cart is not empty after adding a product
    assert add_to_cart_page.is_cart_not_empty()


       
