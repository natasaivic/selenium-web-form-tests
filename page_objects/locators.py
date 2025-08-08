from selenium.webdriver.common.by import By


class WebFormLocators:
    """Centralized locators for the Selenium web form demo page"""
    
    # Text input elements
    TEXT_INPUT = (By.NAME, "my-text")
    PASSWORD_INPUT = (By.NAME, "my-password") 
    TEXTAREA_INPUT = (By.NAME, "my-textarea")
    
    # Advanced input types
    COLOR_PICKER = (By.NAME, "my-colors")
    DATE_PICKER = (By.NAME, "my-date")
    RANGE_SLIDER = (By.NAME, "my-range")
    FILE_INPUT = (By.NAME, "my-file")

    # Selection controls
    CHECKBOX_CHECKED = (By.ID, "my-check-1")
    CHECKBOX_DEFAULT = (By.ID, "my-check-2")
    RADIO_CHECKED = (By.ID, "my-radio-1")
    RADIO_DEFAULT = (By.ID, "my-radio-2")
    DROPDOWN_SELECT = (By.NAME, "my-select")
    DROPDOWN_DATALIST = (By.NAME, "my-datalist")
    
    # Field states
    DISABLED_INPUT = (By.NAME, "my-disabled")
    READONLY_INPUT = (By.NAME, "my-readonly")
    
    # Form submission
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.ID, "message")