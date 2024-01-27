# правый бинарный двоичный поиск
  # список а в котором находим элемент х
def rbs(a, x):
# создаём переменные левая и правая
    L = 0
    r = len(a)
    while L + 1 != r:
# прибовляем первый и последний и делим на 2 чтобы найти серидину
        c = (L + r) // 2
        if a[c] > x:
            r = c
        else:
            L = c
    return L

a = [1, 5, 5, 5, 5, 12, 14, 17]
print(rbs(a, 1))
