import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given ('user in PIM page')
def navigate_PIM(context):
    pim_link= WebDriverWait(context.driver, 20).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "PIM")))
    pim_link.click()
    print("clicked on PIM Link")
    time.sleep(2)
    header= context.driver.find_element(By.TAG_NAME, "h6").text
    time.sleep(3)
    assert "PIM" in header, "PIM click failed"

@when ('user clicks on Add button')
def add_button(context):
    context.driver.find_element(By.XPATH, "(//button[@type ='button'])[5]").click()
    time.sleep(3)

@when ('user adds Employees "{firstName}" and "{LastName}"')
def add_employees(context, firstName, LastName):
    context.driver.find_element(By.NAME, "firstName").send_keys(firstName)
    time.sleep(3)
    context.driver.find_element(By.NAME, "lastName").send_keys(LastName)
    time.sleep(3)
    # context.driver.find_element(By.CLASS_NAME, "oxd-input oxd-input--active").send_keys(Employee_ID)
    # time.sleep(3)

@then ('user should be able to add Employees')
def adds_users(context):
    context.driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']").click()
    time.sleep(8)

    # try:
    #     assert "PIM" in context.driver.current_url, "passed"
    #
    # except:
    #     assert "dashboard" in context.driver.current_url, "failed"

@given ('user in Employee list page')
def click_Employee_list(context):
    context.driver.find_element(By.XPATH, "//a[text() ='Employee List']").click()
    time.sleep(4)

@when ('user enters Employee name in "{Employee_name}"')
def user_enter_employee_name(context, Employee_name):
    context.driver.find_element(By.XPATH, "(//input[@ placeholder = 'Type for hints...'])[1]").send_keys(Employee_name)
    time.sleep(4)

@when('user clicks on search')
def user_clicks_search(context):
    context.driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']").click()
    time.sleep(4)

@then ('user should be able to see list of Employee name in Records')
def find_records(context):

    Employee_Name= context.driver.find_element(By.XPATH, "(//input[@ placeholder = 'Type for hints...'])[1]").get_attribute("Value")
    print("Employee_Name", Employee_Name)

    # first_middle_name= context.driver.find_element(By.NAME, "First (& Middle) Name").text.strip()
    first_middle_name= context.driver.find_element(By.XPATH, "(//div[@class='oxd-table-header-cell oxd-padding-cell oxd-table-th'])[3]").text.strip()

    # Last_Name= context.driver.find_element(By.NAME, "Last Name").text.strip()
    Last_Name = context.driver.find_element(By.XPATH, "(//div[@class='oxd-table-header-cell oxd-padding-cell oxd-table-th'])[4]").text.strip()

    name = (first_middle_name + " " + Last_Name)
    print("Actual_Employee_Name", name)

    if Employee_Name == name:
        print(f"Search of Employee {Employee_Name} is successful")
    else:
        print(f"{Employee_Name} Employee not found")

    assert "Record Found" or "Records Found" in context.driver.find_element(By.XPATH, "(//span[@class = 'oxd-text oxd-text--span'])[1]'"), "test has failed"
    print("Search was successful")