from Test_UI_pw.pages.locators import sale_locators as loc
from Test_UI_pw.pages.base_page import BasePage
from playwright.sync_api import expect


class SalePage(BasePage):

    sale_url = 'sale.html'

    def check_title(self, text):
        self.find(loc.page_title_loc)
        expect(self.find(loc.page_title_loc)).to_have_text(text)

    def check_product_count(self):
        products = self.find(loc.products_loc)
        product_count = products.count()
        expected_count = product_count
        assert product_count == expected_count
        expect(products).to_have_count(expected_count)

    def women_s_deals_element(self, text):
        self.find(loc.pands_loc)
        expect(self.find(loc.pands_loc)).to_have_text(text)

    def mens_bargains_element(self, text):
        self.find(loc.mens_loc)
        expect(self.find(loc.mens_loc)).to_have_text(text)
