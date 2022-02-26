def turn_positive(x):
    if x < 0:
        return x * -1
    else:
        return x


def check_if_triangle(a, b, c):
    if not turn_positive(b-c) < a < b+c:
        print("Area = {:.1f}".format((a+b)*c/2))
        return
    if not turn_positive(a-c) < b < a+c:
        print("Area = {:.1f}".format((a+b)*c/2))
        return
    if not turn_positive(a-b) < c < a+b:
        print("Area = {:.1f}".format((a+b)*c/2))
        return
    print("Perimetro = {:.1f}".format(a+b+c))


values = [float(x) for x in input().split(' ')]
check_if_triangle(*values)