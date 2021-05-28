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
    cell_value = get_sheet().cell_value(row_number, col_number)
    return cell_value


def col_value(col_number, start_row, end_row=None):
    # 读某列值 11可以写也可以不写,不写默认是最后,切片思想
    col_value = get_sheet().col_values(col_number, start_row, end_row)
    return col_value


def row_value(row_number, start_col, end_col=None):
    # 读某行值 9可以写也可以不写,不写默认是最后,切片思想
    row_value = get_sheet().row_values(row_number, start_col, end_col)
    return row_value


def allvalues_by_row(start_row, end_row, start_col, end_col=None):
    # 读一堆值
    new_list = []
    for i in range(start_row, end_row):
        new_list.append(get_sheet().row_values(i, start_col, end_col))
    return new_list
