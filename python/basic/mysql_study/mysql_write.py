# 把mysql的数据读出来写入到excel中
from basic.excel_study.ExcelHelpr import ExcelHelper
from basic.mysql_study.MysqlHelper import MySQLHelper

mysql = MySQLHelper()
mysql.host = 'localhost'
mysql.password = 'root'
mysql.database = 'test'

sql = 'select * from student where sex=0'
data = mysql.select(sql)
# print(data)

excel = ExcelHelper()
excel.add_sheet_name = '学生信息'
excel.save_path = r'd:\学生信息表.xls'
title = ['id', 'name', 'sex']
excel.create_and_write(title, data)
