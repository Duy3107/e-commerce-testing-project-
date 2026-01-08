import os
import pytest
from selenium import webdriver


os.environ["SE_DRIVER_MIRROR_URL"] = "https://msedgedriver.microsoft.com"

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()