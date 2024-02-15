'''
5. Выбор действия:

Создайте программу, которая предлагает пользователю выбрать операцию: сложение или вычитание. Затем запрашивайте два числа и выполняйте выбранную операцию.
'''

operation = input("Select an action ' + ' or ' - ': ")
one, two = map(int, input('Enter two numbers: ').split())


def mat(one, two):
    if operation == '+':
        print(f'Сумма {one + two}')
    elif operation == '-':
        print(f'Сумма {one - two}')
    else:
        print('Incorrect input', operation)


mat(one, two)
