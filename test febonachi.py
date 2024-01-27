
f1 = 0
f2 = 1
sum = 0
n = int(input())

print(f1, f2, end=' ')
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
    if f2 % 2 == 0:
        print(sum + f2)    
