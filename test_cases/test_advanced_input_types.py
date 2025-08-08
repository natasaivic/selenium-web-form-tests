from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os


def test_color_picker(driver):
    color_picker = driver.find_element(By.NAME, "my-colors")
    test_color = "#ff5733"
    
    # Set color using JavaScript (more reliable for color inputs)
    driver.execute_script(f"arguments[0].value = '{test_color}';", color_picker)
    
    assert color_picker.get_attribute("value") == test_color
    print(f"✅ Color picker test passed: {test_color}")


def test_date_picker(driver):
    date_picker = driver.find_element(By.NAME, "my-date")
    test_date = "2024-12-25"
    
    date_picker.clear()
    date_picker.send_keys(test_date)
    
    assert date_picker.get_attribute("value") == test_date
    print(f"✅ Date picker test passed: {test_date}")


def test_range_slider(driver):
    range_slider = driver.find_element(By.NAME, "my-range")
    
    # Get initial value
    initial_value = range_slider.get_attribute("value")
    
    # Move slider using ActionChains
    actions = ActionChains(driver)
    actions.click_and_hold(range_slider).move_by_offset(50, 0).release().perform()
    
    # Verify value changed
    new_value = range_slider.get_attribute("value")
    assert new_value != initial_value
    
    print(f"✅ Range slider test passed: {initial_value} → {new_value}")


def test_file_upload(driver):
    file_input = driver.find_element(By.NAME, "my-file")
    
    # Create a temporary test file
    test_file_path = "/tmp/test_upload.txt"
    with open(test_file_path, "w") as f:
        f.write("This is a test file for upload")
    
    try:
        # Upload the file
        file_input.send_keys(test_file_path)
        
        # Verify file is selected (check if value contains filename)
        uploaded_filename = file_input.get_attribute("value")
        assert "test_upload.txt" in uploaded_filename
        
        print(f"✅ File upload test passed: {uploaded_filename}")
        
    finally:
        # Clean up test file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)