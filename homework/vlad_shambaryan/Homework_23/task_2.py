from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_id_name(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    f_name = driver.find_element(By.ID, 'firstName')
    f_name.send_keys('Donald')
    l_name = driver.find_element(By.ID, 'lastName')
    l_name.send_keys('Tramp')

    email = driver.find_element(By.ID, 'userEmail')
    email.send_keys('123abc@gmail.com')

    driver.execute_script("window.scrollBy(0, 700);")
    gender = driver.find_element(By.XPATH, "//label[contains(.,'Female')]")
    gender.click()

    mobile_num = driver.find_element(By.ID, 'userNumber')
    mobile_num.send_keys('1453699877')

    date = driver.find_element(By.ID, 'dateOfBirthInput')
    date.click()
    year = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
    selector = Select(year)
    selector.select_by_value("1979")
    month = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
    selector = Select(month)
    selector.select_by_value("5")
    day = driver.find_element(By.XPATH, "//div[contains(@class,'day--022')]")
    day.click()

    subjects = driver.find_element(By.ID, 'subjectsInput')
    subjects.send_keys('English')
    subjects.send_keys(Keys.ENTER)

    hobbies = (driver.find_element(By.XPATH, "//label[contains(.,'Sports')]"))
    hobbies.click(),
    hobbies = driver.find_element(By.XPATH, "//label[contains(.,'Music')]")
    hobbies.click()

    current_address = driver.find_element(By.ID, 'currentAddress')
    current_address.send_keys(' Donald Tramp 11 Southgate Blvd C25 N11467,\
    New Castle Delaware 19720 USA +1 302 4148567')

    driver.find_element(By.XPATH, "(//div[contains(.,'Select State')])[12]").click()
    state = driver.find_element(By.ID, 'react-select-3-option-0')
    state.click()

    driver.find_element(By.XPATH, "(//div[contains(.,'Select City')])[11]").click()
    city = driver.find_element(By.ID, 'react-select-4-option-1')
    city.click()
    submit = driver.find_element(By.ID, 'submit')
    submit.click()

    table_info = driver.find_element(By.XPATH, "//div[@class='modal-body']")
    print(table_info.text)
