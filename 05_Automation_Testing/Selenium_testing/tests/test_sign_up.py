import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.sign_up import SignUp



def test_sign_up_page_visibility(driver):
    sign_up = SignUp(driver)
    sign_up.visit()
    assert sign_up.is_signup_page_visible()


def test_sign_up_with_existing_email(driver):
    wait = WebDriverWait(driver, 5)
    sign_up = SignUp(driver)
    sign_up.visit()
    sign_up.enter_name("Existing User")
    sign_up.enter_email("crisntdgamer@gmail.com")
    sign_up.click_signup()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Email Address already exist!')]")))
    assert "Email Address already exist!" in driver.page_source

    
def test_sign_up_process(driver):
    wait = WebDriverWait(driver, 10)
    temp = int(time.time())
    email = f"example+{temp}@email.com"
    sign_up = SignUp(driver)
    sign_up.visit()
    sign_up.enter_name("Test User")
    sign_up.enter_email(email)
    sign_up.click_signup()  
    assert sign_up.is_account_info_page_loaded()
    sign_up.enter_account_information()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Account Created!')]")))
    sign_up.click_continue()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Logged in as')]")))


