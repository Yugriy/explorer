def power(x, n): #возвести число x в степень n
    if n == 0:
        return 1
    if n < 0: #если степень отрицательная
        return 1/power(x, -n)
    if n % 2 == 0:
        return power(x, n//2)*power(x, n//2)
    else:
        return power(x, n-1)*x

x = int(input())
n = int(input())
print(power(x, n))

