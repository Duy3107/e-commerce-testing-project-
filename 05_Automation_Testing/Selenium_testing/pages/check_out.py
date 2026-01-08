from selenium.webdriver.common.by import By


class CheckOut:
    URL = "https://automationexercise.com/checkout"

    # locators
    ADDRESS_DETAIL = (By.CSS_SELECTOR, "h2[class='heading']")
    ADDRESS_FIRST_NAME = (By.CSS_SELECTOR, "li[class='address_firstname address_lastname']")
    ADDRESS_ADDRESS = (By.CSS_SELECTOR, "li[class='address_address1 address_address2']")
    ADDRESS_CITY_STATE_ZIP = (By.CSS_SELECTOR, "li[class~='address_city']")
    ADDRESS_COUNTRY = (By.CSS_SELECTOR, "li[class='address_country_name']")
    ADRESS_PHONE = (By.CSS_SELECTOR, "li[class='address_phone']")
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, "a[href='/payment']")
    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-default.check_out")
    PRODUCT_IN_ORDER = (By.CSS_SELECTOR, "table[class='table table-condensed']")
    PAYMENT_TITLE = (By.CSS_SELECTOR, "h2[class='heading']")
    NAME_ON_CARD_INPUT = (By.CSS_SELECTOR, "input[data-qa='name-on-card']")
    CARD_NUMBER_INPUT = (By.CSS_SELECTOR, "input[data-qa='card-number']")
    CVC_INPUT = (By.CSS_SELECTOR, "input[data-qa='cvc']")
    EXPIRATION_MONTH_INPUT = (By.CSS_SELECTOR, "input[data-qa='expiry-month']")
    EXPIRATION_YEAR_INPUT = (By.CSS_SELECTOR, "input[data-qa='expiry-year']")
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, "button[data-qa='pay-button']")
    ORDER_PLACED_MESSAGE = (By.CSS_SELECTOR, "h2[data-qa='order-placed']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")


    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(self.URL)

    def click_proceed_to_checkout(self):
        self.driver.find_element(*self.PROCEED_TO_CHECKOUT_BUTTON).click()

    def verify_address_details_are_visible(self):
        return (
            self.driver.find_element(*self.ADDRESS_DETAIL).is_displayed()
            and self.driver.find_element(*self.ADDRESS_FIRST_NAME).is_displayed()
            and self.driver.find_element(*self.ADDRESS_CITY_STATE_ZIP).is_displayed()
            and self.driver.find_element(*self.ADDRESS_COUNTRY).is_displayed()
            and self.driver.find_element(*self.ADRESS_PHONE).is_displayed()
    )
    
    def verify_products_in_order_summary(self):
        return len(self.driver.find_elements(*self.PRODUCT_IN_ORDER)) > 0
    
    def is_payment_page_visible(self):
        return self.driver.find_element(*self.PAYMENT_TITLE).is_displayed()
    
    def enter_card_details(self, name_on_card, card_number, cvc, exp_month, exp_year):
        self.driver.find_element(*self.NAME_ON_CARD_INPUT).send_keys(name_on_card)
        self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(card_number)
        self.driver.find_element(*self.CVC_INPUT).send_keys(cvc)
        self.driver.find_element(*self.EXPIRATION_MONTH_INPUT).send_keys(exp_month)
        self.driver.find_element(*self.EXPIRATION_YEAR_INPUT).send_keys(exp_year)

    def click_place_order(self):
        self.driver.find_element(*self.PLACE_ORDER_BUTTON).click()    

    def click_confirm_order(self):
        self.driver.find_element(*self.CONFIRM_ORDER_BUTTON).click()    

    def is_order_placed_successfully(self):
        return self.driver.find_element(*self.ORDER_PLACED_MESSAGE).is_displayed()    
    
    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        