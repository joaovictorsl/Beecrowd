def start():
    a = float(input())
    b = float(input())
    c = float(input())
    if a > 10 or b > 10 or c > 10:
        return False
    if a < 0 or b < 0 or c < 0:
        return False
    print("MEDIA = {:.1f}".format((2*a+3*b+5*c)/10))


start()