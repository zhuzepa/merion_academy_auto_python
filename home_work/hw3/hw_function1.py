'''
1. Определение функций:

Напишите функцию `calculate_area`, которая принимает радиус круга в качестве аргумента и возвращает его площадь. После этого вызовите функцию с радиусами 5, 8 и 10 и выведите результат.
'''

import math


def calculate_area(circle_radius):
    return math.pi * circle_radius ** 2


print(calculate_area(5))
print(calculate_area(8))
print(calculate_area(10))
