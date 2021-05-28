from pymysql import connect


class MySQLHelper():

    def __init__(self):
        self.host = ''
        self.user = 'root'
        self.password = ''
        self.database = ''
        self.port = 3306

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

    def select(self, query, flag='all', number=2):
        cursor = self.__getcursor()
        cursor.execute(query)
        try:
            if flag == 'all':
                result = cursor.fetchall()
            elif flag == 'one':
                result = cursor.fetchone()
            elif flag == 'many':
                result = cursor.fetchmany(number)
            else:
                pass
            return result
        except Exception:
            print('对不起,第二个参数只能输all、one、many中的其中一个,'
                  '如果你写的是many,默认返回2个,可传入第三个参数来修改返回的个数')

    def dml(self, query):
        cursor = self.__getcursor()
        cursor.execute(query)
        self.__getconnect().commit()  # 提交

# # 测试
# helper = MySQLHelper()
# helper.host = 'localhost'
# helper.password = 'root'
# helper.database = 'test'
#
# query = 'select * from dept'
#
# result = helper.select(query, 'all', 3)
# print(result)
#
# # helper.dml("insert into dept(dname) values ('testing')")
# # helper.dml("update dept set dname='developer' where dname='testing'")
# helper.dml("delete from dept where dname='developer'")
# helper.close()
