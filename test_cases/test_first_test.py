from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_web_form_submission_first_test():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        driver.maximize_window()
        
        print(f"Page title: {driver.title}")
        print(f"Current URL: {driver.current_url}")
        
        driver.implicitly_wait(5)
        
        text_box = driver.find_element(By.NAME, "my-text")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button")
        
        text_box.clear()
        text_box.send_keys("Selenium WebDriver Test")
        print("Text entered successfully")
        
        time.sleep(1)
        submit_button.click()
        print("Form submitted")
        
        time.sleep(2)
        message = driver.find_element(By.ID, "message")
        success_text = message.text
        print(f"Success message: {success_text}")
        
        if "Received!" in success_text:
            print("✅ Test passed: Form submission successful")
        else:
            print("❌ Test failed: Unexpected message")
            
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        
    finally:
        driver.quit()
        print("Browser closed")
