def test_color_picker_pom(web_form_page):
    test_color = "#ff5733"
    
    actual_color = web_form_page.set_color_picker(test_color)
    
    assert actual_color == test_color
    print(f"✅ Color picker POM test passed: {test_color}")


def test_date_picker_pom(web_form_page):
    test_date = "2024-12-25"
    
    actual_date = web_form_page.set_date_picker(test_date)
    
    assert actual_date == test_date
    print(f"✅ Date picker POM test passed: {test_date}")


def test_range_slider_pom(web_form_page):
    initial_value, new_value = web_form_page.move_range_slider(50)
    
    assert new_value != initial_value
    print(f"✅ Range slider POM test passed: {initial_value} → {new_value}")


def test_file_upload_pom(web_form_page):
    test_content = "This is a POM test file for upload"
    test_filename = "pom_test_upload.txt"
    
    uploaded_filename = web_form_page.upload_file(test_content, test_filename)
    
    assert test_filename in uploaded_filename
    print(f"✅ File upload POM test passed: {uploaded_filename}")