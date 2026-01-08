from pages.home_page import HomePage
from pages.search_product import SearchProduct


def test_search_non_existing_product(driver):
    search_product = SearchProduct(driver)
    search_product.visit()
    search_product.enter_search_term("Spiderman Costume")
    search_product.click_search()
    search_product.is_search_results_empty()
   

def test_search_existing_product(driver):
    search_product = SearchProduct(driver)
    search_product.visit()
    search_product.enter_search_term("Jeans")
    search_product.click_search()
    assert search_product.is_search_results_visible()
    search_product.clear_search_term()
    search_product.enter_search_term("Tops")
    search_product.click_search()
    assert search_product.is_search_results_visible()


