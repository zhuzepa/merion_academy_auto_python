"""
8. Список товаров в заказе:

Создайте класс `Order` (заказ). В заказе должны быть поля `customer_name` (имя клиента) и `items` (список товаров). Создайте экземпляр класса `Order`, укажите имя клиента и наполните список несколькими товарами (строковый тип данных). Выведите на экран информацию о товаре в виде  Заказ для <order.customer_name>: <список товаров>.
"""


class Order:
    def __init__(self, customer_name, items):
        self.customer_name = customer_name
        self.items = items

    def info_order(self):
        return print(
            f"Меня зовут {self.customer_name} и сегодня я купил {items_list[:-2]}"
        )


goods = Order("Скриптонит", ["ганжу", "канабис", "дудка"])
items_list = ""
for item in goods.items:
    items_list += item + ", "

goods.info_order()


# class Order:
#     def __init__(self, customer_name, items):
#         self.customer_name = customer_name
#         self.items = items
#
#     def info_order(self):
#         items_list = ", ".join(self.items)
#         return print(f"Меня зовут {self.customer_name} и сегодня я купил {items_list}")
#
#
# goods = Order("Скриптонит", ["ганжу", "канабис", "дудка"])
# goods.info_order()
# goods = Order("Мияги", "микрофон")
# goods.info_order()
# goods = Order("Тимати", "Bently")
# goods.info_order()
