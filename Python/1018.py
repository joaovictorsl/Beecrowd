num = int(input())
print(num)
hundred = divmod(num/100, 1)
num -= hundred[0]*100
fifty = divmod(num/50, 1)
num -= fifty[0]*50
twenty = divmod(num/20, 1)
num -= twenty[0]*20
ten = divmod(num/10, 1)
num -= ten[0]*10
five = divmod(num/5, 1)
num -= five[0]*5
two = divmod(num/2, 1)
num -= two[0]*2
one = divmod(num/1, 1)
num -= one[0]*1
print(
    "{:.0f} nota(s) de R$ 100,00\n{:.0f} nota(s) de R$ 50,00\n{:.0f} nota(s) de R$ 20,00\n{:.0f} nota(s) de R$ 10,00\n{:.0f} nota(s) de R$ 5,00\n{:.0f} nota(s) de R$ 2,00\n{:.0f} nota(s) de R$ 1,00"
    .format(hundred[0], fifty[0], twenty[0], ten[0], five[0], two[0], one[0]))