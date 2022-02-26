a = input().split(' ')
start = int(a[0])
end = int(a[1])

if start < end:
    print("O JOGO DUROU {} HORA(S)".format(end-start))
elif (start > end):
    print("O JOGO DUROU {} HORA(S)".format(24-start+end))
else:
    print("O JOGO DUROU 24 HORA(S)")
