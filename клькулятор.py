login = input('Введите логин: ')
if not login == 'admin':
    print('Несуществующий логин')
else:    
    pasword = input('Введите пароль: ')
    if pasword == 'admin':
        print('Добро пожаловать admin')
    else:
        print('Неверный пароль')





num1 = int(input('ввод первого значения: '))
oper = input('выбор операции: ')
num2 = int(input('ввод второго значения: '))
if oper == '+':
    print(num1 + num2)
elif oper == '-':
    print(num1 - num2)
elif oper == '*':
    print(num1 * num2)
elif num2 != 0 and oper == '/':
    print(num1 / num2)
elif num2 == 0:
    print('На ноль делить нельзя!')
else:
    print('Неверная операция')

