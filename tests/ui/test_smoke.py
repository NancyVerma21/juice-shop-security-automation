import allure
import pytest

from pages.home_page import HomePage


@pytest.mark.ui
@pytest.mark.smoke
@allure.feature("UI")
@allure.story("Application Smoke Test")
@allure.title("Verify Juice Shop homepage loads successfully")
def test_juice_shop_homepage(page, base_url):
    home_page = HomePage(page)

    home_page.open(base_url)
    home_page.verify_loaded()
