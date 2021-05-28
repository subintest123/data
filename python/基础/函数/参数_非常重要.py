# 参数的意义?  当我写完业务逻辑,我会审视一下代码,把写死的部分当参数传递(定参---默认值---变参),这样更加灵活一点
# 定参
from pymysql import connect


def total(start, end):
    total = 0
    for i in range(start, end):
        total = total + i  # total+=i也可以
        # print(total)
    print(f'1+2+3+.....+{end - 1}的和为:{total}')


# total(5, 51)

# 参数:默认值
# 调用时,如写了默认值,就根据写的走,如果没有写,就按照默认走
def total2(start, end, step=1):
    total = 0
    for i in range(start, end, step):
        total = total + i  # total+=i也可以
        # print(total)
    print(f'1+2+3+.....+{end - 1}的和为:{total}')


# total2(1, 101)
# total2(1, 101, 5)

# 变参(新人了解,高手必会)
# 定义时， *将参数配成元组；调用时，*将元组或列表打散成参数进行参数传递
# 定义时，**将参数装配成字典；调用时，**将字典打散成参数进行参数传递
def total3(*args):
    total = 0
    for i in range(args[0], args[1], args[2]):
        total = total + i  # total+=i也可以
        # print(total)
    print(f'1+2+3+.....+{args[1] - 1}的和为:{total}')


# total3(1,51,4)
# total3(1,51,4,132,21,321,321,312,3123)


def total4(**kwargs):
    total = 0
    for i in range(kwargs['start'], kwargs['end'], kwargs['step']):
        total = total + i  # total+=i也可以
        # print(total)
    print(f"1+2+3+.....+{kwargs['end'] - 1}的和为:{total}")


total4(start=1, end=51, step=2)


#作业,把笔试题中的所有业务封装成函数并使用参数

connect()