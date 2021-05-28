#为什么要使用函数? 代码复用,维护度的考虑

#定义:def 函数名():
#        具体业务内容
def total():
    total = 0
    for i in range(1, 101):
        total = total + i  # total+=i也可以
        # print(total)
    print(f'1+2+3+.....+100的和为:{total}')


#调用
total()