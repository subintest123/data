from xlrd import open_workbook

from basic.excel_study.ExcelHelpr import ExcelHelper
from basic.mysql_study.MysqlHelper import MySQLHelper

bk = open_workbook(r'D:\package\python\doc\mendao.xls')
# print(bk)

# 获得'员工表'
sheet = bk.sheet_by_name('员工表')

# 获得'员工表'的总行数
print(f'该表共有:{sheet.nrows}行')

# 获得'员工表'的总列数
print(f'该表共有:{sheet.ncols}列')

# 读取'员工表'的某单元格
cell_value = sheet.cell_value(8, 5)
print(f'第8行，第5列为:{cell_value}')

# 读'员工表'的某列值,11可写可不写,不写默认是读到最后,切片思想
# col_value = sheet.col_values(6, 9)
# print(f'第6列的值为{col_value}')
col_value = sheet.col_values(6, 9, 12)
print(f'第6列的9到12行的值为{col_value}')

# 读'员工表'某行值,9可写可不写,不写默认是读到最后,切片思想
row_value = sheet.row_values(11, 5, 9)
print(row_value)
# row_value = sheet.row_values(10, 8)
# print(row_value)

# 读'员工表'中一片值
new_list = []
for i in range(7, sheet.nrows + 1):
    new_list.append(sheet.row_values(20, 4, 13))
print(new_list)
