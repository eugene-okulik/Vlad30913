from playwright.sync_api import expect
from Test_UI_pw.pages.locators import product_locators as prod
from Test_UI_pw.pages.base_page import BasePage


class AnaRunningShort(BasePage):

    ana_running_short_url = 'ana-running-short.html'

    def check_product_name(self, text):
        expect(self.page.locator(prod.product_name_loc)).to_have_text(text)

    def check_product_price(self, text):
        expect(self.page.locator(prod.product_price_loc)).to_have_text(text)

    def check_product_size(self, text):
        self.find(prod.available_sizes_loc).wait_for(state='visible')
        expect(self.page.locator(prod.available_sizes_loc)).to_have_text(text)

    def check_product_color(self, text):
        self.find(prod.available_sizes_loc).wait_for(state='visible')
        expect(self.page.locator(prod.available_colors_loc)).to_have_text(text)

    def add_to_compare(self):
        compare = self.find(prod.compare_loc)
        self.find(prod.compare_loc).wait_for(state='visible')
        self.page.evaluate("window.scrollBy(0, 300);")
        compare.click()

    def check_compare_list(self, text):
        self.find(prod.comparision_list_loc).wait_for(state='visible')
        expect(self.page.locator(prod.comparision_list_loc)).to_have_text(text)

    def add_product_to_cart(self):
        size = self.find(prod.size_loc)
        size.click()
        color = self.find(prod.color_loc)
        color.click()
        add_cart = self.find(prod.add_to_cart_loc)
        add_cart.click()

    def check_count(self, text):
        count = self.find(prod.count_loc)
        count.click()
        self.find(prod.count_loc).wait_for(state='visible')
        expect(self.page.locator(prod.count_loc)).to_have_text(text)

    def check_product_in_cart(self, text):
        self.find(prod.item_in_cart_loc).wait_for(state='visible')
        expect(self.page.locator(prod.item_in_cart_loc)).to_have_text(text)

    def check_add_to_cart_with_out_selected_size_color(self, text):
        add_cart = self.find(prod.add_to_cart_loc)
        add_cart.click()
        expect(self.page.locator(prod.color_error_loc)).to_have_text(text)
        expect(self.page.locator(prod.size_error_loc)).to_have_text(text)
