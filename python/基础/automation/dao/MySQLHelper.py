from pymysql import connect

from automation.utils.Config import Config

'''
    功能:自己二次封装的MySQL的工具类,是在pymysql的基础上做的
    作者:caichang
    时间:2021-05-18
    版本:v1.0.1
'''


class MySQLHelper():
    file = './conf/config.ini'
    config = Config(file)
    # 初始化方法,因为用户名和端口一般不变,因此给了个默认
    def __init__(self):
        self.host = self.config.get_value(self.file, 'mysql', 'host')
        self.user = self.config.get_value(self.file, 'mysql', 'user')
        self.password = self.config.get_value(self.file, 'mysql', 'password')
        self.database = self.config.get_value(self.file, 'mysql', 'database')
        self.port = int(self.config.get_value(self.file, 'mysql', 'port'))

    # 获得连接
    def __getconnect(self):
        conn = connect(self.host, self.user, self.password, self.database, self.port)
        return conn

    # 获得游标
    def __getcursor(self):
        cursor = self.__getconnect().cursor()
        return cursor

    # 关闭连接
    def close(self):
        self.__getcursor().close()
        self.__getconnect().close()

    '''
        功能:查询所有数据
        返回:查询结果
        参数:
            query:sql语句
            flag:判断是所有还是一个还是多个的标签申明
            number:如果为多个,传入number即可,默认为2个
        作者:caichang
        时间:2021-05-18
        版本:v1.0.1
    '''

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
            print('对不起,第二个参数只能输all,one,many中的其中一个,'
                  '如果你写的是many,默认返回2个,可传入第三个参数来修改返回的个数')

    '''
        功能:增删改
        作者:caichang
        时间:2021-05-18
        版本:v1.0.1
    '''

    def dml(self, query):
        cursor = self.__getcursor()
        cursor.execute(query)
        self.__getconnect().commit()  # 提交

# 测试代码,可删除
# helper = MySQLHelper()
# query = 'select * from dept'
# result = helper.select(query, 'many', 3)
# print(result)
#
# # helper.dml("insert into dept(dname) values ('testing')")
# # helper.dml("update dept set dname='developer' where dname='testing'")
# helper.dml("delete from dept where dname='developer'")
# helper.close()
