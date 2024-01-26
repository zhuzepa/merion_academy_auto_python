from classes.car_class import Car
from classes.price_car_class import PriceCar

car1 = Car()
car1.model = "Kia"
car1.year = 2023
car1.run = 10
car1.engine = "электро"
car1.carcase = "пластик"
car2 = PriceCar()
car2.price = 2000000
car2.promocode = 100000


print(
    f"У меня машина {car1.model}, {car1.year} года с пробегом {car1.year} км с"
    f" {car1.engine} двигателем и корпус {car1.carcase}, машина стоит {car2.price} и на"
    f" неё действует скидка {car2.promocode}"
)


car2 = Car()
car2.model = "Bmw"
car2.year = 2022
car2.run = 100
car2.engine = "бензин"
car2.carcase = "карбон"

print(
    f"У меня машина {car2.model}, {car2.year} года с пробегом {car2.year} км с"
    f" {car2.engine} двигателем и корпус {car2.carcase}"
)

car3 = Car()
car3.model = "Audi"
car3.year = 2017
car3.run = 25000
car3.engine = "дизель"
car3.carcase = "универсал"

print(
    f"У меня машина {car3.model}, {car3.year} года с пробегом {car3.year} км с"
    f" {car3.engine} двигателем и корпус {car3.carcase}"
)
