def is_odd(n):
    r = n % 2
    result = r == 0
    return result


num = int(input('Enter a number: '))

if is_odd(num):
    print('Четное число', num)
else:
    print('Нечетное число', num)
