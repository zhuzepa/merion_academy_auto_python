'''
17. Заполнение списка:

Используя цикл `for`, создайте список, содержащий квадраты чисел от 1 до 5. Выведите полученный список.
'''

list_number = []
for i in range(1, 6):
    list_n = [i * 2]
    list_number += list_n

print(list_number)

lst = []
for x in range(1, 6):
    lst.append(x ** 2)
print(lst)
