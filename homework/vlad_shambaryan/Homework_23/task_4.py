from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()

def test_Choose(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start = driver.find_element(By.XPATH,"//button[contains(.,'Start')]")
    start.click()
    WebDriverWait(driver, 7).until(EC.presence_of_all_elements_located
                                   ((By.XPATH, "//h4[contains(.,'Hello World!')]")))
    finish = driver.find_element(By.XPATH, "//h4[contains(.,'Hello World!')]")
    assert finish.text == 'Hello World!'
    print(finish.text)
