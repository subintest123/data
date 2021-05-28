# 可以直接print('')就可输出想要的内容

print('hello world')


# 换行
print('jadsklfajdlfajdlfadsjfda\n'
      'fadskjfldadjksjflkdsfjsdklfjd;lfadjflk\n'
      'adjfdsaklfjadsklfjdasfkladjfklsajfdsaklfjsadklf')


# 注释
# name = "深圳市门道信息咨询有限公司"
# print("我们培训的机构是 :%s" % name)
# 快捷键 ctrl+/
print('test') # 这是简单的打印
'''
学习目标:学会python注释
用三个单引号或双引号都可以
注释在你工作中非常重要,有可能你的注释比代码还多
'''
"""
cccccccc
"""

# 变量
# 变量:你解数学时使用的x,y
# name,sex,age
# 习惯:见名知意

# 补充:格式化代码(ctrl+alt+l)

age = 20
name_2 = 'test'
print(name_2)
# 2name='baobao'
# if=

'''
变量的使用:重点
'''

# 变量名=变量值
# 上班就按照这样的方式赋值,后面的都忘记
name = 'test'
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
name = 'Su'
print(name)


# 关键字
# 带特殊颜色的就是关键字,你不用去刻意的记
# if
# else
# for
# del


# 运算符
# 1.	赋值运算符:  =
# 2.	算术运算符:  + ， - ， * ， / ， // ， % ， **
# 1.	// 返回商的整数部分
# 2.	%  返回余数(工作中这个用得多)
# 3.	** 幂运算
# 3.	关系运算符:  >，<， ==， >=，<=，!= (运用在判断的代码中)
# 4.	逻辑运算符:  and，or，not (运用在判断的代码中)

# 表达式:将不同数据（包括变量、函数）用运算符按照一定的规则连接起来的一种式子
# 简单理解:判断中写的式子都是表达式,他主要是判断结果是真还是假

name = 'test'
sal = 2000 * 12
print(sal)

print(50 // 3)
print(50 % 3)
# %读成'模'，非常常用,用来判断某个东西能不能被整除

if 51 % 3 == 0:
    print('ok')

year_sal = 20 ** 5
print(year_sal)

if 20 > 5:
    print('ok')

if 51 % 3 == 0 and 20 <= 5:
    print('hehe')

if 51 % 3 == 0 or 20 <= 5:
    print('haha')

if 51 % 3 == 0 and not 20 <= 5:
    print('yeah! :)')

if not 51 % 3 == 0 and 20 <= 5:
    print('yeah2! :)')

if not (51 % 3 == 0 and 20 <= 5):
    print('yeah3! :)')


