from .base_page import BasePage
from .locators import WebFormLocators


class WebFormPage(BasePage):
    """Page object for the Selenium web form demo page"""
    
    def fill_text_input(self, text):
        """Fill the text input field"""
        text_input = self.find_element(WebFormLocators.TEXT_INPUT)
        text_input.clear()
        text_input.send_keys(text)
        return self.get_attribute(WebFormLocators.TEXT_INPUT, "value")
    
    def fill_password_input(self, password):
        """Fill the password input field"""
        password_input = self.find_element(WebFormLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)
        return self.get_attribute(WebFormLocators.PASSWORD_INPUT, "value")
    
    def fill_textarea_input(self, text):
        """Fill the textarea input field"""
        textarea = self.find_element(WebFormLocators.TEXTAREA_INPUT)
        textarea.clear()
        textarea.send_keys(text)
        return self.get_attribute(WebFormLocators.TEXTAREA_INPUT, "value")