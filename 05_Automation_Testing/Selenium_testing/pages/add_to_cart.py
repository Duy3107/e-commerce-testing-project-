from selenium.webdriver.common.by import By


class AddToCart:
    URL = "https://automationexercise.com/view_cart"

    # locators  
    PRODUCT_NAME = (By.CSS_SELECTOR, ".cart_info .cart_description h4 a")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".cart_info .cart_price p")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, ".cart_info .cart_quantity button")
    PRODUCT_TOTAL_PRICE = (By.CSS_SELECTOR, ".cart_info .cart_total_price p")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".cart_navigation a[href='/checkout']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".add-to-cart")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, ".text-center a[href='/view_cart']")


    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(self.URL)
       
    def is_cart_empty(self):
        cart_items = self.driver.find_elements(*self.PRODUCT_NAME)
        return len(cart_items) == 0   
    
    def is_cart_not_empty(self):
        cart_items = self.driver.find_elements(*self.PRODUCT_NAME)
        return len(cart_items) > 0

    def add_first_seached_product_to_cart(self): 
        first_product = self.driver.find_elements(*self.SEARCH_RESULTS)[0]
        add_to_cart_button = first_product.find_element(*self.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()


    