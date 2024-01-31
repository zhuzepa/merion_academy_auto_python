from classes.player import Player

player1 = Player("Ёрик")
print(player1.nickname)
player1.upgrade(10)
player1.upgrade(10)
player1.upgrade()
print(player1.xp)
print(player1.get_info())
