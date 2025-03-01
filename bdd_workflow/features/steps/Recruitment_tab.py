import time

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given ('click on the "Candidates" section')
def click_candidates(context):
    context.driver.find_element(By.LINK_TEXT, "Candidates").click()
    time.sleep(3)

@when ('click on the "Add" button')
def add_candidates(context):
    context.driver.find_element(By.XPATH, "//button[@class = 'oxd-button oxd-button--medium oxd-button--secondary']").click()
    time.sleep(4)


@when ('enter the candidate "{firstName}" firstName')
def enter_firstname(context, firstName):
    context.driver.find_element(By.NAME, "firstName").send_keys(firstName)
    time.sleep(3)


@when ('enter the candidate "{lastName}" lastName')
def enter_lastname(context, lastName):
    context.driver.find_element(By.NAME, "lastName").send_keys(lastName)
    time.sleep(3)

@when ('enter the candidate "{email}"')
def enter_email(context, email):
    context.driver.find_element(By.XPATH, "(//input [@placeholder = 'Type here'])[1]").send_keys(email)
    time.sleep(3)

@when ('select a job "{vacancy}"')
def select_vacancy(context,vacancy):
    dropdown = context.driver.find_element(By.XPATH, "//i[@class= 'oxd-icon bi-caret-down-fill oxd-select-text--arrow']")
    dropdown.click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, f"//span[contains(text(), '{vacancy}')]").click()
    time.sleep(6)
    print(f"Selected '{vacancy}'")
    time.sleep(2)
#

    # Try with action class and pautogui

@when ('upload the candidate resume')
def upload_resume(context):
    pdf_file_path = r"C:\Prathima\Automation\Test_files\NewMicrosoftExcelWorksheet.pdf"
    upload = WebDriverWait(context.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    upload.send_keys(pdf_file_path)
    time.sleep(3)

    WebDriverWait(context.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[contains (text(), 'NewMicrosoftExcelWorksheet.pdf')]")))
    print("File uploaded successfully")

    # pyautogui.write(pdf_file_path)
    # time.sleep(2)
    # pyautogui.press('enter')
    # time.sleep(5)

@when ('click on the "Save" button')
def save_all(context):
    context.driver.find_element(By.XPATH, "//button[@type ='submit']").click()
    time.sleep(4)

@then ('should see a success message "Successfully Saved"')
def message_save(context):
    assert "Status: Application Initiated" in context.driver.find_element(By.NAME,"Status: Application Initiated"), "passed"

@given('I am on the "Candidates" section')
def candidate_page(context):
    time.sleep(3)
    context.driver.find_element(By.LINK_TEXT, "Candidates").click()
    time.sleep(3)

@when('I enter the candidate name "{CandidateName}" in the search field')
def candidate_name(context, CandidateName):
   Search_candidate_name = WebDriverWait(context.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@placeholder ='Type for hints...']")))
   Search_candidate_name.send_keys(CandidateName)

   WebDriverWait(context.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class ='oxd-autocomplete-option']//*[contains(text(), 'John  Doe')]"))).click()
   time.sleep(4)

   print("Found Candidate")


@when('I click on the "Search" button')
def search(context):
    context.driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']").click()
    time.sleep(4)

    print("Search Completed")


# @then('I should see "{CandidateName}" listed in the search results')
# def record_found(context, CandidateName):
#    assert "John  Doe" in context.driver.find_element(By.NAME, CandidateName), "passed"
