from xlrd import open_workbook
from xlutils.copy import copy
from xlwt import Workbook, XFStyle, Borders, Font, Pattern, Alignment


class ExcelHelper():

    def __init__(self):
        self.book_path = ''
        self.sheet_name = ''

        # 写excel的属性
        self.add_sheet_name = ''
        self.save_path = ''

    # 获得工作簿
    def _get_work_book(self):
        bk = open_workbook(self.book_path, formatting_info=True)
        return bk

    # 获得工作表
    def get_sheet(self):
        sheet = self._get_work_book().sheet_by_name(self.sheet_name)
        return sheet


    def total_rows(self):
        # 获得总行数
        nrows = self.get_sheet().nrows
        return nrows

    def total_cols(self):
        # 获得总列数
        ncols = self.get_sheet().ncols
        return ncols

    def cell_value(self, row_number, col_number):
        # 读某单元格
        cell_value = self.get_sheet().cell_value(row_number, col_number)
        return cell_value

    def col_value(self, col_number, start_row, end_row=None):
        # 读某列值
        col_value = self.get_sheet().col_values(col_number, start_row, end_row)
        return col_value

    def row_value(self, row_number, start_col, end_col=None):
        # 读某行值
        row_value = self.get_sheet().row_values(row_number, start_col, end_col)
        return row_value

    def all_row_values(self, start_row, end_row, start_col, end_col=None):
        new_list = []
        for i in range(start_row, end_row):
            new_list.append(self.get_sheet().row_values(i, start_col, end_col))
        return new_list

    def create_and_write(self, title, content):

        wb = Workbook('utf-8')
        sheet = wb.add_sheet(self.add_sheet_name, True)

        # 定义边框
        borders = Borders()
        borders.left = Borders.THIN
        borders.right = Borders.THIN
        borders.top = Borders.THIN
        borders.bottom = Borders.THIN

        # 是否加粗
        font = Font()
        font.bold = True

        # 设置背景色
        pattern = Pattern()
        pattern.pattern = pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = 23

        # 居中显示
        alignment = Alignment()
        alignment.horz = Alignment.HORZ_CENTER

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
        content_style.alignment = alignment

        # 7:行,4:列
        for i in range(len(content)):
            for j in range(len(content[i])):
                sheet.write(i + 7, j + 4, content[i][j], content_style)

        wb.save(self.save_path)

    def copy_write(self):
        original_wb = self._get_work_book()
        original_sheet = self.get_sheet()

        new_list = []
        for i in range(7, original_sheet.nrows):
            new_list.append(original_sheet.row_values(i, 11, 13))

        borders = Borders()
        borders.left = borders.THIN
        borders.right = borders.THIN
        borders.top = borders.THIN
        borders.bottom = borders.THIN

        alignment = Alignment()
        alignment.horz = Alignment.HORZ_CENTER

        style = XFStyle()
        style.borders = borders
        style.alignment = alignment

        new_wb = copy(original_wb)
        new_sheet = new_wb.get_sheet(0)

        for j in range(len(new_list)):
            if new_list[j][0] == new_list[j][1]:
                new_sheet.write(j + 7, 12, '通过', style)
            else:
                new_sheet.write(j + 7, 12, '不通过', style)
        new_wb.save(self.save_path)


# # 测试代码
# helper = ExcelHelper()
# helper.book_path = r'd:\mendao.xls'
# helper.sheet_name = '员工表'
# print(helper.all_row_values(7, 21, 4, 14))
# print(helper.cell_value(7, 6))
# print(helper.total_rows())

# helper = ExcelHelper()
# helper.add_sheet_name = 'test'
# helper.save_path = r'D:\凤姐.xls'
# title = ['姓名', '年龄', '身高']
# content = [['凤姐', 18, 170], ['范冰冰', 20, 180], ['菜10', 22, 185]]
# helper.create_and_write(title, content)

# helper = ExcelHelper()
# helper.book_path = r'd:\mendao.xls'
# helper.sheet_name = '员工表'
# helper.save_path = r'D:\test001.xls'
# helper.copy_write()

# # 写入
# helper = ExcelHelper()
# helper.add_sheet_name = 'SUBIN'
# helper.save_path = r'D:\SUBIN\测试.xls'
# title = ['姓名', '年龄', '身高']
# content = [['Jack', 20, 178], ['Lisa', 18, 165], ['Jeson', 21, 185]]
# helper.create_and_write(title, content)

# # 复制
# helper = ExcelHelper()
# helper.book_path = r'D:\subin\自定义表.xls'
# helper.sheet_name = '员工表'
# helper.save_path = r'D:\subin\test002.xls'
# helper.copy_write()
