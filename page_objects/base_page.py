class BasePage:
    """Base page class with common functionality for all page objects"""
    
    def __init__(self, driver):
        self.driver = driver
    
    def find_element(self, locator):
        """Find element using locator tuple"""
        return self.driver.find_element(*locator)
    
    def get_attribute(self, locator, attribute):
        """Get attribute value from element"""
        element = self.find_element(locator)
        return element.get_attribute(attribute)