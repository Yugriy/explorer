import os
import shutil
from subprocess import check_call, CalledProcessError

# Функция для создания файла или папки
def create(path):
    if not os.path.exists(path):
        if '.' in os.path.basename(path):  # Предполагаем, что это файл, если есть расширение
            with open(path, 'w') as file:
                file.write("")  # Создаем пустой файл
        else:
            os.makedirs(path)  # Создаем папку
        print(f"{path} создан(а).")
    else:
        print(f"{path} уже существует.")

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

# Функция для копирования файла или папки
def copy(src, dst):
    if os.path.isfile(src):
        shutil.copy(src, dst)
    elif os.path.isdir(src):
        shutil.copytree(src, dst)
    else:
        print(f"{src} не найден(а) для копирования.")
        return
    print(f"{src} скопирован(а) в {dst}.")

# Функция для выполнения команд Git
def git_command(command):
    try:
        check_call(['git'] + command.split())
    except CalledProcessError as e:
        print(f"Ошибка выполнения команды Git: {e}")
