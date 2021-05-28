from xlwt import Workbook, XFStyle, Borders, Font, Pattern, Alignment

wb = Workbook('utf-8')
sheet = wb.add_sheet('员工表', True)

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

style = XFStyle()
style.borders = borders
style.font = font
style.pattern = pattern
style.alignment = alignment

title = ['empno', 'ename', 'job', 'mgr', 'hiredate', 'sal', 'comm', 'deptno', '实际结果', '是否通过']
for i in range(len(title)):
    sheet.write(6, i + 4, title[i], style)

content_style = XFStyle()
content_style.borders = borders

content = [[7369.0, 'SMITH', 'CLERK', 7902.0, 29572.0, 800.0, '', 10.0, 10.0, ''],
           [7499.0, 'ALLEN', 'SALESMAN', 7698.0, 29637.0, 1600.0, 300.0, 30.0, 10.0, ''],
           [7521.0, 'WARD', 'SALESMAN', 7698.0, 29639.0, 1250.0, 500.0, 30.0, 10.0, ''],
           [7566.0, 'JONES', 'MANAGER', 7839.0, 29678.0, 2975.0, '', 20.0, 10.0, ''],
           [7654.0, 'MARTIN', 'SALESMAN', 7698.0, 29857.0, 1250.0, 1400.0, 30.0, 10.0, ''],
           [7698.0, 'BLAKE', 'MANAGER', 7839.0, 29707.0, 2850.0, '', 30.0, 10.0, ''],
           [7782.0, 'CLARK', 'MANAGER', 7839.0, 29746.0, 2450.0, '', 10.0, 10.0, ''],
           [7788.0, 'SCOTT', 'ANALYST', 7566.0, 31886.0, 3000.0, '', 20.0, 10.0, ''],
           [7839.0, 'KING', 'PRESIDENT', '', 29907.0, 5000.0, '', 10.0, 10.0, ''],
           [7844.0, 'TURNER', 'SALESMAN', 7698.0, 29837.0, 1500.0, 0.0, 30.0, 10.0, ''],
           [7876.0, 'ADAMS', 'CLERK', 7788.0, 31920.0, 1100.0, '', 20.0, 10.0, ''],
           [7900.0, 'JAMES', 'CLERK', 7698.0, 29923.0, 950.0, '', 30.0, 10.0, ''],
           [7902.0, 'FORD', 'ANALYST', 7566.0, 29923.0, 3000.0, '', 20.0, 10.0, ''],
           [7934.0, 'MILLER', 'CLERK', 7782.0, 29974.0, 1300.0, '', 10.0, 10.0, '']]
for i in range(len(content)):
    for j in range(len(content[i])):
        sheet.write(i + 7, j + 4, content[i][j], content_style)

wb.save(r'd:\自定义表.xls')
