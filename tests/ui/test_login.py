import allure
import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.security
@allure.feature("Authentication")
@allure.story("Login")
@allure.title("Verify login page is accessible")
def test_login_page_loads(page, base_url):
    login_page = LoginPage(page)

    login_page.open(base_url)
    login_page.verify_login_page()


@pytest.mark.ui
@pytest.mark.security
@allure.feature("Authentication")
@allure.story("Invalid Login")
@allure.title("Verify invalid credentials are rejected")
def test_invalid_login(page, base_url):
    login_page = LoginPage(page)

    login_page.open(base_url)

    login_page.login(
        "invalid-user@example.com",
        "InvalidPassword123!"
    )

    expect(page).to_have_url(
        f"{base_url}/#/login"
    )
