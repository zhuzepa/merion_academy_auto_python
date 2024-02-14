"""
5. Список объектов:

Во втором уроке вы создавали классы `Mailing` и `Address`. Создайте объектов  `Mailing` (несколько почтовый отправлений). Про каждое отправление распечатайте информацию в формате: Отправление <track> из <город>, <улица>, <дом>-<квартира> в <город>, <улица>, <дом>-<квартира>. Стоимость <стоимость> рублей.
"""

from classes.address import Mailing, Address


add_to = Address("125252", "Moscow", "Зорге", "k25", "77")
add_from = Address("125167", "Moscow", "Ленинградский проспект", "36", "1")

cost = 3223  # стоимость
track = "TR777"

print(
    f"Отправление {track} из {add_to.city}, {add_to.street},"
    f" {add_to.home}-{add_to.apartament} в {add_from.city}, {add_from.street},"
    f" {add_from.home}-{add_from.apartament}. Стоимость {cost} рублей."
)

add_to1 = Address("140016", "Moscov", "Барыкина", "4", "88")
add_from2 = Address("199034", "Санкт-Петербург", "Биржевой переулок", "4", "0123")

cost1 = 7894
track1 = "TR6789"

print(
    f"Отправление {track1} из {add_to1.city}, {add_to1.street},"
    f" {add_to1.home}-{add_to1.apartament} в {add_from2.city}, {add_from2.street},"
    f" {add_from2.home}-{add_from2.apartament}. Стоимость {cost1} рублей."
)

cost2 = 15464
track2 = "TR99999"
add_to2 = Address("123424", "Талин", "Самсунговна", "334", "68")
add_from2 = Address("533343", "Краснодар", "Ахо переулок", "6", "158")

request = Mailing(add_to2, add_from2, cost2, track2)
response = Mailing(add_to2, add_from2, cost2, track2)

print(
    f"Отправление {request.track} из {request.addres_to.city},"
    f" {request.addres_to.street},"
    f" {request.addres_to.home}-{request.addres_to.apartament} в"
    f" {response.addres_from.city}, {response.addres_from.street},"
    f" {response.addres_from.home}-{response.addres_from.apartament}. Стоимость"
    f" {response.cost} рублей."
)

address1 = Address("140091", "Москва", "Северный проезд", "2", "нет квартиры")
address2 = Address("143026", "д.Скольково", "Новая", "100", "нет квартиры")
address3 = Address("428000", "Чебоксары", "Президенский бульвар", "10", "1")
address4 = Address("428032", "Чебоксары", "Дзержинского", "19", "100")

mail_1 = Mailing(address1, address2, 9000, "TR03243")
mail_2 = Mailing(address3, address4, 3141, "TR044444")

mailing = [mail_1, mail_2]

for mail in mailing:
    print(
        f"Отправление {mail.track} из {mail.addres_to.city},"
        f" {mail.addres_to.street},"
        f" {mail.addres_to.home}-{mail.addres_to.apartament} в"
        f" {mail.addres_from.city}, {mail.addres_from.street},"
        f" {mail.addres_from.home}-{mail.addres_from.apartament}. Стоимость"
        f" {mail.cost} рублей."
    )
