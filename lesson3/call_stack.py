x = 1
def funca():
    y = 2
    print("Начали делать A")
    funcb()
    print("Закончили делать A")


def funcb():
    print("Начали делать B")
    funcc()
    print("Закончили делать B")


def funcc():
    print("Начали делать C")
    funcd()
    print("Закончили делать C")


def funcd():
    print("Сделали D")


print("Начали программу")
funca()
print("Закончили программу")
