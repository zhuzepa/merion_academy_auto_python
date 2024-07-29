import pytest
import requests
from employee import EmployeeService

base_url = "https://x-clients-be.onrender.com"


def test_emp_create(get_token):
    employee = EmployeeService()
    employee.company_id()
    employee.creating_company_employee(get_token, '8909999999', "Заебатов", "Бабулат")
    employee.get_list_of_employees()


# employee.creating_company_employee(employee.company_id)
