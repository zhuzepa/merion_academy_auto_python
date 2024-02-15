'''
6. Проверка равенства строк:

Запросите у пользователя ввод строки. Если введенная строка равна "Python", выведите "Это Python!", в противном случае "Это не Python!".
'''

machine_language = input('Enter programming language: ')


def language(x):
    if x.capitalize() == 'Python':
        print('Это Python!')
    else:
        print('Это не Python!')


language(machine_language)
