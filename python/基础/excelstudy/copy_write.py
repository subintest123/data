from xlrd import open_workbook
from xlutils.copy import copy
from xlwt import XFStyle, Borders

original_wb = open_workbook(r'd:\mendao.xls',formatting_info=True)
original_sheet = original_wb.sheet_by_name('员工表')
new_list=[]
for i in range(7,original_sheet.nrows):
    new_list.append(original_sheet.row_values(i, 11, 13))
#print(new_list)

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
    if new_list[j][0]==new_list[j][1]:
        new_sheet.write(j+7,13,'通过',style)
    else:
        new_sheet.write(j + 7, 13, '不通过',style)
new_wb.save(r'd:\mendao_copy.xls')
