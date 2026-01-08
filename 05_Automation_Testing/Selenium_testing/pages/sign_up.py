from selenium.webdriver.common.by import By

class SignUp:
    URL = "https://automationexercise.com/login"

    # locators
    NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    SIGNUP_FORM = (By.CSS_SELECTOR, ".signup-form")
    ENTER_ACCOUNT_INFO_TEXT = (By.CSS_SELECTOR, "h2.title.text-center b")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='password']")
    DATE_OF_BIRTH_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='days']")
    MONTH_OF_BIRTH_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='months']")
    YEAR_OF_BIRTH_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='years']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='first_name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='last_name']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[data-qa='address']")
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='country']")
    STATE_INPUT = (By.CSS_SELECTOR, "input[data-qa='state']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[data-qa='city']")
    ZIPCODE_INPUT = (By.CSS_SELECTOR, "input[data-qa='zipcode']")
    MOBILE_NUMBER_INPUT = (By.CSS_SELECTOR, "input[data-qa='mobile_number']")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(self.URL)

    def enter_name(self, name):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def click_signup(self):
        self.driver.find_element(*self.SIGNUP_BUTTON).click()

    def is_signup_page_visible(self):
        return self.driver.find_element(*self.SIGNUP_FORM).is_displayed()
    
    def is_account_info_page_loaded(self):
        return self.driver.find_element(*self.ENTER_ACCOUNT_INFO_TEXT).is_displayed()
    
    def enter_account_information(self):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys("TestPassword123")
        self.driver.find_element(*self.DATE_OF_BIRTH_DROPDOWN).send_keys("31")
        self.driver.find_element(*self.MONTH_OF_BIRTH_DROPDOWN).send_keys("July")
        self.driver.find_element(*self.YEAR_OF_BIRTH_DROPDOWN).send_keys("2002")
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys("Test")
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys("User")
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys("123 Test St")  
        self.driver.find_element(*self.COUNTRY_DROPDOWN).send_keys("United States")
        self.driver.find_element(*self.STATE_INPUT).send_keys("Test State") 
        self.driver.find_element(*self.CITY_INPUT).send_keys("Test City")
        self.driver.find_element(*self.ZIPCODE_INPUT).send_keys("12345")
        self.driver.find_element(*self.MOBILE_NUMBER_INPUT).send_keys("1234567890")
        self.driver.find_element(*self.CREATE_ACCOUNT_BUTTON).click()

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()    

       