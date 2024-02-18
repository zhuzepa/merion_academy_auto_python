list_numbers = [2, 5, 2342, 3, 757, 9, 42, 73, 6]


def summ_number(x):
    if x % 2 == 0:
        print('Это четное число', x)
    else:
        print('Это нечетное число', x)


for list_number in list_numbers:
    summ_number(list_number)
