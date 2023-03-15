import tkinter as tk
import views

class Main:
    def __init__(self, master: tk.Tk):
        # 方便代码
        self.root = master
        self.root.geometry('1000x500')
        self.root.title('人事管理系统')
        self.creat_page()

    # 菜单栏
    def creat_page(self):

        self.about_frame = views.AboutFrame(self.root)
        self.change_frame = views.ChangeFrame(self.root)
        self.insert_frame = views.IncertFrame(self.root)
        self.delete_frame = views.DeleteFrame(self.root)
        self.find_frame = views.FindFrame(self.root)
        self.count_frame = views.CountFrame(self.root)

        menubar = tk.Menu(self.root)
        menubar.add_command(label='录入', command=self.show_insert)
        menubar.add_command(label='查询', command=self.show_find)
        menubar.add_command(label='删除', command=self.show_delete)
        menubar.add_command(label='修改', command=self.show_change)
        menubar.add_command(label='统计', command=self.show_count)
        menubar.add_command(label='关于', command=self.show_about)
        self.root['menu'] = menubar

    def show_about(self):
        self.about_frame.pack()
        self.find_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.change_frame.pack_forget()
        self.count_frame.pack_forget()

    def show_count(self):
        self.count_frame.pack()
        self.about_frame.pack_forget()
        self.find_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.change_frame.pack_forget()

    def show_change(self):
        self.change_frame.pack()
        self.find_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.about_frame.pack_forget()
        self.count_frame.pack_forget()

    def show_insert(self):
        self.insert_frame.pack()
        self.find_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.about_frame.pack_forget()
        self.change_frame.pack_forget()
        self.count_frame.pack_forget()

    def show_delete(self):
        self.delete_frame.pack()
        self.about_frame.pack_forget()
        self.change_frame.pack_forget()
        self.find_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.count_frame.pack_forget()

    def show_find(self):
        self.find_frame.pack()
        self.delete_frame.pack_forget()
        self.about_frame.pack_forget()
        self.change_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.count_frame.pack_forget()


if __name__ == '__main__':
    root = tk.Tk()
    Main(root)
    root.mainloop()