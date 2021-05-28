from xlrd import open_workbook


def get_sheet():
    bk = open_workbook(r'D:\mendao.xls')
    sheet = bk.sheet_by_name('员工表')
    return sheet


def total_rows():
    # 获得总行数
    nrows = get_sheet().nrows
    return nrows


def total_cols():
    # 获得总列数
    ncols = get_sheet().ncols
    return ncols


def cell_value(row_number, col_number):
    # 读某单元格
    cell_values = get_sheet().cell_value(row_number, col_number)
    return cell_values


def col_value(col_number, start_row, end_row=None):
    # 读某列值
    col_values = get_sheet().col_values(col_number, start_row, end_row)
    return col_values


def row_value(row_number, start_col, end_col=None):
    # 读某行值 9可以写也可以不写,不写默认是最后,切片思想
    row_values = get_sheet().row_values(row_number, start_col, end_col)
    return row_values


def all_row_values(start_row, end_row, start_col, end_col=None):
    new_list = []
    for i in range(start_row, end_row):
        new_list.append(get_sheet().row_values(i, start_col, end_col))
    return new_list


# 获得'员工表'的总列数
print(f'该表共有:{total_rows()}列')
# 获得'员工表'的总行数
print(f'该表共有:{total_cols()}行')
# 读取'员工表'的某单元格
cell_values = get_sheet().cell_value(8, 5)
print(f'第8行，第5列为:{cell_values}')
# 读'员工表'的某列值
col_values = get_sheet().col_values(6, 9, 12)
print(f'第6列的9到12行的值为{col_values}')
# 读'员工表'某行值,9可写可不写,不写默认是读到最后,切片思想
row_values = get_sheet().row_values(11, 5, 9)
print(row_values)
# 读'员工表'中第10到13行，第5-7列的所有值
print(all_row_values(10, 13, 5, 8))
