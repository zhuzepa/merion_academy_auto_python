# import pytest
# import requests
#
# base_url = "https://x-clients-be.onrender.com"
#
#
# @pytest.fixture  # получаем токен и передаем его в тестах
# def get_token() -> str:
#     body_params = {"username": "leyla", "password": "water-fairy"}
#     response = requests.post(base_url + "/auth/login", json=body_params)
#     return response.json().get("userToken")
