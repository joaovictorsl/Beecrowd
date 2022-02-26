def start():
    p1 = [float(x) for x in input().split(' ')]
    p2 = [float(x) for x in input().split(' ')]
    print("VALOR A PAGAR: R$ {:.2f}".format(p1[1]*p1[2]+p2[1]*p2[2]))


start()