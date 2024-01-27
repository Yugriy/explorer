import tkinter as tk
from tkinter import messagebox

def check_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "user" and password == "passwd":
        messagebox.showinfo("Успешный вход", "Вы успешно вошли в систему!")
    else:
        messagebox.showerror("Ошибка входа", "Неправильный логин или пароль")

root = tk.Tk()
root.title("Вход")

username_label = tk.Label(root, text="Логин:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Пароль:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Войти", command=check_login)
login_button.pack()

root.mainloop()