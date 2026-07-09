import pytest
import allure
from utils.api_helper import APIHelper
from configs.config import AUTH_PAYLOAD

@allure.feature("Authentication")
class TestAuth:

    @allure.story("Get Token")
    @allure.title("TC001 - Get token with valid credentials")
    def test_get_token_valid(self):
        api = APIHelper()
        response = api.get_token(AUTH_PAYLOAD)

        assert response.status_code == 200
        assert "token" in response.json()

    @allure.story("Get Token")
    @allure.title("TC002 - Get token with invalid credentials")
    def test_get_token_invalid(self):
        api = APIHelper()
        response = api.get_token({
            "username": "wronguser",
            "password": "wrongpass"
        })

        assert response.status_code == 200
        assert response.json()["reason"] == "Bad credentials"