from xlrd import open_workbook

bk = open_workbook(r'D:\mendao.xls')

sheet = bk.sheet_by_name('员工表')
# 获得总行数
print(sheet.nrows)

# 获得总列数
print(sheet.ncols)

# 读某单元格
cell_value = sheet.cell_value(8, 5)
print(cell_value)

# 读某列值 11可以写也可以不写,不写默认是最后,切片思想
col_value = sheet.col_values(5, 7, 11)
print(col_value)

# 读某行值 9可以写也可以不写,不写默认是最后,切片思想
row_value = sheet.row_values(11, 5, 9)
print(row_value)

# 读一堆值
new_list = []
for i in range(7, sheet.nrows + 1):
    new_list.append(sheet.row_values(20, 4, 13))
print(new_list)
