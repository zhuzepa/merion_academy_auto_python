import requests
import pytest


class EmployeeService:
    def __init__(self):
        self.URL = "https://x-clients-be.onrender.com"

    def company_id(self):  # получение ид компании и возвращает его при вызове функции
        query_params = {"active": "True"}
        r = requests.get(self.URL + "/company", params=query_params)
        # print(r.json()[0]["id"])
        return r.json()[0]["id"]

    def creating_company_employee(
            self, get_token, phone: str, firstName: str, lastName: str
    ):  # создание юзера в компании
        body_params = {
            "phone": phone,
            "firstName": firstName,
            "companyId": self.company_id(),
            "lastName": lastName,
        }
        headers = {"x-client-token": get_token}
        r = requests.post(self.URL + "/employee", headers=headers, json=body_params)
        print(r.json()['id'])
        return r.json()['id']

    def ban_creating_company_employee(
            self, get_token, phone: str, firstName: str, lastName: str,
            company_id: int):  # запрет создание юзера в компании с неправильным id company
        body_params = {
            "phone": phone,
            "firstName": firstName,
            "companyId": company_id,
            "lastName": lastName,
        }
        headers = {"x-client-token": get_token}
        r = requests.post(self.URL + "/employee", headers=headers, json=body_params)
        assert r.status_code == 500

    def get_list_of_employees(self):  # получение списка пользователей и проверка, что в ней есть созданный юзер
        query_params = {'company': self.company_id()}
        r = requests.get(self.URL + "/employee", params=query_params)
        print(r.status_code)
        print(r.json()[-1]['firstName'])
        assert r.json()[-1]['firstName'] == "Заебатов"

    def change_data_employee(self, get_token, id, status, email=None, phone=None):  # изменение данных юзера
        id = id
        headers = {
            'x-client-token': get_token
        }
        body_params = {
            'isActive': status,
            'email': email,
            'phone': phone
        }
        r = requests.patch(f'{self.URL}/employee/{id}', headers=headers, json=body_params)
        print(r.status_code)
        print(r.json())
