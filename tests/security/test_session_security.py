import allure
import pytest

from api.client import ApiClient


@pytest.mark.api
@pytest.mark.security
@allure.feature("Session Security")
@allure.story("Token Validation")
@allure.title("Reject a malformed bearer token")
def test_rejects_malformed_bearer_token(base_url):
    client = ApiClient(base_url)

    try:
        response = client.request(
            "GET",
            "/rest/basket/1",
            headers={
                "Authorization": "Bearer this-is-not-a-valid-token"
            }
        )

        assert response.status_code == 401, (
            f"Expected HTTP 401, received {response.status_code}. "
            f"Response: {response.text[:300]}"
        )
    finally:
        client.close()


@pytest.mark.api
@pytest.mark.security
@allure.feature("Session Security")
@allure.story("Token Validation")
@allure.title("Reject an unsupported authorization scheme")
def test_rejects_unsupported_authorization_scheme(base_url):
    client = ApiClient(base_url)

    try:
        response = client.request(
            "GET",
            "/rest/basket/1",
            headers={
                "Authorization": "Basic dGVzdDp0ZXN0"
            }
        )

        assert response.status_code == 401, (
            f"Expected HTTP 401, received {response.status_code}. "
            f"Response: {response.text[:300]}"
        )
    finally:
        client.close()
