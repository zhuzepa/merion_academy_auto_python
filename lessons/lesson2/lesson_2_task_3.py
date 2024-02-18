from classes.address import Mailing, Address

add_to = Address('103123', "Москва", 'Ленина', '105', '1 каб')
add_from = Address('103123', "Москва", 'Ленина', '105', '2 каб')

cost = 10
track = 'TR001'

request = Mailing(add_to, add_from, cost, track)
response = Mailing(add_to, add_from, cost, track)

print(
    f'Отправление {request.track} из {request.addres_to.city}, {request.addres_to.street}, {request.addres_to.home}-{request.addres_to.apartament} в {response.addres_from.city}, {response.addres_from.street}, {response.addres_from.home}-{response.addres_from.apartament}. Стоимость {cost} рублей.')
