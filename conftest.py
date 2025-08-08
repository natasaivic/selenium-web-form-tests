import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


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