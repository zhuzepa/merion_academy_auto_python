'''
16. Таблица умножения:

Используя вложенный цикл `for`, создайте таблицу умножения от 1 до 5. Выведите результат в виде строки таблицы.
'''

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} * {j} = {i*j}', end='\t')
#     print()

for i in range(1, 6):
    for j in range(1, 6):
        print(f'{i} * {j} = {i*j}', end='\t')
    print()