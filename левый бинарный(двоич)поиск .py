
# левый бинарный двоичный поиск

def lbs(a, x):  # список а в котором находим элемент х
# создаём переменные левая и правая
    L = -1
    r = len(a) - 1
    while L + 1 != r:
# прибовляем первый и последний и делим на 2 чтобы найти серидину
        c = (L + r) // 2
        if a[c] < x:
            L = c
        else:
            r = c
    return r

a = [1, 5, 5, 5, 5, 12, 14, 17]
print(lbs(a, 11))




