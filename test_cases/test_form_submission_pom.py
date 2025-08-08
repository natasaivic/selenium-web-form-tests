from page_objects.locators import WebFormLocators
import time


def test_complete_form_submission_pom(web_form_page):
    # Fill text input
    web_form_page.fill_text_input("Comprehensive Test")
    
    # Fill password
    web_form_page.fill_password_input("TestPassword123")
    
    # Fill textarea
    web_form_page.fill_textarea_input("This is a comprehensive form test covering all fields.")
    
    # Select dropdown option
    web_form_page.select_dropdown_by_text(WebFormLocators.DROPDOWN_SELECT, "Three")
    
    # Fill datalist
    web_form_page.fill_datalist(WebFormLocators.DROPDOWN_DATALIST, "Los Angeles")
    
    # Set color
    web_form_page.set_color_picker("#33ff57")
    
    # Set date
    web_form_page.set_date_picker("2024-06-15")
    
    # Upload test file
    web_form_page.upload_file("Comprehensive test file content", "comprehensive_test.txt")
    
    # Adjust range slider
    web_form_page.move_range_slider(30)
    
    # Ensure checked checkbox is selected
    checkbox_1_state = web_form_page.get_checkbox_state(WebFormLocators.CHECKBOX_CHECKED)
    if not checkbox_1_state:
        web_form_page.toggle_checkbox(WebFormLocators.CHECKBOX_CHECKED)
    
    # Select default checkbox
    checkbox_2_state = web_form_page.get_checkbox_state(WebFormLocators.CHECKBOX_DEFAULT)
    if not checkbox_2_state:
        web_form_page.toggle_checkbox(WebFormLocators.CHECKBOX_DEFAULT)
    
    # Select checked radio button
    web_form_page.click_radio_button(WebFormLocators.RADIO_CHECKED)
    
    # Submit form
    submit_button = web_form_page.find_element(WebFormLocators.SUBMIT_BUTTON)
    submit_button.click()
    
    # Wait for and verify success message
    time.sleep(2)
    success_message = web_form_page.find_element(WebFormLocators.SUCCESS_MESSAGE)
    message_text = success_message.text
    
    assert "Received!" in message_text
    print("✅ Complete form submission POM test passed")
    print(f"Success message: {message_text}")