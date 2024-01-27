x = int(input())

def lbs(a, x):
    h = -1
    r = len(a) - 1
    while h + 1 != r:
        c = (h + r) // 2
        if a[c] < x:
            h = c
    return r

a = [1, 5, 5, 5, 5, 12, 14, 17]
print(lbs(a))
