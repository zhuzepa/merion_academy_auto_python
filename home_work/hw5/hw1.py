"""
1. Простые условия:

Напишите программу, которая запрашивает у пользователя число и выводит сообщение "Число четное", если оно четное, и "Число нечетное" в противном случае.
"""

name_number = int(input("Name number please: "))

# if name_number % 2 == 0:
#     print("Это четное число", name_number)
# else:
#     print("Это нечетное число", name_number)


def chet_ne_chet(x):
    return x % 2 == 0


if chet_ne_chet(name_number):
    print("Это четное число", name_number)
else:
    print("Это нечетное число", name_number)
