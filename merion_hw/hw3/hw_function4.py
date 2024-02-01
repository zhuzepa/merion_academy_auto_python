'''
3. Аргументы по умолчанию:

Напишите функцию `greet_user`, которая принимает имя пользователя и выводит приветствие. Установите значение "Гость" по умолчанию. Вызовите функцию без передачи аргумента и с передачей имени пользователя.
'''


def great_user(purchase_amount, discount):
    discount_ammount = purchase_amount - purchase_amount * discount / 100
    return discount_ammount


print(great_user(30000, 5))
