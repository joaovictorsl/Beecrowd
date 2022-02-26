dictionary = { 
  61: 'Brasilia',
  71: 'Salvador',
  11: 'Sao Paulo',
  21: 'Rio de Janeiro',
  32: 'Juiz de Fora',
  19: 'Campinas',
  27: 'Vitoria',
  31: 'Belo Horizonte'
}

DDD = int(input())

destination = dictionary.get(DDD)

if destination:
    print(destination)
else:
    print("DDD nao cadastrado")
