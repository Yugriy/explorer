import os
import shutil
from subprocess import check_call, CalledProcessError

# Функция для создания файла или папки   
def create(path):
    try:
        if not os.path.exists(path):
            if '.' in os.path.basename(path):  # Предполагаем, что это файл, если есть расширение
                with open(path, 'w') as file:
                    file.write("")  # Создаем пустой файл
            else:
                os.makedirs(path)  # Создаем папку
            print(f"{path} создан(а).")
        else:
            print(f"{path} уже существует.")
    except OSError:
        print('Ничего не создано, т.к. задано некорректное имя')

# Функция для удаления файла или папки
def delete(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:
        print(f"{path} не найден(а).")
        return
    print(f"{path} удален(а).")

# Функция для перемещения файла или папки
def move(src, dst):
    try:
        shutil.move(src, dst)
        print(f"{src} перемещен(а) в {dst}.")
    except FileNotFoundError:
        print(f"{src} не найден(а) для перемещения.")
    except OSError:
        print('Ничего не пермещено, т.к. указано некорректное имя')

# Функция для копирования файла или папки
def copy(src, dst):
    try:
        if os.path.isfile(src):
            shutil.copy(src, dst)
        elif os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            print(f"{src} не найден(а) для копирования.")
            return
        print(f"{src} скопирован(а) в {dst}.")
    except OSError:
        print('Ничего не скопировано, т.к. указано некорректное имя')

# Функция для выполнения команд Git
def git_command(command):
    try:
        check_call(['git'] + command.split())
    except CalledProcessError as e:
        print(f"Ошибка выполнения команды Git: {e}")

       
# Интерактивный цикл командной строки
while True:
    command = input("Введите команду: ").strip().lower()
    if command == "exit":
        break
    args = command.split()
    if args[0] == "create":
        create(' '.join(args[1:]))
    elif args[0] == "delete":
        delete(' '.join(args[1:]))
    elif args[0] == "move":
        move(args[1], args[2])
    elif args[0] == "copy":
        copy(args[1], args[2])
    elif args[0] == "git":
        git_command(' '.join(args[1:]))
    else:
        print("Неизвестная команда.")
