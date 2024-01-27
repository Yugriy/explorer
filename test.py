f1 = 0
f2 = 1
summa = 0
n = int(input()) 
print(f2, end=' ')

for i in range(n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
     
if f2 % 2 == 0:
    print("сумма чётных=", summa + f2)


