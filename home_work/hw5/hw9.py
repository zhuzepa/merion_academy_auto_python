'''
9. Проверка длины строки:

Запросите у пользователя ввод строки. Если длина строки больше 10 символов, выведите "Длина строки больше 10 символов", иначе "Длина строки 10 символов или меньше".
'''

enter_string = input('Enter string: ')

def len_string(str):
    if len(str) > 10:
        print(f'Длина строки больше 10 символов -- {str}')
    else:
        print(f'Длина строки 10 символов или меньше -- {str}')

len_string(enter_string)