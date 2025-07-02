# Imported all the required modules 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
# Storing webdriver for the reuse        
        self.driver = driver


    def find_element(self, locator, timeout=10):
# Used wait method for element to appear on screen         
        return WebDriverWait(self.driver,  timeout).until(EC.presence_of_element_located(locator))
        

    def click(self, locator):
# Clicks an element        
        self.find_element(locator).click()

    def enter_text(self, locator, text):
# Clear's input box and enters new text        
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)        

