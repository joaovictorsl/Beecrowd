# -*- coding: utf-8 -*-

import math

one = input().split(' ')
two = input().split(' ')

x1 = float(one[0])
y1 = float(one[1])
x2 = float(two[0])
y2 = float(two[1])

print("{:.4f}".format(math.sqrt((x2-x1)**2+(y2-y1)**2)))