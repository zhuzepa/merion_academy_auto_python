import requests


class EmployeeService():

    def __init__(self, login, password) -> None:
        self.URL = 'https://x-clients-be.onrender.com/employee'
        self.AUTH_URL = 'https://x-clients-be.onrender.com/auth/login'
        self.login = login
        self.password = password
        self.token = ""      

    def get_employees_for(self, company_id: int) -> list[dict]:
        query_params  = {'company': company_id}
        response = requests.get(self.URL, params=query_params)
        return response.json()
        
    def get_employee_by_id(self, emp_id: int) -> dict:
        response = requests.get(f"{self.URL}/{emp_id}")
        return response.json()


    def create(self, first_name: str, last_name: str, company_id: int, phone: str) -> int:
        body = {
            "firstName": first_name,
            "lastName": last_name,
            "companyId": company_id,
            "phone": phone
        }

        my_headers = {
            "x-client-token": self.get_token()
        }

        response = requests.post(self.URL, json=body, headers=my_headers)
        return response.json().get("id")
    
    def set_email(self, emp_id, email):
        body = {"email": email}
        my_headers = {
            "x-client-token": self.get_token()
        }
        response = requests.patch(f"{self.URL}/{emp_id}", json=body, headers=my_headers)
        return response.json()

    def update(self, emp_id: int, last_name: str = None, is_active: bool = None, email: str = None, phone: str = None, url: str = None):
        my_headers = {
            "x-client-token": self.get_token()
        }
        
        body = {}
        
        if last_name != None:
            body["lastName"] = last_name
        
        if is_active != None:
            body["isActive"] = is_active
            
        if email != None:
            body["email"] = email
            
        if url != None:
            body["url"] = url
            
        if phone != None:
            body["phone"] = phone
        
        response = requests.patch(f"{self.URL}/{emp_id}", json=body, headers=my_headers)
        return response.json()
                
        
        
        
        
        
        
        
        
        
        
        

    def get_token(self) -> str:
        if self.token != "":
            return self.token
        
        body = {
            "username": self.login,
            "password": self.password
        }
        response = requests.post(self.AUTH_URL, json=body)
        self.token = response.json().get("userToken")
        
        return self.token
