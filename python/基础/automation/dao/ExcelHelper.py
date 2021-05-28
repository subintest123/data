from xlrd import open_workbook
from xlutils.copy import copy
from xlwt import Workbook, XFStyle, Borders, Font, Pattern, Alignment

from automation.utils.Config import Config

'''
    功能:Excel的工具类
    作者:蔡昶
    时间:2021-05-19
    版本:v1.0.1
'''


class ExcelHelper():
    file = '../conf/config.ini'
    def __init__(self):
        self.config = Config(self.file)
        # 这2个是给读excel
        self.book_path = self.config.get_value(self.file, 'data', 'book_path')
        self.sheet_name = self.config.get_value(self.file, 'data', 'sheet_name')

        # 写excel的属性
        self.add_sheet_name = ''
        self.save_path = ''

    # 获得工作簿
    def _get_work_book(self):
        bk = open_workbook(self.book_path, formatting_info=True)
        return bk

    # 获得工作表
    def _get_sheet(self):
        sheet = self._get_work_book().sheet_by_name(self.sheet_name)
        return sheet

    def total_rows(self):
        # 获得总行数
        nrows = self._get_sheet().nrows
        return nrows

    def total_cols(self):
        # 获得总列数
        ncols = self._get_sheet().ncols
        return ncols

    def cell_value(self, row_number, col_number):
        # 读某单元格
        cell_value = self._get_sheet().cell_value(row_number, col_number)
        return cell_value

    def col_value(self, col_number, start_row, end_row=None):
        # 读某列值 11可以写也可以不写,不写默认是最后,切片思想
        col_value = self._get_sheet().col_values(col_number, start_row, end_row)
        return col_value

    def row_value(self, row_number, start_col, end_col=None):
        # 读某行值 9可以写也可以不写,不写默认是最后,切片思想
        row_value = self._get_sheet().row_values(row_number, start_col, end_col)
        return row_value

    def allvalues_by_row(self, start_row, end_row, start_col, end_col=None):
        # 读一堆值
        new_list = []
        for i in range(start_row, end_row):
            new_list.append(self._get_sheet().row_values(i, start_col, end_col))
        return new_list

    '''
        功能:写excel,是创建一个新的excel后并写入内容
    '''

    def create_and_write(self, title, content):

        wb = Workbook('utf-8')
        sheet = wb.add_sheet(self.add_sheet_name, True)

        borders = Borders()
        borders.left = borders.THIN
        borders.right = borders.THIN
        borders.top = borders.THIN
        borders.bottom = borders.THIN

        font = Font()
        font.bold = True

        pattern = Pattern()
        pattern.pattern = pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = 22

        alignment = Alignment()
        alignment.horz = alignment.HORZ_CENTER

        # 样式
        style = XFStyle()
        style.borders = borders
        style.font = font
        style.pattern = pattern
        style.alignment = alignment

        # 6:行 4:列
        for i in range(len(title)):
            sheet.write(6, i + 4, title[i], style)

        content_style = XFStyle()
        content_style.borders = borders

        # 7:行,4:列
        for i in range(len(content)):
            for j in range(len(content[i])):
                sheet.write(i + 7, j + 4, content[i][j], content_style)

        wb.save(self.save_path)

    '''
        功能:往一个已存在的工作簿中写入数据
    '''

    def copy_write(self):
        original_wb = self._get_work_book()
        original_sheet = self._get_sheet()

        new_list = []
        for i in range(7, original_sheet.nrows):
            new_list.append(original_sheet.row_values(i, 11, 13))
        # print(new_list)

        borders = Borders()
        borders.left = borders.THIN
        borders.right = borders.THIN
        borders.top = borders.THIN
        borders.bottom = borders.THIN

        style = XFStyle()
        style.borders = borders

        new_wb = copy(original_wb)
        new_sheet = new_wb.get_sheet(0)

        for j in range(len(new_list)):
            if new_list[j][0] == new_list[j][1]:
                new_sheet.write(j + 7, 13, '通过', style)
            else:
                new_sheet.write(j + 7, 13, '不通过', style)
        new_wb.save(self.save_path)

# 测试代码
helper =ExcelHelper()
print(helper.allvalues_by_row(7,21,4,14))
print(helper.cell_value(7,6))
print(helper.total_rows())

# helper = ExcelHelper()
# helper.add_sheet_name='包包'
# helper.save_path=r'e:\凤姐.xls'
# title=['姓名','年龄','身高']
# content=[['凤姐',18,170],['范冰冰',20,180],['菜10',22,185]]
# helper.create_and_write(title,content)

# helper = ExcelHelper()
# helper.book_path=r'd:\mendao.xls'
# helper.sheet_name='员工表'
# helper.save_path=r'e:\凤姐.xls'
# helper.copy_write()
