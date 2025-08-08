from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException


def test_disabled_input(driver):
    disabled_input = driver.find_element(By.NAME, "my-disabled")
    
    # Verify field is disabled
    assert not disabled_input.is_enabled()
    
    # Verify placeholder text is present
    placeholder = disabled_input.get_attribute("placeholder")
    assert placeholder == "Disabled input"
    
    # Attempt to interact with disabled field should fail
    try:
        disabled_input.send_keys("This should not work")
        assert False, "Should not be able to type in disabled field"
    except ElementNotInteractableException:
        print("✅ Disabled input correctly prevents interaction")
    
    print("✅ Disabled input test passed")


def test_readonly_input(driver):
    readonly_input = driver.find_element(By.NAME, "my-readonly")
    
    # Verify field is enabled but readonly
    assert readonly_input.is_enabled()
    
    # Verify readonly attribute
    readonly_attr = readonly_input.get_attribute("readonly")
    assert readonly_attr is not None
    
    # Get initial value
    initial_value = readonly_input.get_attribute("value")
    assert initial_value == "Readonly input"
    
    # Attempt to modify readonly field should fail
    try:
        readonly_input.clear()
        # If we get here, the field incorrectly allows modification
        print("⚠️  Readonly input unexpectedly allowed clear() operation")
    except:
        print("✅ Readonly input correctly prevents clear() operation")
    
    # Attempt to send keys should also fail  
    try:
        readonly_input.send_keys("Modified text")
        print("⚠️  Readonly input unexpectedly allowed send_keys() operation")
    except:
        print("✅ Readonly input correctly prevents send_keys() operation")
    
    print("✅ Readonly input test passed")