input_age = int(input('Enter your age: '))

# 3 %
# 5 %
# 15 %

if input_age < 12:
    print('Вы еше малы для скидки')
elif 12 <= input_age <= 18:
    print('Вам от 12 до 18 и ваша скидка 3% ')
elif 19 <= input_age <= 65:
    print('Вам от 19 до 65 и ваша скидка 5% ')
else:
    print('Вам от 65 и ваша скидка 15% ')