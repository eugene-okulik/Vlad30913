from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(5)
    yield chrome_driver


def test_product(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    item = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "(//a[@class='product-item-link'])[1]")
    ))
    item_name = item.find_element(By.XPATH, "(//a[@class='product-item-link'])").text
    actions = ActionChains(driver)
    actions.move_to_element(item)
    add_to_compare_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "(//a[@class='action tocompare'])"))
    )
    actions.move_to_element(add_to_compare_btn).click().perform()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "(//div[@class='block block-compare'])"))
    )
    added_item = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "(//strong[@class='product-item-name'])"))
    ).text
    assert added_item in item_name
