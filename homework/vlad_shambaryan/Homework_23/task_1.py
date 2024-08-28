from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_input(driver):
    input_data = 'abc123password'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys('abc123password')
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == input_data
    print(result_text.text)
