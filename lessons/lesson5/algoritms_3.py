from classes.player import Player
from random import Random

players = []

rand = Random()

for x in range(1, 101):
    player = Player('Playes ' + str(x))
    xp_to_add = rand.randint(500, 1500)
    player.upgrade(xp_to_add)
    players.append(player)

list_to_invite = []
looseers_list = []

for player in players:
    if player.xp >= 1000:
        list_to_invite.append(player)
    else:
        looseers_list.append(player)

for inv in list_to_invite:
    print(inv.get_info())
print('====')

for looser in looseers_list:
    print(looser.get_info())