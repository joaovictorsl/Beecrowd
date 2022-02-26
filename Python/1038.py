def look(code, tabela):
    for x in tabela:
        if x[0] == int(code):
            return x


tabela = [[1, 4], [2, 4.5], [3, 5], [4, 2], [5, 1.5]]
numbers = input().split(' ')
res = look(numbers[0], tabela)
print("Total: R$ {:.2f}".format(int(numbers[1])*res[1]))