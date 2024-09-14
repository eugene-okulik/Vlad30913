import re
import json
from playwright.sync_api import Page, expect, Route
from time import sleep


def test_header_replacement(page: Page):

    title = "яблокоффон 16 про"

    def title_route(route: Route):
        server_response = route.fetch()
        body = server_response.json()
        print("Original response:", body)
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = title
        body = json.dumps(body)
        route.fulfill(
            response=server_response,
            body=body,
            headers={"content-type": "application/json"})
    page.route(re.compile('library/step0_iphone/digitalmat'), title_route)
    page.goto("https://www.apple.com/shop/buy-iphone")
    iphone = page.locator("(//h3[@class='rf-hcard-content-title'])[1]")
    iphone.click()
    new_title = page.locator("(//h2[@id='rf-digitalmat-overlay-label-0'])[1]")
    expect(new_title).to_have_text(title)
