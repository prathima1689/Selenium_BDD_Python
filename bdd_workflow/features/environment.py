import time

from selenium import webdriver


def before_all(context):
    context. driver = webdriver.Chrome()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()
    time.sleep(3)

def after_all(context):
    context.driver.quit()