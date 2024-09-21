from playwright.sync_api import Page
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None
    sale_url = None
    friendly_page_url = None
    login_page_url = None
    account_create_page_url = None
    ana_running_short_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto(f'{self.base_url}/{self.page_url}')

    def open_friendly_page(self):
        self.page.goto(f'{self.base_url}/{self.friendly_page_url}')

    def open_sale_page(self):
        self.page.goto(f'{self.base_url}/{self.sale_url}')

    def open_account_page(self):
        self.page.goto(f'{self.base_url}/{self.account_create_page_url}')

    def open_login_page(self):
        self.page.goto(f'{self.base_url}/{self.login_page_url}')

    def open_ana_running_short_page(self):
        self.page.goto(f'{self.base_url}/{self.ana_running_short_url}')

    @allure.step('Find elements by locator')
    def find(self, locator):
        return self.page.locator(locator)
