# -*- coding: utf-8 -*-

array = input().split(' ')

a = float(array[0])
b = float(array[1])
c = float(array[2])
pi = 3.14159

triangle = a * c / 2
circle = pi * c ** 2
trapezium = (a + b) * c / 2
square = b ** 2
rectangle = a * b

print(
    "TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}"
    .format(triangle, circle, trapezium, square, rectangle)
)
