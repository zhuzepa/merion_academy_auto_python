from random import Random

participants = []

s = []
m = []
l = []
xl = []

for x in range(1, 101):
    weight = Random().randint(60, 130)
    participants.append(weight)


def sort(weights):
    for weight in weights:
        if weight < 80:
            s.append(weight)
        elif weight < 100:
            m.append(weight)
        elif weight < 120:
            l.append(weight)
        else:
            xl.append(weight)


sort(participants)
print("finish")
