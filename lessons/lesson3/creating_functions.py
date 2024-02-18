def say_message(name, age, language):
    print(f'Привет! Меня зовут {name}')
    print(f'В следующем году мне будет {age + 1}')
    print(f'Я изучаю {language}')


say_message('Ашот', 20, 'JS')


def double_num():
    num = input('Введите число: ')
    my_number = int(num)
    print(my_number * 2)
    print(type(my_number))


double_num()
