# 1.把excel中的数据读出来插入到mysql表中
from basic.excel_study.ExcelHelpr import ExcelHelper
from basic.mysql_study.MysqlHelper import MySQLHelper

excel = ExcelHelper()
excel.book_path = r'D:\subin\test002.xls'
excel.sheet_name = '员工表'

data = excel.all_row_values(11, 15, 6, 10)
print(data)

mysql = MySQLHelper()
mysql.host = 'localhost'
mysql.password = 'root'
mysql.database = 'test'

for i in range(len(data)):
    sql = f"insert into students(name,sex) values ('{data[i][0]}',{data[i][1]})"
    mysql.dml(sql)

mysql.close()
#
# 2.把mysql的数据读出来写入到excel中
# from python基础.excelstudy.ExcelHelper import ExcelHelper
# from python基础.mysqlstudy.MySQLHelper import MySQLHelper
#
# mysql=MySQLHelper()
# mysql.host='localhost'
# mysql.password='root'
# mysql.database='blog'
#
# sql='select * from student where sex=0'
# data = mysql.select(sql)
# #print(data)
#
# excel = ExcelHelper()
# excel.add_sheet_name='学生信息'
# excel.save_path=r'd:\学生信息表.xls'
# title=['编号','姓名','性别']
# excel.create_and_write(title,data)
