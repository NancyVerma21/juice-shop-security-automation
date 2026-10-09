import re

from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#loginButton")

    def _close_overlays(self):
        welcome_button = self.page.get_by_role(
            "button",
            name="Close Welcome Banner"
        )

        cookie_button = self.page.get_by_role(
            "button",
            name=re.compile("dismiss cookie message", re.IGNORECASE)
        )

        try:
            welcome_button.click(timeout=3000)
        except Exception:
            pass

        try:
            cookie_button.click(timeout=3000)
        except Exception:
            pass

    def open(self, base_url: str):
        self.page.goto(
            f"{base_url}/#/login",
            wait_until="domcontentloaded"
        )

        self._close_overlays()

        self.email_input.wait_for(
            state="visible",
            timeout=15000
        )

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_login_page(self):
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.login_button).to_be_visible()
