# 变量:你解数学时使用的x,y
# name,sex,age
# 习惯:见名知意

# 补充:格式化代码(ctrl+alt+l)

age = 20
name_2 = 'caichang'
print(name_2)
# 2name='baobao'
# if=

'''
变量的使用:重点
'''

# 变量名=变量值
# 上班就按照这样的方式赋值,后面的都忘记
name = 'caichang'
print(name)

# 一次性赋多值(不多)
empno, ename, job, sal = 7788, 'smith', 'clerk', 2000
print(ename)
print(sal)

# 连续赋值(更不多)
name = ename = cname = '凤姐'
print(name)
print(ename)

# 注意:后面覆盖前面
name = '包包'
print(name)
