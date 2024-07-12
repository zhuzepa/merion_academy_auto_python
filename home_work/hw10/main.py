from employee import Employee

empl = Employee('leyla', 'water-fairy')
# получаем список сотрудников компании
r = empl.get_list_employees(14732)
print(r)

# добавляем нового сотрудника
id_add = (empl.add_new_employee('Шакал', 'чур', 14732, '9999'))
print(id_add)

# получаем нового сотрудника по id
emp = empl.get_employee(r(14732))
print(emp)

# изменяем информацию о сотруднике
upd = empl.change_employee_info(id_add, 'Принц', 'ppp@mail.ru', '939328', False,
                                'https://x-clients-be.onrender.com/docs/#/')
print(upd)
