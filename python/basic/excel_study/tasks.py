# 把excel中的数据读出来插入到mysql表中
from basic.excel_study.ExcelHelpr import ExcelHelper
from basic.mysql_study.MysqlHelper import MySQLHelper

excel = ExcelHelper()
excel.book_path = r'D:\subin\test002.xls'
excel.sheet_name = '员工表'

data = excel.all_row_values(6, 18, 7, 10)
print(data)

mysql = MySQLHelper()
mysql.host = 'localhost'
mysql.password = 'root'
mysql.database = 'test'

for i in range(len(data)):
    sql = f"insert into student(name,sex) values ('{data[i][0]}',{data[i][1]})"
    mysql.dml(sql)

mysql.close()
