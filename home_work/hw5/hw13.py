'''
13. Условия с and:

Попросите пользователя ввести два числа. Проверьте, является ли одно число положительным, а другое - четным. Выведите соответствующее сообщение.
'''

one, two = map(int, input().split())

if one > 0 and two % 2 == 0:
    print('one number is positive and the other is even')
else:
    print('Incorrect input')
