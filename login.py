import tkinter as tk
from tkinter import messagebox
from db import db
from Mainpage import Main
# 构造登陆界面
class LoginPage:
    def __init__(self,master):
        self.root = master
        self.root.geometry('300x180')
        self.root.title('登录页')

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.page = tk.Frame(root)
        self.page.pack()
        tk.Label(self.page).grid()
        tk.Label(self.page, text='工号：').grid(row=1, column=1)
        tk.Entry(self.page, textvariable=self.username).grid(row=1, column=2)

        tk.Label(self.page, text='密码：').grid(row=2, column=1, pady=10)
        tk.Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=2)

        tk.Button(self.page, text='登录', command=self.login).grid(row=3, column=1, pady=10)
        tk.Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=2)
        root.mainloop()
# 跳转功能
    def login(self):
        name = self.username.get()
        pwd = self.password.get()
        flag, message = db.check_login(name, pwd)
        # 判断是否具备条件
        if flag:
            self.page.destroy()
            Main(self.root)
        else:
            messagebox.showwarning(title='警告', message=message)


if __name__ == '__main__':
    root = tk.Tk()
    LoginPage(master=root)

