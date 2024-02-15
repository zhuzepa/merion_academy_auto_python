"""
6. Изменение элементов списка:

Создайте список целых чисел. Используйте цикл `for` для увеличения каждого элемента на 2. Выведите обновленный список.
"""
# numbers_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# new_numbers_list = []
# for number in numbers_list:
#     numbers_list = number * 2
#     new_numbers_list.append(numbers_list)
#
# print(new_numbers_list)


numbers_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for x in range(0, len(numbers_list)):
    numbers_list[x] = numbers_list[x] + 2
print(numbers_list)
