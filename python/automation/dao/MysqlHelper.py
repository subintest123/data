from pymysql import connect

from automation.utils.Config import Config


class MySQLHelper():
    file = './conf/config.ini'
    config = Config(file)

    def __init__(self):
        self.host = self.config.get_value(self.file, 'mysql', 'host')
        self.user = self.config.get_value(self.file, 'mysql', 'user')
        self.password = self.config.get_value(self.file, 'mysql', 'password')
        self.database = self.config.get_value(self.file, 'mysql', 'database')
        self.port = int(self.config.get_value(self.file, 'mysql', 'port'))

    # 获得连接
    def __getconnect(self):
        conn = connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
        return conn

    # 获得游标
    def __getcursor(self):
        cursor = self.__getconnect().cursor()
        return cursor

    # 关闭连接
    def close(self):
        self.__getcursor().close()
        self.__getconnect().close()

    # 查询
    def select(self, query, flag='all', number=2):
        cursor = self.__getcursor()
        cursor.execute(query)
        try:
            if flag == 'all':   # ‘all’-->查询所有
                result = cursor.fetchall()
            elif flag == 'one':   # ‘one’-->查询一个
                result = cursor.fetchone()
            elif flag == 'many':   # ‘many’-->查询一些
                result = cursor.fetchmany(number)
            else:
                pass
            return result
        except Exception:
            print('对不起,第二个参数只能输all、one、many中的其中一个,'
                  '如果你写的是many,默认返回2个,可传入第三个参数来修改返回的个数')

    # 增删改
    def dml(self, query):
        cursor = self.__getcursor()
        cursor.execute(query)
        self.__getconnect().commit()  # 提交

# # 测试
# helper = MySQLHelper()
# helper.host = 'localhost'
# helper.password = 'root'
# helper.database = 'test'

# # helper.dml("insert into dept(dname) values ('testing')")
# # helper.dml("update dept set dname='developer' where dname='testing'")
# helper.dml("delete from dept where dname='developer'")
# helper.close()
# helper = MySQLHelper()
# query = 'select * from dept'
# result = helper.select(query, 'many', 3)
# print(result)
