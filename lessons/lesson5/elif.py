status = input('Enter your status: ')


def check_status(status_to_be):
    return status == status_to_be


if check_status('ok'):
    print('платеж принят')
elif check_status('error'):
    print('ошибка платежа')
elif check_status('wait'):
    print('ожидает платежа')
else:
    print('неизвестный статус')
