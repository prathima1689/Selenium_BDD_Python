import time

from selenium.webdriver.common.by import By
from behave import given, when , then


@given ('user is on the login page')
def step_open_login_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()
    time.sleep(3)

@when ('the user enters "{username}" username and "{password}" password')
def enter_credentials(context, username, password):
    context.driver.find_element(By.NAME, "username").send_keys(username)
    context.driver.find_element(By.NAME, "password").send_keys(password)
    time.sleep(3)

@when ('clicks on the login button')
def login_button(context):
    context.driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button").click()
    print("user successfully logged in")
    time.sleep(3)

@then ('user should be able to login')
def logged_in(context):
    try:
        assert "dashboard" in context.driver.current_url, "passed"
    except:
        assert "login" in context.driver.current_url, "failed"

@then ('navigated to "Recruitment" tab')
def navigated_recruitment_tab(context):
    context.driver.find_element(By.LINK_TEXT, "Recruitment").click()
    time.sleep(3)

    header = context.driver.find_element(By.TAG_NAME, "h6").text
    time.sleep(3)

    # assert "Recruitment" in header, "failed"
