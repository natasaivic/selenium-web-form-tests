from page_objects.locators import WebFormLocators


def get_radio_states(web_form_page):
    """Helper function to get both radio button states"""
    return web_form_page.get_radio_states(
        WebFormLocators.RADIO_CHECKED, WebFormLocators.RADIO_DEFAULT
    )


def test_checkbox_checked_pom(web_form_page):
    # Toggle (uncheck) and verify initial and new states
    initial_state, new_state = web_form_page.toggle_checkbox(WebFormLocators.CHECKBOX_CHECKED)
    assert initial_state  # Was initially checked
    assert not new_state
    
    # Toggle (check) again and verify
    _, final_state = web_form_page.toggle_checkbox(WebFormLocators.CHECKBOX_CHECKED)
    assert final_state
    
    print("✅ Checked checkbox POM test passed")


def test_checkbox_default_pom(web_form_page):
    # Toggle (check) and verify initial and new states
    initial_state, new_state = web_form_page.toggle_checkbox(WebFormLocators.CHECKBOX_DEFAULT)
    assert not initial_state  # Was initially unchecked
    assert new_state
    
    # Toggle (uncheck) again and verify
    _, final_state = web_form_page.toggle_checkbox(WebFormLocators.CHECKBOX_DEFAULT)
    assert not final_state
    
    print("✅ Default checkbox POM test passed")


def test_radio_button_group_pom(web_form_page):
    # Verify initial states
    checked_state, default_state = get_radio_states(web_form_page)
    assert checked_state and not default_state
    
    # Click default radio and verify mutual exclusivity
    web_form_page.click_radio_button(WebFormLocators.RADIO_DEFAULT)
    checked_state, default_state = get_radio_states(web_form_page)
    assert not checked_state and default_state
    
    # Click checked radio and verify mutual exclusivity
    web_form_page.click_radio_button(WebFormLocators.RADIO_CHECKED)
    checked_state, default_state = get_radio_states(web_form_page)
    assert checked_state and not default_state
    
    print("✅ Radio button group POM test passed")


def test_dropdown_select_pom(web_form_page):
    # Test selecting by visible text
    selected_text = web_form_page.select_dropdown_by_text(WebFormLocators.DROPDOWN_SELECT, "Two")
    assert selected_text == "Two"
    
    # Test selecting by value
    selected_value = web_form_page.select_dropdown_by_value(WebFormLocators.DROPDOWN_SELECT, "3")
    assert selected_value == "3"
    
    print("✅ Dropdown (select) POM test passed")


def test_dropdown_datalist_pom(web_form_page):
    test_value = "San Francisco"
    
    actual_value = web_form_page.fill_datalist(WebFormLocators.DROPDOWN_DATALIST, test_value)
    
    assert actual_value == test_value
    print(f"✅ Dropdown (datalist) POM test passed: '{test_value}'")