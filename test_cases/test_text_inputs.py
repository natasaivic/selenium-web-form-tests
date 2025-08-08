from selenium.webdriver.common.by import By


def test_text_input(driver):
    text_box = driver.find_element(By.NAME, "my-text")
    test_text = "Test Text Input"
    
    text_box.clear()
    text_box.send_keys(test_text)
    
    assert text_box.get_attribute("value") == test_text
    print(f"✅ Text input test passed: '{test_text}'")


def test_password_input(driver):
    password_box = driver.find_element(By.NAME, "my-password")
    test_password = "SecurePassword123"
    
    password_box.clear()
    password_box.send_keys(test_password)
    
    assert password_box.get_attribute("value") == test_password
    print(f"✅ Password input test passed")


def test_textarea_input(driver):
    textarea = driver.find_element(By.NAME, "my-textarea")
    test_text = "This is a test message in the textarea field.\nMultiple lines are supported."
    
    textarea.clear()
    textarea.send_keys(test_text)
    
    assert textarea.get_attribute("value") == test_text
    print(f"✅ Textarea input test passed")