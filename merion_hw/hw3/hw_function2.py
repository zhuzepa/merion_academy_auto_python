'''
2. Возвращаемые значения:

Создайте функцию `is_even`, которая принимает целое число и возвращает `True`, если число четное, и `False` в противном случае. Протестируйте функцию на нескольких числах.
'''


def is_even(num):
    if num % 2 == 0:
        print('True')
    else:
        print('False')


is_even(3)


def is_even1(num):
    return num % 2 == 0


print(is_even1(4))
