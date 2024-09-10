from playwright.sync_api import Page, expect


def test_first1(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    username = page.get_by_role('textbox', name='username')
    username.fill('Jambo')
    password = page.get_by_role('textbox', name='password')
    password.fill('123abc')
    login = page.get_by_role('button', name='login')
    login.click()
