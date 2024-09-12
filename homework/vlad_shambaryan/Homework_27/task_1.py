from playwright.sync_api import Page, expect


def test_confirm_alert8(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.on("dialog", lambda dialog: dialog.accept())
    button = page.locator("//a[@class='a-button']")
    button.click()
    confirmation = page.locator("//div[contains(@id,'result')]")
    expect(confirmation).to_be_visible()
    confirmation_text = confirmation.inner_text().strip().replace('\n', ' ').replace('  ', ' ')
    assert confirmation_text == "You selected Ok"
