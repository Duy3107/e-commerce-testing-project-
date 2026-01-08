from pages.sign_up import SignUp
from pages.log_in import LogIn
from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def test_login_page_visibility(driver):
    login = LogIn(driver)
    login.visit()
    assert login.is_login_page_visible()


def test_login_with_invalid_credentials(driver):
    wait = WebDriverWait(driver, 5)
    login = LogIn(driver)
    login.visit()
    login.enter_email("asd@example.com")
    login.enter_password("wrongpassword")
    login.click_login()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Your email or password is incorrect!')]")))
    assert "Your email or password is incorrect!" in driver.page_source


def test_login_with_valid_credentials(driver):
    login = LogIn(driver)
    wait = WebDriverWait(driver, 5)
    login.visit()
    login.enter_email("crisntdgamer@email.com")
    login.enter_password("Test@12345678")
    login.click_login()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Logged in as')]")))
    assert "Logged in as" in driver.page_source
    homepage = HomePage(driver)
    homepage.click_logout()

