'''
4. Циклы и списки:

Создайте список чисел от 1 до 10. Используйте цикл `for` для вывода квадратов каждого числа в списке..
'''
numbers_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for x in range(0, len(numbers_list)):
    current_num = numbers_list[x]
    print(current_num, current_num ** 2)

numbers_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for x in numbers_list:
    print(x, x ** 2)

