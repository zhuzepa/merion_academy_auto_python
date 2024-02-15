'''
12. Условия с or:

Запросите у пользователя ввод числа. Проверьте, является ли число четным или кратным 5. Выведите соответствующее сообщение.
'''

number_input = int(input('Enter number: '))


def devision_by(num):
    if num % 2 == 0 or num % 5 == 0:
        if num % 2 == 0:
            print('число четное')
        elif num % 5 == 0:
            print('кратное 5')
    else:
        print('число НЕчетное и НЕ кратное 5')


devision_by(number_input)
