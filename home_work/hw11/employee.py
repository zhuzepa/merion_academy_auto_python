import requests
import pytest


class EmployeeService:
    def __init__(self):
        self.URL = "https://x-clients-be.onrender.com"

    def company_id(self):  # получение ид компании и возвращает его при вызове функции
        query_params = {"active": "True"}
        r = requests.get(self.URL + "/company", params=query_params)
        #print(r.json()[0]["id"])
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
        #print(r.json()['id'])
        return r.json()['id']

    def get_list_of_employees(self):
        body_params = {'company': self.company_id()}
        r = requests.get(self.URL + "/employee", params=body_params)
        print(r.status_code)
        print(r.json()[-1]['firstName'])
        assert r.json()[-1]['firstName'] == "Заебатов"
