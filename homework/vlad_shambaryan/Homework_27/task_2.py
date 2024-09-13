from playwright.sync_api import Page


def test_new_tab_button(page: Page):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    with page.context.expect_page() as new_page_info:
        page.click('text=Click')
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    assert "I am a new page in a new tab" in new_page.inner_text('body')
    page.bring_to_front()
    assert page.is_enabled('text=Click')
