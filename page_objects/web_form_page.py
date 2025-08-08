from .base_page import BasePage
from .locators import WebFormLocators
from selenium.common.exceptions import ElementNotInteractableException
import os


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
    
    def set_color_picker(self, color):
        """Set color picker value using JavaScript"""
        color_picker = self.find_element(WebFormLocators.COLOR_PICKER)
        self.execute_script(f"arguments[0].value = '{color}';", color_picker)
        return self.get_attribute(WebFormLocators.COLOR_PICKER, "value")
        
    def set_date_picker(self, date):
        """Set date picker value"""
        date_picker = self.find_element(WebFormLocators.DATE_PICKER)
        date_picker.clear()
        date_picker.send_keys(date)
        return self.get_attribute(WebFormLocators.DATE_PICKER, "value")
     
    def move_range_slider(self, offset_x=50):
        """Move range slider by specified offset"""
        range_slider = self.find_element(WebFormLocators.RANGE_SLIDER)
        initial_value = self.get_attribute(WebFormLocators.RANGE_SLIDER, "value")
        
        self.actions.click_and_hold(range_slider).move_by_offset(offset_x, 0).release().perform()
        
        new_value = self.get_attribute(WebFormLocators.RANGE_SLIDER, "value")
        return initial_value, new_value
   
    def upload_file(self, file_content, filename="test_upload.txt"):
        """Upload file with specified content"""
        file_input = self.find_element(WebFormLocators.FILE_INPUT)
        
        # Create temporary test file
        test_file_path = f"/tmp/{filename}"
        with open(test_file_path, "w") as f:
            f.write(file_content)
        
        try:
            file_input.send_keys(test_file_path)
            uploaded_filename = self.get_attribute(WebFormLocators.FILE_INPUT, "value")
            return uploaded_filename
        finally:
            # Clean up test file
            if os.path.exists(test_file_path):
                os.remove(test_file_path)
    
    def toggle_checkbox(self, checkbox_locator):
        """Toggle checkbox and return its new state"""
        checkbox = self.find_element(checkbox_locator)
        initial_state = self.is_selected(checkbox_locator)
        checkbox.click()
        new_state = self.is_selected(checkbox_locator)
        return initial_state, new_state
    
    def get_checkbox_state(self, checkbox_locator):
        """Get current checkbox state"""
        return self.is_selected(checkbox_locator)
    
    def click_radio_button(self, radio_locator):
        """Click radio button"""
        radio_button = self.find_element(radio_locator)
        radio_button.click()
    
    def get_radio_states(self, radio1_locator, radio2_locator):
        """Get states of both radio buttons as tuple"""
        return self.is_selected(radio1_locator), self.is_selected(radio2_locator)
    
    def select_dropdown_by_text(self, dropdown_locator, text):
        """Select dropdown option by visible text"""
        dropdown = self.get_select(dropdown_locator)
        dropdown.select_by_visible_text(text)
        return dropdown.first_selected_option.text
    
    def select_dropdown_by_value(self, dropdown_locator, value):
        """Select dropdown option by value"""
        dropdown = self.get_select(dropdown_locator)
        dropdown.select_by_value(value)
        return dropdown.first_selected_option.get_attribute("value")
    
    def fill_datalist(self, datalist_locator, text):
        """Fill datalist input field"""
        datalist = self.find_element(datalist_locator)
        datalist.clear()
        datalist.send_keys(text)
        return self.get_attribute(datalist_locator, "value")
    
    def test_disabled_field(self, field_locator):
        """Test disabled field properties and interaction"""
        
        is_enabled = self.is_enabled(field_locator)
        placeholder = self.get_attribute(field_locator, "placeholder")
        
        # Test interaction fails
        interaction_blocked = False
        try:
            element = self.find_element(field_locator)
            element.send_keys("Test input")
        except ElementNotInteractableException:
            interaction_blocked = True
            
        return is_enabled, placeholder, interaction_blocked
    
    def test_readonly_field(self, field_locator):
        """Test readonly field properties and interaction"""
        is_enabled = self.is_enabled(field_locator)
        readonly_attr = self.get_attribute(field_locator, "readonly")
        initial_value = self.get_attribute(field_locator, "value")
        
        # Test if clear/send_keys operations are blocked
        element = self.find_element(field_locator)
        clear_blocked = False
        sendkeys_blocked = False
        
        try:
            element.clear()
        except:
            clear_blocked = True
            
        try:
            element.send_keys("Test input")
        except:
            sendkeys_blocked = True
            
        return is_enabled, readonly_attr, initial_value, clear_blocked, sendkeys_blocked