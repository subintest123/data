from 基础.mysqlstudy.MySQLHelper import MySQLHelper

helper = MySQLHelper()
helper.host = '192.168.1.40'
helper.password = 'root'
helper.database = 'project'

sql = 'select * from score'
result = helper.select(sql, 'many', 2)
print(result)

helper.close()
