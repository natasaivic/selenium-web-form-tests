from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_checkbox_checked(driver):
    checkbox = driver.find_element(By.ID, "my-check-1")
    
    # Verify it's initially checked
    assert checkbox.is_selected()
    
    # Uncheck and verify
    checkbox.click()
    assert not checkbox.is_selected()
    
    # Check again and verify
    checkbox.click()
    assert checkbox.is_selected()
    
    print("✅ Checked checkbox test passed")


def test_checkbox_default(driver):
    checkbox = driver.find_element(By.ID, "my-check-2")
    
    # Verify it's initially unchecked
    assert not checkbox.is_selected()
    
    # Check and verify
    checkbox.click()
    assert checkbox.is_selected()
    
    # Uncheck and verify
    checkbox.click()
    assert not checkbox.is_selected()
    
    print("✅ Default checkbox test passed")


def test_radio_button_group(driver):
    radio_checked = driver.find_element(By.ID, "my-radio-1")
    radio_default = driver.find_element(By.ID, "my-radio-2")
    
    # Verify initial states
    assert radio_checked.is_selected()
    assert not radio_default.is_selected()
    
    # Click default radio and verify mutual exclusivity
    radio_default.click()
    assert not radio_checked.is_selected()
    assert radio_default.is_selected()
    
    # Click checked radio and verify mutual exclusivity
    radio_checked.click()
    assert radio_checked.is_selected()
    assert not radio_default.is_selected()
    
    print("✅ Radio button group test passed")


def test_dropdown_select(driver):
    dropdown = Select(driver.find_element(By.NAME, "my-select"))
    
    # Test selecting by visible text
    dropdown.select_by_visible_text("Two")
    selected_option = dropdown.first_selected_option
    assert selected_option.text == "Two"
    
    # Test selecting by value
    dropdown.select_by_value("3")
    selected_option = dropdown.first_selected_option
    assert selected_option.get_attribute("value") == "3"
    
    print("✅ Dropdown (select) test passed")


def test_dropdown_datalist(driver):
    datalist_input = driver.find_element(By.NAME, "my-datalist")
    test_value = "San Francisco"
    
    datalist_input.clear()
    datalist_input.send_keys(test_value)
    
    assert datalist_input.get_attribute("value") == test_value
    print(f"✅ Dropdown (datalist) test passed: '{test_value}'")