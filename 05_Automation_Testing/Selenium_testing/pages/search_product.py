from selenium.webdriver.common.by import By

class SearchProduct:
    URL = "https://automationexercise.com/products"

    # locators
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='search_product']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[id='submit_search']")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(self.URL)

    def enter_search_term(self, term):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(term)

    def clear_search_term(self):
        self.driver.find_element(*self.SEARCH_INPUT).clear()    

    def click_search(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def is_search_results_visible(self):
        return len(self.driver.find_elements(*self.SEARCH_RESULTS)) > 0
    
    def is_search_results_empty(self):
        return len(self.driver.find_elements(*self.SEARCH_RESULTS)) == 0