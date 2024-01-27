import os

#1 создание файла
def greate_fale(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)

#2 создание папки
def greate_folder(name):
    try:
        os.makedirs(name)
    except FileExistsError:
        print('Такая папка уже существует!')


if __name__=='__main__':
    greate_fale('text.dat')
    greate_fale('text.dat', 'some text')
    greate_folder('new_f')



    

    

    
    
    