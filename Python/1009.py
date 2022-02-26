# -*- coding: utf-8 -*-

name = input()
salary = input()
sold = input()

bonus = (15/100)*float(sold)

final_salary = float(salary) + bonus

print("TOTAL = R$ {:.2f}".format(final_salary))