'''
6. Использование функций в функциях:

Создайте две функции: `square` для вычисления квадрата числа и `cube` для вычисления куба числа. Затем напишите функцию `calculate_result`, которая принимает число и возвращает сумму квадрата и куба этого числа. Попробуйте функцию с различными числами.
'''


def square(sum_square):
    return sum_square * sum_square


print(square(5))


def cube(sum_cube):
    return square(sum_cube) * sum_cube


print(cube(5))


def calculate_result(number):
    return square(number) + cube(number)


print(calculate_result(2))
print(calculate_result(3))
