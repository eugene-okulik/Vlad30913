from playwright.sync_api import Page


def test_color_change_button(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    page.evaluate("window.scrollBy(0, 300);")
    color_button = page.locator("#colorChange")
    page.wait_for_function(
        "element => getComputedStyle(element).color === 'rgb(220, 53, 69)'", arg=color_button.element_handle())
    color_button.click()
