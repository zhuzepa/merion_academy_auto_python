nums = [2, 5, 2342, 3, 757, 9, 42, 73, 6]
val = input('Which numbers to print: ')


def print_if_even(x):
    if x % 2 == 0:
        print('Это четное число', x)


def print_if_odd(x):
    if x % 2 == 1:
        print('Это нечетное число', x)


if val.startswith('чет'):
    for num in nums:
        print_if_even(num)
elif val.startswith('нечет'):
    for num in nums:
        print_if_odd(num)
else:
    print('команда не распоздана')



