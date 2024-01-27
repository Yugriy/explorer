a = [1, [2, [3, 4], 5], 6, [7, 8]]

def rec(spisok, level = 1):# spisok это переменная a
    # level это локальная переменная
    print(*spisok, 'level=', level) #звёздочка чтобы наш список распоковался
    for i in spisok: #проход по нашему списку
        #print(i, type(i))
        if type(i) == list:
            rec(i, level+1)



rec(a)