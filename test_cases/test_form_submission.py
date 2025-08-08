from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import os
import time


def test_complete_form_submission(driver):
    # Fill text input
    text_input = driver.find_element(By.NAME, "my-text")
    text_input.clear()
    text_input.send_keys("Comprehensive Test")
    
    # Fill password
    password_input = driver.find_element(By.NAME, "my-password")
    password_input.clear()
    password_input.send_keys("TestPassword123")
    
    # Fill textarea
    textarea = driver.find_element(By.NAME, "my-textarea")
    textarea.clear()
    textarea.send_keys("This is a comprehensive form test covering all fields.")
    
    # Select dropdown option
    dropdown = Select(driver.find_element(By.NAME, "my-select"))
    dropdown.select_by_visible_text("Three")
    
    # Fill datalist
    datalist = driver.find_element(By.NAME, "my-datalist")
    datalist.clear()
    datalist.send_keys("Los Angeles")
    
    # Set color
    color_picker = driver.find_element(By.NAME, "my-colors")
    driver.execute_script("arguments[0].value = '#33ff57';", color_picker)
    
    # Set date
    date_picker = driver.find_element(By.NAME, "my-date")
    date_picker.clear()
    date_picker.send_keys("2024-06-15")
    
    # Create and upload test file
    test_file_path = "/tmp/comprehensive_test.txt"
    with open(test_file_path, "w") as f:
        f.write("Comprehensive test file content")
    
    try:
        file_input = driver.find_element(By.NAME, "my-file")
        file_input.send_keys(test_file_path)
        
        # Adjust range slider
        range_slider = driver.find_element(By.NAME, "my-range")
        actions = ActionChains(driver)
        actions.click_and_hold(range_slider).move_by_offset(30, 0).release().perform()
        
        # Ensure checked checkbox is selected
        checkbox_1 = driver.find_element(By.ID, "my-check-1")
        if not checkbox_1.is_selected():
            checkbox_1.click()
        
        # Select default checkbox
        checkbox_2 = driver.find_element(By.ID, "my-check-2")
        if not checkbox_2.is_selected():
            checkbox_2.click()
        
        # Select checked radio button
        radio_1 = driver.find_element(By.ID, "my-radio-1")
        radio_1.click()
        
        # Submit form
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # Wait for and verify success message
        time.sleep(2)
        success_message = driver.find_element(By.ID, "message")
        message_text = success_message.text
        
        assert "Received!" in message_text
        print("✅ Complete form submission test passed")
        print(f"Success message: {message_text}")
        
    finally:
        # Clean up test file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)