a = [9, 12, 16, 18, 23, 28, 38, 40, 43, 50]

n = int(input())
low = 0
high = len(a) - 1
count = 0
check = False

while low <= high:
    count += 1
    mid = (low + high) // 2
    #print('step:',count)
    #print('check number:', a[mid])
    if n == a[mid]:
        check = True
        break
    if n > a[mid]:
        low = mid + 1
    else:
        high = mid - 1

        
if check == True:
    print('Число найдено.')
    print('ID:', mid)
    print('Количество попыток поиска =', count)
else:
    print('Число не найдено.')
