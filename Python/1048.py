n = float(input())

if 0 <= n <= 400:
    p = 15
    m = n*1.15
if 400 < n <= 800:
    p = 12
    m = n*1.12
if 800 < n <= 1200:
    p = 10
    m = n*1.10
if 1200 < n <= 2000:
    p = 7
    m = n*1.07
if n > 2000:
    p = 4
    m = n*1.04

print(
    """Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: {} %""".format(m, m-n, p))
