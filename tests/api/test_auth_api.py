import allure
import pytest

from api.client import ApiClient


@pytest.mark.api
@pytest.mark.security
@allure.feature("Authentication API")
@allure.story("Invalid Credentials")
@allure.title("Reject login with invalid credentials")
def test_login_rejects_invalid_credentials(base_url):
    client = ApiClient(base_url)

    try:
        response = client.request(
            "POST",
            "/rest/user/login",
            json={
                "email": "invalid-user@example.com",
                "password": "WrongPassword123!"
            }
        )

        assert response.status_code == 401, (
            f"Expected HTTP 401, received {response.status_code}. "
            f"Response: {response.text[:300]}"
        )

        assert "Invalid email or password" in response.text

    finally:
        client.close()


@pytest.mark.api
@pytest.mark.security
@allure.feature("Authorization API")
@allure.story("Unauthenticated Access")
@allure.title("Reject private basket access without authentication")
def test_private_basket_requires_authentication(base_url):
    client = ApiClient(base_url)

    try:
        response = client.request(
            "GET",
            "/rest/basket/1"
        )

        assert response.status_code == 401, (
            f"Expected HTTP 401 for an unauthenticated request, "
            f"received {response.status_code}. "
            f"Response: {response.text[:300]}"
        )

    finally:
        client.close()
