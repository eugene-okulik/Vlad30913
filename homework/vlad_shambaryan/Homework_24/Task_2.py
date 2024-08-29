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
    chrome_driver.maximize_window()
    yield chrome_driver


def test_Products(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    item_name = driver.find_element(By.XPATH, "(//a[@class='product-item-link'])[1]").text
    item = driver.find_element(By.XPATH, "//img[@alt='Push It Messenger Bag']")
    add_compare = driver.find_element(By.XPATH, "(//a[contains(.,'Add to Compare')])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(item)
    actions.click(add_compare)
    actions.perform()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='block block-compare']")))
    added_item = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "(//strong[@class='product-item-name'])"))).text
    assert added_item in item_name
