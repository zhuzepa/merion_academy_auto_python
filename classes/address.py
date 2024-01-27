class Address:
    def __init__(self, zip_code, city, street, home, apartment):
        self.index = zip_code
        self.city = city
        self.street = street
        self.home = home
        self.apartament = apartment


class Mailing:
    def __init__(self, addres_to, addres_from, cost, track):
        self.addres_to = addres_to
        self.addres_from = addres_from
        self.cost = cost
        self.track = track
