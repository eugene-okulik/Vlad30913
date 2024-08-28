from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_Choose(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    choose_language = driver.find_element(By.CLASS_NAME, 'form-select')
    result = driver.find_element(By.XPATH, '//*[@id="id_choose_language"]/option[2]')
    result_text = result.text
    selector = Select(choose_language)
    selector.select_by_value("1")
    selected_option = selector.first_selected_option
    assert selected_option.text == result_text
    print(selected_option.text)
