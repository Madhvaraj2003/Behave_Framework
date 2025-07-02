# Imported all the required modules
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Created a class called LoginPage
class LoginPage(BasePage):
# Locators for login and logout functionality    
    USER_EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-btn")
    SIGN_OUT_ICON = (By.CSS_SELECTOR,"img#dropdown_contents.avatar_banner")
    SIGNOUT_BUTTON = (By.XPATH, "//div[text()='Sign Out']")

    def enter_user_email(self, useremail):
# Fills the email input         
        self.enter_text(self.USER_EMAIL_INPUT, useremail)

# Fills the password
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
# Clicks on the login button        
        self.click(self.LOGIN_BUTTON)

    def signout(self):
# First it clicks on profile icon and then clicks on signout button        
        self.click(self.SIGN_OUT_ICON)
        self.click(self.SIGNOUT_BUTTON)

# Verifying login functionality
    def is_login_successful(self):
        return "dashboard" in self.driver.current_url.lower()