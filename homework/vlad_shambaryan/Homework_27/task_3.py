from playwright.sync_api import Page, expect


def test_color_change_button(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    red_color_button = page.locator("//button[contains(@class,'mt-4 text-danger btn btn-primary')]")
    red_color_button.click()
    expect(red_color_button).to_have_css("color", "rgb(220, 53, 69)")
