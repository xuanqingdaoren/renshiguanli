import json

class MysqlDatabases:
    def __init__(self):
        self.people = json.loads(open('init.json', mode='r', encoding='utf-8').read())

    def check_login(self, username, password):
        for user in self.people:
            if username == user['ID']:
                if password == str(user['password']):
                    return True, '登陆成功'
                else:
                    return False, '密码不存在'
        return False, '登陆失败,用户不存在'

    def all(self):
        return self.people

    def insert(self, people):
        self.people.append(people)

    def delete_by_username(self, name):
        for people in self.people:
            # print(people)
            if people['name'] == name:
                self.people.remove(people)
                return True, f'{name}用户删除成功'
        return False, f'{name}用户不存在'

    def search_by_username(self, name):
        for people in self.people:
            if people['name'] == name:
                return True, people
        return False, f'{name}用户不存在'

    def change_by_username(self, name):
        for people in self.people:
            if people['name'] == name:
                return True, people
        return False, f'{name}用户不存在'

    def update(self, stu):
        for people in self.people:
            if people['name'] == stu['name']:
                people.update(stu)
                return True, '用户数据修改成功'
        return False, '用户不存在'



db = MysqlDatabases()
# if __name__ == '__main__':
#      print(db.check_login('admin', 'admin'))
#      print(db.all())
#      print(db.delete_by_username('admin'))