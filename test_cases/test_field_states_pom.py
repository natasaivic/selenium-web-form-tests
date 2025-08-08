from page_objects.locators import WebFormLocators


def test_disabled_input_pom(web_form_page):
    is_enabled, placeholder, interaction_blocked = web_form_page.test_disabled_field(WebFormLocators.DISABLED_INPUT)
    
    # Verify field is disabled
    assert not is_enabled
    
    # Verify placeholder text is present
    assert placeholder == "Disabled input"
    
    # Verify interaction is blocked
    assert interaction_blocked
    
    print("✅ Disabled input POM test passed")


def test_readonly_input_pom(web_form_page):
    is_enabled, readonly_attr, initial_value, clear_blocked, sendkeys_blocked = web_form_page.test_readonly_field(WebFormLocators.READONLY_INPUT)
    
    # Verify field is enabled but readonly
    assert is_enabled
    
    # Verify readonly attribute
    assert readonly_attr is not None
    
    # Verify initial value
    assert initial_value == "Readonly input"
    
    # Verify operations are blocked
    if clear_blocked:
        print("✅ Readonly input correctly prevents clear() operation")
    else:
        print("⚠️  Readonly input unexpectedly allowed clear() operation")
    
    if sendkeys_blocked:
        print("✅ Readonly input correctly prevents send_keys() operation")
    else:
        print("⚠️  Readonly input unexpectedly allowed send_keys() operation")
    
    print("✅ Readonly input POM test passed")