import allure
import pytest

from api.client import ApiClient


@pytest.mark.api
@pytest.mark.security
@allure.feature("Security Regression")
@allure.story("Input Validation")
@allure.title("Handle HTML-like input in product search")
def test_search_handles_html_like_input(base_url):
    client = ApiClient(base_url)

    try:
        response = client.request(
            "GET",
            "/rest/products/search",
            params={"q": "<script>alert(1)</script>"}
        )

        assert response.status_code == 200

        payload = response.json()

        assert payload.get("status") == "success"
        assert isinstance(payload.get("data"), list)

    finally:
        client.close()


@pytest.mark.api
@pytest.mark.security
@allure.feature("Security Regression")
@allure.story("Input Validation")
@allure.title("Handle long search input without a server error")
def test_search_handles_long_input(base_url):
    client = ApiClient(base_url)

    try:
        response = client.request(
            "GET",
            "/rest/products/search",
            params={"q": "A" * 512}
        )

        assert response.status_code == 200

        payload = response.json()

        assert payload.get("status") == "success"
        assert isinstance(payload.get("data"), list)

    finally:
        client.close()
