import requests


class Employee:
    def __init__(self, login, password):
        self.URL = 'https://x-clients-be.onrender.com/employee'
        self.AUTH_URL = 'https://x-clients-be.onrender.com/auth/login'
        self.login = login
        self.password = password
        self.token = ''

    def get_token(self) -> str:
        if self.token != '':
            return self.token

        body_params = {
            "username": self.login,
            "password": self.password
        }
        r = requests.post(self.AUTH_URL, json=body_params)
        self.token = r.json().get('userToken')
        return self.token

    def get_list_employees(self, company_id: int) -> list[dict]:
        query_params = {'company': company_id}
        r = requests.get(self.URL, params=query_params)
        return r.json()[0]['id']

    def get_employee(self, id: int) -> dict:
        r = requests.get(f'{self.URL}/{id}')
        return r.json()

    def add_new_employee(self, first_name: str, last_name: str, company_id: int, phone: str) -> int:
        body_params = {

            "firstName": first_name,
            "lastName": last_name,
            "companyId": company_id,
            "phone": phone

        }

        headers = {'x-client-token': self.get_token()}
        r = requests.post(self.URL, json=body_params, headers=headers)
        return r.json().get('id')

    def change_employee_info(self, id: int, last_name: str, email: str, phone: str, isactive: bool, url: str):
        headers = {'x-client-token': self.get_token()}
        body_params = {

            "email": email,
            "lastName": last_name,
            "isActive": isactive,
            "phone": phone,
            'url': url

        }
        r = requests.patch(f'{self.URL}/{id}', headers=headers, json=body_params)
        return r.json()
