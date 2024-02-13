'''
6. Изменение элементов списка:

Создайте список целых чисел. Используйте цикл `for` для увеличения каждого элемента на 2. Выведите обновленный список.
'''
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers_list = []
for number in numbers_list:
    numbers_list = number * 2
    new_numbers_list.append(numbers_list)

print(new_numbers_list)

