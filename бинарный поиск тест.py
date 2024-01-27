

a = [9, 12, 16, 18, 23, 28, 38, 40, 43, 50]

n = int(input())
low = 0
high = len(a) - 1
mid = (low + high) // 2

def count_digits(a):
    cont = 0
    for char in a:
        if char.isdigit():
            cont += 1
    return count_digits(a)

while n != a[mid] and low < high:
    if n > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if n == a[mid]:
    print('ID:', mid)
    print('Количество попыток поиска', count_digits(a))
else:
    print("No: 'n'")


