import allure
import pytest

from api.client import ApiClient


@pytest.mark.api
@allure.feature("API Testing")
@allure.story("Product Search")
@allure.title("Verify product search API returns matching products")
def test_product_search_returns_matching_products(base_url):
    client = ApiClient(base_url)

    try:
        response = client.request(
            "GET",
            "/rest/products/search",
            params={"q": "Apple"}
        )

        assert response.status_code == 200

        payload = response.json()

        assert payload.get("status") == "success"
        assert isinstance(payload.get("data"), list)
        assert len(payload["data"]) > 0

        assert any(
            "apple" in str(product.get("name", "")).lower()
            for product in payload["data"]
        )
    finally:
        client.close()


@pytest.mark.api
@allure.feature("API Testing")
@allure.story("Negative Search")
@allure.title("Verify search handles a nonexistent product")
def test_product_search_with_no_matching_product(base_url):
    client = ApiClient(base_url)

    try:
        response = client.request(
            "GET",
            "/rest/products/search",
            params={"q": "no-such-product-qa-987654"}
        )

        assert response.status_code == 200

        payload = response.json()

        assert payload.get("status") == "success"
        assert isinstance(payload.get("data"), list)
        assert payload["data"] == []
    finally:
        client.close()
