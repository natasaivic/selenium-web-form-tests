import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.web_form_page import WebFormPage


@pytest.fixture
def driver():
    """Shared WebDriver fixture for all tests"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    yield driver
    driver.quit()


@pytest.fixture
def web_form_page(driver):
    """Shared WebFormPage fixture for POM tests"""
    return WebFormPage(driver)