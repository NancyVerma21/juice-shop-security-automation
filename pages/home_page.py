from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.all_products = page.get_by_text("All Products", exact=True)

    def open(self, base_url: str):
        self.page.goto(base_url)

    def verify_loaded(self):
        expect(self.page).to_have_title("OWASP Juice Shop")
        expect(self.all_products).to_be_visible()
