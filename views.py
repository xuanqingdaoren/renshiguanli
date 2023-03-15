import tkinter as tk
from tkinter import ttk
from db import db
import xlwt

class AboutFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        tk.Label(self, text='版权所有：王喆焓'+'\r'+'使用前请先点击更新.py多谢').pack()

class ChangeFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.department = tk.StringVar()
        self.name = tk.StringVar()
        self.ID = tk.StringVar()
        self.password = tk.StringVar()
        self.gender = tk.StringVar()
        self.status = tk.StringVar()
        self.age = tk.StringVar()
        self.performance = tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0, pady=10)
        tk.Label(self, text='部 门:').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.department).grid(row=1, column=2, pady=10)
        tk.Label(self, text='姓 名:').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=2, column=2, pady=10)
        tk.Label(self, text='工 号:').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.ID).grid(row=3, column=2, pady=10)
        tk.Label(self, text='密 码:').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.password).grid(row=4, column=2, pady=10)
        tk.Label(self, text='性 别:').grid(row=5, column=1, pady=10)
        tk.Entry(self, textvariable=self.gender).grid(row=5, column=2, pady=10)
        tk.Label(self, text='年 龄:').grid(row=6, column=1, pady=10)
        tk.Entry(self, textvariable=self.age).grid(row=6, column=2, pady=10)
        tk.Label(self, text='绩 效:').grid(row=7, column=1, pady=10)
        tk.Entry(self, textvariable=self.performance).grid(row=7, column=2, pady=10)
        tk.Button(self, text='查询', command=self.search_user).grid(row=8, column=1, pady=10)
        tk.Button(self, text='修改', command=self.change_user).grid(row=8, column=2, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=9, column=2, pady=10)

    def search_user(self):
        flag, info = db.search_by_username(self.name.get())
        if flag:
            self.name.set(info['department'])
            self.name.set(info['name'])
            self.name.set(info['ID'])
            self.name.set(info['password'])
            self.name.set(info['gender'])
            self.name.set(info['age'])
            self.name.set(info['performance'])
            self.status.set(f'查询成功')
        else:
            self.status.set(info)

    def change_user(self):
        stu = {'department': self.department.get(),
               'name': self.name.get(),
               'ID': self.ID.get(),
               'password': self.password.get(),
               'gender': self.gender.get(),
               'age': self.age.get(),
               'performance': self.performance.get()}
        self.department.set('')
        self.name.set('')
        self.ID.set('')
        self.password.set('')
        self.gender.set('')
        self.age.set('')
        self.performance.set('')
        db.update(stu)
        self.status.set('修改数据成功')

class FindFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.table_view = tk.Frame()
        self.table_view.pack()
        self.creat_page()
    def creat_page(self):
        columns = ('department', 'name', 'ID', 'password', 'gender', 'age', 'performance')
        columns_values = ('部门', '姓名', '工号', '密码', '性别', '年龄', '绩效')
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('department', width=110, anchor='center')
        self.tree_view.column('name', width=110, anchor='center')
        self.tree_view.column('ID', width=110, anchor='center')
        self.tree_view.column('gender', width=110, anchor='center')
        self.tree_view.column('password', width=110, anchor='center')
        self.tree_view.column('age', width=110, anchor='center')
        self.tree_view.column('performance', width=110, anchor='center')
        self.tree_view.heading('department', text='部门')
        self.tree_view.heading('name', text='姓名')
        self.tree_view.heading('ID', text='工号')
        self.tree_view.heading('gender', text='性别')
        self.tree_view.heading('password', text='密码')
        self.tree_view.heading('age', text='年龄')
        self.tree_view.heading('performance', text='绩效')
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        self.show_data_frame()
        tk.Button(self, text='刷新数据', command=self.show_data_frame).pack(anchor=tk.E, pady=5)
        tk.Button(self, text='导出数据', command=self.output_data_frame).pack(anchor=tk.E, pady=5)

    def output_data_frame(self):
        content = db.all()
        wb = xlwt.Workbook(encoding='utf-8')
        ws1 =wb.add_sheet('first')
        # 添加一个新表命名为‘first’
        ws1.write(0, 0, 'department')
        ws1.write(0, 1, 'name')
        ws1.write(0, 2, 'ID')
        ws1.write(0, 3, 'password')
        ws1.write(0, 4, 'gender')
        ws1.write(0, 5, 'age')
        ws1.write(0, 6, 'performance')
        row = 1
        # 写入起始行
        for i in content:
            ws1.write(row, 0, str(i['department']))
            ws1.write(row, 1, str(i['name']))
            ws1.write(row, 2, str(i['ID']))
            ws1.write(row, 3, str(i['password']))
            ws1.write(row, 4, str(i['gender']))
            ws1.write(row, 5, str(i['age']))
            ws1.write(row, 6, str(i['performance']))
            row += 1
        wb.save('init.xls')
        pass
    def show_data_frame(self):
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        people = db.all()
        index = 0
        for stu in people:
            self.tree_view.insert('', index + 1, values=(
                stu['department'], stu['name'], stu['ID'], stu['password'], stu['gender'], stu['age'], stu['performance']
            ))

class IncertFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.department = tk.StringVar()
        self.name = tk.StringVar()
        self.ID = tk.StringVar()
        self.password = tk.StringVar()
        self.gender = tk.StringVar()
        self.status = tk.StringVar()
        self.age = tk.StringVar()
        self.performance = tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0, pady=10)
        tk.Label(self, text='部 门:').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.department).grid(row=1, column=2, pady=10)
        tk.Label(self, text='姓 名:').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=2, column=2, pady=10)
        tk.Label(self, text='工 号:').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.ID).grid(row=3, column=2, pady=10)
        tk.Label(self, text='密 码:').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.password).grid(row=4, column=2, pady=10)
        tk.Label(self, text='性 别:').grid(row=5, column=1, pady=10)
        tk.Entry(self, textvariable=self.gender).grid(row=5, column=2, pady=10)
        tk.Label(self, text='年 龄:').grid(row=6, column=1, pady=10)
        tk.Entry(self, textvariable=self.age).grid(row=6, column=2, pady=10)
        tk.Label(self, text='绩 效:').grid(row=7, column=1, pady=10)
        tk.Entry(self, textvariable=self.performance).grid(row=7, column=2, pady=10)
        tk.Button(self, text='录入', command=self.recode_info).grid(row=8, column=2, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=9, column=2, pady=10)

    def recode_info(self):
        stu = {'department': self.department.get(),
               'name': self.name.get(),
               'ID': self.ID.get(),
               'password': self.password.get(),
               'gender': self.gender.get(),
               'age': self.age.get(),
               'performance': self.performance.get()
               }
        db.insert(stu)
        self.status.set('获取数据成功')

class DeleteFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.username = tk.StringVar()
        self.status = tk.StringVar()
        tk.Label(self, text='根据姓名删除').pack()
        tk.Entry(self, textvariable=self.username).pack()
        tk.Button(self, text='删除', command=self.delete).pack()
        tk.Label(self, textvariable=self.status).pack()

    def delete(self):
        username = self.username.get()
        flag, message = db.delete_by_username(username)
        self.status.set(message)

class CountFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.status2 = tk.StringVar()
        self.status3 = tk.StringVar()
        self.status1 = tk.StringVar()
        self.department = tk.StringVar()
        self.gender = tk.StringVar()
        self.age = tk.StringVar()
        self.performance = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0, pady=10)
        tk.Label(self, text='部 门:').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.department).grid(row=1, column=2, pady=10)
        tk.Button(self, text='查询', command=self.count_user).grid(row=1, column=3, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=1, column=4, pady=10)

        tk.Label(self, text='性 别:').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.gender).grid(row=2, column=2, pady=10)
        tk.Button(self, text='查询', command=self.count_gender).grid(row=2, column=3, pady=10)
        tk.Label(self, textvariable=self.status1).grid(row=2, column=4, pady=10)

        tk.Label(self, text='年 龄:').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.age).grid(row=3, column=2, pady=10)
        tk.Button(self, text='查询', command=self.count_age).grid(row=3, column=3, pady=10)
        tk.Label(self, textvariable=self.status2).grid(row=3, column=4, pady=10)

        tk.Label(self, text='绩 效:').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.performance).grid(row=4, column=2, pady=10)
        tk.Button(self, text='查询', command=self.count_performance).grid(row=4, column=3, pady=10)
        tk.Label(self, textvariable=self.status3).grid(row=4, column=4, pady=10)

    def count_user(self):
        people = db.all()
        a = 0
        for i in people:
            if self.department.get() == str(i['department']):
                a += 1
        if a != 0:
            self.status.set('该部门共有{}项数据'.format(a))
        else:
            self.status.set('未查询到数据!')

    def count_gender(self):
        people = db.all()
        a = 0
        for i in people:
            if self.gender.get() == str(i['gender']):
                a += 1
        if a != 0:
            self.status1.set('该性别共有{}项数据'.format(a))
        else:
            self.status1.set('未查询到数据!')

    def count_age(self):
        people = db.all()
        a = 0
        for i in people:
            if self.age.get() == str(i['age']):
                a += 1
        if a != 0:
            self.status2.set('该年龄共有{}项数据'.format(a))
        else:
            self.status2.set('未查询到数据!')

    def count_performance(self):
        people = db.all()
        a = 0
        for i in people:
            if str(self.performance.get()) == str(i['performance']):
                a += 1
        if a != 0:
            self.status3.set('该绩效共有{}项数据'.format(a))
        else:
            self.status3.set('未查询到数据!')








