# pip install requests

from employee_service import EmployeeService
import pytest


@pytest.fixture
def service():
    return EmployeeService("leyla", "water-fairy")


def test_emp_create(service: EmployeeService):
    company_id = 2981
    emp_first_name = "Sam"
    emp_last_name = "Smith"
    emp_phone = "+7345654324"

    # получить список сотрудников
    list_before = service.get_employees_for(company_id)  # X

    # добавить нового
    new_emp_id = service.create(emp_first_name, emp_last_name, company_id, emp_phone)
    # проверить, что на шаге 2 пришел id нового сотрудника
    assert new_emp_id > 0

    # получить список сотрудников снова
    list_after = service.get_employees_for(company_id)  # X+1
    # проверить, что список стал больше
    assert len(list_before) == len(list_after) - 1

    # запросить сотрудника по id
    emp_info = service.get_employee_by_id(new_emp_id)
    # проверить данные у сотрудника
    assert emp_info["id"] == new_emp_id
    assert emp_info["firstName"] == emp_first_name
    assert emp_info["lastName"] == emp_last_name
    assert emp_info["middleName"] == None
    assert emp_info["companyId"] == company_id
    assert emp_info["email"] == None
    assert emp_info["avatar_url"] == None
    assert emp_info["phone"] == emp_phone
    assert emp_info["birthdate"] == None
    assert emp_info["isActive"] == True


def test_emp_is_employee_list(service: EmployeeService):
    company_id = 2981
    emp_first_name = "Sam"
    emp_last_name = "Smith"
    emp_phone = "+7345654324"

    # создать сотрудника для компании
    new_emp_id = service.create(emp_first_name, emp_last_name, company_id, emp_phone)

    # запросить сотрудников для компании
    emp_list = service.get_employees_for(company_id)  # [ {}, {"id": new_emp_id}, {}]

    # проверить, что сотрудник отображается в списке компаний
    counter = 0

    for emp in emp_list:
        if emp["id"] == new_emp_id:
            counter += 1

    assert counter == 1


def test_i_can_change_emp_status(service: EmployeeService):
    company_id = 2981
    emp_first_name = "Sam"
    emp_last_name = "Smith"
    emp_phone = "+7345654324"

    # создать сотрудника для компании
    new_emp_id = service.create(emp_first_name, emp_last_name, company_id, emp_phone)

    # поменять статус
    service.update(new_emp_id, is_active=False)

    # запросить сотрудника по id
    emp_info = service.get_employee_by_id(new_emp_id)

    # проверить, что is_active == False
    assert emp_info["isActive"] == False


def test_i_cannot_create_emp_for_non_exist_company(service: EmployeeService):
    company_id = 999999
    emp_first_name = "Sam"
    emp_last_name = "Smith"
    emp_phone = "+7345654324"

    # получить список сотрудников
    list_before = service.get_employees_for(company_id)

    # добавить нового
    new_emp_id = service.create(emp_first_name, emp_last_name, company_id, emp_phone)
    assert new_emp_id == None

    # получить список сотрудников снова
    list_after = service.get_employees_for(company_id)

    # проверить, что список остался тот же
    assert list_before == list_after