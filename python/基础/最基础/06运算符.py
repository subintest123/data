# 1.	赋值运算符:  =
# 2.	算术运算符:  + ， - ， * ， / ， // ， % ， **
# 1.	// 返回商的整数部分
# 2.	%  返回余数(工作中这个用得多)
# 3.	** 幂运算
# 3.	关系运算符:  >，<， ==， >=，<=，!= (运用在判断的代码中)
# 4.	逻辑运算符:  and，or，not (运用在判断的代码中)

# 表达式:将不同数据（包括变量、函数）用运算符按照一定的规则连接起来的一种式子
# 简单理解:判断中写的式子都是表达式,他主要是判断结果是真还是假

name = 'caichang'
sal = 2000 * 12
print(sal)

print(50 // 3)
print(50 % 3)  # %读成'模'  50模3的值 他非常常用,判断某个东西能不能被整除就靠它

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
