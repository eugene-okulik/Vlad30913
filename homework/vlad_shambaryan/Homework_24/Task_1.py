from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(2)
    chrome_driver.maximize_window()
    yield chrome_driver


def test_new_tabs(driver):
    driver.get('https://www.demoblaze.com/index.html')
    el_nexus = driver.find_element(By.XPATH, "//a[contains(.,'Nexus 6')]")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.click(el_nexus)
    actions.key_up(Keys.CONTROL)
    actions.perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_cart = driver.find_element(By.CSS_SELECTOR, '.btn-success')
    add_to_cart.click()
    WebDriverWait(driver, 7).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    cart = driver.find_element(By.ID, 'cartur')
    cart.click()
    in_cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//td[contains(.,'Nexus 6')]")))
    assert in_cart.text == 'Nexus 6'
