f1 = 1
f2 = 1

n = int(input())

print(f1, f2, end=' ')
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    if n % 2 == 0:
        print(f2, end=' ')



