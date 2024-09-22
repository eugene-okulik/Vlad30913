from Test_UI_pw.pages.locators import eco_friendly_locator as ecoloc
from Test_UI_pw.pages.base_page import BasePage
from playwright.sync_api import expect
import re


class EcoFriendly(BasePage):

    friendly_page_url = 'collections/eco-friendly.html'

    def sort_by_price_and_check_correct_sort(self, text):
        first_man = self.find(ecoloc.products_loc).locator('nth=0')
        print(first_man.inner_text())
        self.find(ecoloc.sorted_loc).locator('nth=0').select_option('Price')
        expect(self.page).to_have_url(re.compile(text))
        print(first_man.inner_text())

    def enter_search_text(self, text):
        search_box = self.find(ecoloc.search_box_loc)
        search_box.fill(text)
        search_box.press('Enter')

    def check_search_functionality(self, text):
        expect(self.find(ecoloc.search_results_loc)).to_have_text(text)

    def filter_products_by_price(self):
        self.page.wait_for_selector(ecoloc.price_filter_loc)
        price_filter = self.page.query_selector(ecoloc.price_filter_loc)
        price_filter.click()
        self.page.wait_for_selector(ecoloc.price_range_loc)
        price_range = self.page.query_selector(ecoloc.price_range_loc)
        price_range.click()

    def check_filter_products_by_price(self, text):
        expect(self.find(ecoloc.filtered_loc)).to_have_text(text)

    def check_product_count(self, count: int):
        products = self.find(ecoloc.products_loc)
        expect(products).to_have_count(count)
