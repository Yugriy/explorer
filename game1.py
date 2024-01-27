print('Инструкция:')
print('Визуальные обозначения:')
print('Стол - Table - 田')
print('Верхний стул - Chair1 - 国')
print('Шкаф - Wardrobe - 目')
print('Нижний стул - Chair2 - 四')
print('Пустая ячейка - 口')
print('Кресло - Armchair - 画')
print('Управление:')
print('Для начала решения введите Start')
print('Далее введите предмет')
print('Дальше введите направление')
print('Все вводы по-английски, приведенными выше обозначениями')
print('Когда кресло и шкаф поменяются местами,')
print('програма автоматически завершится')
print('Начальное положение:')
pos=[['Table','Chair1','Wardrobe'],
['Chair2','Empty','Armchair']]
mov=["Up","Left","Down","Right"]
def Result():
    for i in range(2):
        vis=[]
    for j in range(3):
        if pos[i][j]=="Empty":
            vis.append("口")
        elif pos[i][j]=="Wardrobe":
            vis.append("目")
        elif pos[i][j]=="Table":
            vis.append("田")
        elif pos[i][j]=="Chair1":
            vis.append("国")
        elif pos[i][j]=="Chair2":
            vis.append("四")
        elif pos[i][j]=="Armchair":
            vis.append("画")
            print(vis)
    print('------------------')

def Left():
    if it in pos[0]:
        if pos[0].index(it)!=0:
            if pos[0][pos[0].index(it)-1]=="Empty":
                pos[0][pos[0].index(it)-1]=it
                pos[0][pos[0].index(it)+1]="Empty"
            else:
                print('Невозможно переместить')
            #else:
                if pos[1].index(it)!= 0:
                    if pos[1][pos[1].index(it)-1]=="Empty":
                        pos[1][pos[1].index(it)-1]=it
                        pos[1][pos[1].index(it)+1]="Empty"
                    else:
                        print('Невозможно переместить')
def Right():
    if it in pos[0]:
        if pos[0].index(it)!=2:
            if pos[0][pos[0].index(it)+1]=="Empty":
                pos[0][pos[0].index(it)+1]=it
                pos[0][pos[0].index(it)]="Empty"
            else:
                print("Невозможно переместить")
            #else:
                if pos[1].index(it)!=2:
                    if pos[1][pos[1].index(it)+1]=="Empty":
                        pos[1][pos[1].index(it)+1]=it
                        pos[1][pos[1].index(it)]="Empty"
                    else:
                        print("Невозможно переместить")
def Up():
    if it not in pos[0]:
        if pos[0][pos[1].index(it)]=="Empty":
            pos[0][pos[1].index(it)]=it
            pos[1][pos[1].index(it)]="Empty"
        else:
            print("Невозможно переместить")
def Down():
    if it not in pos[1]:
        if pos[1][pos[0].index(it)]=="Empty":
            pos[1][pos[0].index(it)]=it
            pos[0][pos[0].index(it)]="Empty"
        else:
            print("Невозможно переместить")
Result()
op=input()
if op=="Start":
    while op!="End":
        it=input()
    if it in (pos[0]+pos[1]):
        di=input()
    if di in mov:
        if di=="Up":
            Up()
    elif di=="Left":
        Left()
    elif di=="Down":
        Down()
    elif di=="Right":
        Right()

Result()
if "Wardrobe" in pos[1] and "Armchair" in pos[0]:
    if pos[1].index("Wardrobe")==2 and pos[0].index("Armchair")==2:
        op=="End"
print('Поздравляю, Вы решили пазл!')
