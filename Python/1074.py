n = int(input())

for i in range(n):
    num = int(input())
    if num == 0:
        print("NULL")
    else:
        x = "EVEN" if num % 2 == 0 else "ODD"
        y = "POSITIVE" if num > 0 else "NEGATIVE"
        print("{} {}".format(x, y))