'''
11. Условия с in:

Создайте программу, которая проверяет, принадлежит ли введенное пользователем число к диапазону от 1 до 100. Выведите соответствующее сообщение.
'''

num_input = int(input('Enter number: '))


def numbers(num_input):
    if num_input in range(1, 101):
        print(f'Число {num_input} в диапозоне от 1 до 100')
    else:
        print(f'Число {num_input} вне диапозона')


numbers(num_input)
