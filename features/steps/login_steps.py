# Imported all the required modules
from behave import given, when, then
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from pages.login_page import LoginPage

@given("I launch the browser and open the zen login page")
def step_impl(context):
# Setups the browser for testing    
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.guvi.in/sign-in/")
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver)
    
    

@when("I enter valid email  and password")
def step_impl(context):
# Enters the valid login credentials    
    context.login_page.enter_user_email("**********.com")
    context.login_page.enter_password("*************")
    

@when("I enter invalid email and password")
def step_impl(context):
# Entered wrong credentials to test the login  failure    
    context.login_page.enter_user_email("invalid@email.com")
    context.login_page.enter_password("invalidpass")

@when("I click on the login button")
def step_impl(context):
# Clicks the login button on guvi    
    context.login_page.click_login()
    time.sleep(2)

@then("I should be logged in successfully")
def step_impl(context):
# Validating the login functionality    
    assert "mycourses" 


@then("I sign out from the portal")
def step_impl(context):
# Signing out from the  website    
    context.login_page.signout()
    time.sleep(5)

@then("I should see an error message")
def step_impl(context):
# Validating the sign out button    
    assert "Incorrect Email or Password" 

@then("Email and password fields should be visible")
def step_impl(context):
# Validating the  email and password buttons that are visible on the screen   
    assert context.login_page.find_element((By.ID, "email")).is_displayed()
    assert context.login_page.find_element((By.ID, "password")).is_displayed()

@then("Login button should be enabled")
def step_impl(context):
# Lastly validating the login button    
    assert context.login_page.find_element((By.ID, "login-btn")).is_enabled()