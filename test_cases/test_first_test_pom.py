from page_objects.locators import WebFormLocators
import time


def test_web_form_submission_first_test_pom(web_form_page):
    driver = web_form_page.driver
    
    print(f"Page title: {driver.title}")
    print(f"Current URL: {driver.current_url}")
    
    # Fill text input
    web_form_page.fill_text_input("Selenium WebDriver Test")
    print("Text entered successfully")
    
    # Submit form
    time.sleep(1)
    submit_button = web_form_page.find_element(WebFormLocators.SUBMIT_BUTTON)
    submit_button.click()
    print("Form submitted")
    
    # Verify success message
    time.sleep(2)
    success_message = web_form_page.find_element(WebFormLocators.SUCCESS_MESSAGE)
    success_text = success_message.text
    print(f"Success message: {success_text}")
    
    if "Received!" in success_text:
        print("✅ Test passed: Form submission successful")
    else:
        print("❌ Test failed: Unexpected message")
        
    assert "Received!" in success_text