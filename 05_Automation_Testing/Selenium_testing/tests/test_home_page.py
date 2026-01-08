from pages.home_page import HomePage


def test_navigate_login_signup(driver):
    home = HomePage(driver)
    home.visit()
    assert home.is_home_page_visible()
    home.click_login_signup()
    assert "/login" in driver.current_url


def test_navigate_products(driver):
    home = HomePage(driver)
    home.visit()
    home.click_products()
    assert "/products" in driver.current_url


def test_navigate_cart(driver):
    home = HomePage(driver)
    home.visit()
    home.click_cart()
    assert "/view_cart" in driver.current_url    


def test_navigate_test_cases(driver):
    home = HomePage(driver)
    home.visit()
    home.click_test_cases()
    assert "/test_cases" in driver.current_url


def test_navigate_api_testing(driver):
    home = HomePage(driver)
    home.visit()
    home.click_api_testing()
    assert "/api_list" in driver.current_url


def test_navigate_contact_us(driver):
    home = HomePage(driver)
    home.visit()
    home.click_contact_us()
    assert "/contact_us" in driver.current_url


# def test_navigate_logout(driver):                              disabled temporarily due to guest status
#     home = HomePage(driver)
#     home.visit()
#     home.click_logout()
#     assert "/login" in driver.current_url


def test_click_logo_navigates_home(driver):
    home = HomePage(driver)
    home.visit()
    home.click_products()  # Navigate away from homepage temporarily
    home.click_logo()      # Click on the logo to return home
    assert home.is_home_page_visible()  


def test_click_all_links(driver):
    home = HomePage(driver)
    home.visit()
    home.click_login_signup()
    assert "/login" in driver.current_url
    home.click_products()
    assert "/products" in driver.current_url
    home.click_cart()
    assert "/view_cart" in driver.current_url
    home.click_test_cases()
    assert "/test_cases" in driver.current_url
    home.click_api_testing()
    assert "/api_list" in driver.current_url
    home.click_contact_us()
    assert "/contact_us" in driver.current_url