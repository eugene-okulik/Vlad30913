from playwright.sync_api import Page, expect


def test_confirm_alert(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.on("dialog", lambda dialog: dialog.accept())
    button = page.locator("//a[@class='a-button']")
    button.click()
    verification = page.locator("//div[contains(@id,'result')]")
    expect(verification).to_be_visible()
    verification_text = verification.inner_text().strip().replace('\n', ' ').replace('  ', ' ')
    assert verification_text == "You selected Ok"
