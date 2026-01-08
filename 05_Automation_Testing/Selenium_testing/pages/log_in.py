from selenium.webdriver.common.by import By 


class LogIn:
    URL = "https://automationexercise.com/login"

    # locators
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGIN_FORM = (By.CSS_SELECTOR, ".login-form")

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(self.URL)

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_login_page_visible(self):
        return self.driver.find_element(*self.LOGIN_FORM).is_displayed()