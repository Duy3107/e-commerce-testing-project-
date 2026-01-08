import os
from selenium import webdriver

os.environ["SE_DRIVER_MIRROR_URL"] = "https://msedgedriver.microsoft.com"

def test_open_homepage():
    driver = webdriver.Edge()  # đơn giản hơn, không cần service
    driver.get("https://automationexercise.com")
    assert "Automation" in driver.title
    driver.quit()




# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager

# def test_open_homepage():
#     driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
#     driver.get("https://automationexercise.com")
#     assert "Automation" in driver.title
#     driver.quit()