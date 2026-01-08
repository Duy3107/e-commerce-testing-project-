from selenium.webdriver.common.by import By


class HomePage:
    URL = "https://automationexercise.com"

    # locators
    LOGIN_SIGNUP_LINK = (By.CSS_SELECTOR, "ul.nav a[href='/login']")
    PRODUCTS_LINK = (By.CSS_SELECTOR, "ul.nav a[href='/products']")
    CART_LINK = (By.CSS_SELECTOR, "ul.nav a[href='/view_cart']")
    TEST_CASES_LINK = (By.CSS_SELECTOR, "ul.nav a[href='/test_cases']")
    API_TESTING_LINK = (By.CSS_SELECTOR, "ul.nav a[href='/api_list']")
    CONTACT_US_LINK = (By.CSS_SELECTOR, "a[href='/contact_us']")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href='/logout']")
    LOGO = (By.CSS_SELECTOR, ".logo.pull-left")
    HOME_TITLE = (By.CSS_SELECTOR, "h1 span")
    DELETE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "ul.nav a[href='/delete_account']")

    def __init__(self, driver):
        self.driver = driver
        #self.wait = WebDriverWait(driver, 5)   next time should try explicit wait in helper methods

    def visit(self):
        self.driver.get(self.URL)

    def click_login_signup(self):
        self.driver.find_element(*self.LOGIN_SIGNUP_LINK).click()

    def click_products(self):
        self.driver.find_element(*self.PRODUCTS_LINK).click()

    def click_cart(self):
        self.driver.find_element(*self.CART_LINK).click()

    def click_test_cases(self):
        self.driver.find_element(*self.TEST_CASES_LINK).click()

    def click_api_testing(self):
        self.driver.find_element(*self.API_TESTING_LINK).click()

    def click_contact_us(self):
        self.driver.find_element(*self.CONTACT_US_LINK).click()

    def click_logout(self):
        self.driver.find_element(*self.LOGOUT_LINK).click()

    def click_logo(self):
        self.driver.find_element(*self.LOGO).click()

    def click_delete_account(self):
        self.driver.find_element(*self.DELETE_ACCOUNT_BUTTON).click()    

    def is_home_page_visible(self):
        return self.driver.find_element(*self.HOME_TITLE).is_displayed()
