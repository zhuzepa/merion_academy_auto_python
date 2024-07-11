# pip install requests

from employee_service import EmployeeService

service = EmployeeService("leyla","water-fairy")

# Получить список сотрудников для компании
res = service.get_employees_for(2756)
print(res) 

# Добавить нового сотрудника
new_emp = service.create("Adam", "Smith", 2756, "+79076567324")
print(new_emp)

# Получить сотрудника по id
emp = service.get_employee_by_id(new_emp)
print(emp)

# Изменить информацию о сотруднике
upd = service.update(1356, email="adam@mail.ru")
print(upd)