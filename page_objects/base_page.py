from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class BasePage:
    """Base page class with common functionality for all page objects"""
    
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
    
    def find_element(self, locator):
        """Find element using locator tuple"""
        return self.driver.find_element(*locator)
    
    def get_attribute(self, locator, attribute):
        """Get attribute value from element"""
        element = self.find_element(locator)
        return element.get_attribute(attribute)
    
    def execute_script(self, script, *args):
        """Execute JavaScript on the page"""
        return self.driver.execute_script(script, *args)
    
    def is_selected(self, locator):
        """Check if checkbox or radio button is selected"""
        element = self.find_element(locator)
        return element.is_selected()
    
    def get_select(self, locator):
        """Get Select object for dropdown"""
        element = self.find_element(locator)
        return Select(element)
    
    def is_enabled(self, locator):
        """Check if element is enabled"""
        element = self.find_element(locator)
        return element.is_enabled()