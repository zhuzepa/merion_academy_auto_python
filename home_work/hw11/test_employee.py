import pytest
import requests
from employee import EmployeeService

base_url = "https://x-clients-be.onrender.com"


def test_emp_create(get_token):
    employee = EmployeeService()
    employee.company_id()
    id_user= employee.creating_company_employee(get_token, '8909999999', "Заебатов", "Бабулат")
    employee.get_list_of_employees()
    employee.change_data_employee(get_token, id_user, True, 'pethov@pethov.ii', '8999999999')
    employee.ban_creating_company_employee(get_token, '23242', 'Бан', 'Банов', 123)
