n = [int(x) for x in input().split(' ')]
highest = 0
for i, num in enumerate(n):
    if i == 0:
        highest = num
    else:
        highest = num if highest < num else highest
print("{} eh o maior".format(highest))