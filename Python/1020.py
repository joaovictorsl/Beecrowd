# -*- coding: utf-8 -*-
import math
age_in_days = int(input())
years = math.floor(age_in_days/365)
age_in_days -= years*365
months = math.floor(age_in_days/30)
age_in_days -= months*30
print("{:.0f} ano(s)\n{:.0f} mes(es)\n{} dia(s)".format(
    years, months, age_in_days))