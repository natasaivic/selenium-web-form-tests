from selenium.webdriver.common.by import By


class WebFormLocators:
    """Centralized locators for the Selenium web form demo page"""
    
    # Text input elements - only what we need for test_text_inputs.py
    TEXT_INPUT = (By.NAME, "my-text")
    PASSWORD_INPUT = (By.NAME, "my-password") 
    TEXTAREA_INPUT = (By.NAME, "my-textarea")
    
    # Form submission
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.ID, "message")