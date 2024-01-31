def do_smth(n):
    print('start' + str(n))
    do_smth(n + 1)
    print('finish' + str(n))
do_smth(0)