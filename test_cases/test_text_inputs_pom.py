def test_text_input_pom(web_form_page):
    test_text = "Test Text Input POM"
    
    actual_value = web_form_page.fill_text_input(test_text)
    
    assert actual_value == test_text
    print(f"✅ Text input POM test passed: '{test_text}'")


def test_password_input_pom(web_form_page):
    test_password = "SecurePassword123POM"
    
    actual_value = web_form_page.fill_password_input(test_password)
    
    assert actual_value == test_password
    print("✅ Password input POM test passed")


def test_textarea_input_pom(web_form_page):
    test_text = "This is a POM test message in the textarea field.\nMultiple lines are supported."
    
    actual_value = web_form_page.fill_textarea_input(test_text)
    
    assert actual_value == test_text
    print("✅ Textarea input POM test passed")