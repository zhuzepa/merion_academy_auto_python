'''
10. Условия с elif:

  Попросите пользователя ввести оценку от 1 до 5. Выведите соответствующий комментарий: "Отлично" (5), "Хорошо" (4), "Удовлетворительно" (3), "Неудовлетворительно" (1-2).
'''
estimation = int(input('What is your rating? '))


def raiting(raiting):
    if raiting == 5:
        print(f'Отлично ({raiting})')
    elif raiting == 4:
        print(f'Хорошо ({raiting})')
    elif raiting == 3:
        print(f'Удовлетворительно ({raiting})')
    elif raiting == 1 or raiting == 2:
        print(f'Неудовлетворительно ({raiting})')
    else:
        print('Incorrect input')


raiting(estimation)
