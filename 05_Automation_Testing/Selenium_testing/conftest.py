import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions

BROWSER = os.getenv("BROWSER", "edge")  # default: edge (local)

@pytest.fixture(scope="function")
def driver():
    if BROWSER == "chrome_ci":
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
    else:
        edge_options = EdgeOptions()
        driver = webdriver.Edge(options=edge_options)

    driver.maximize_window()
    yield driver
    driver.quit()
