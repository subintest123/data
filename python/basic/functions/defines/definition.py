# 定参
# 参数的意义?  当写完业务逻辑,审视一下代码,把写死的部分当参数传递(定参---[默认值]---[变参]),这样更加灵活一点
def total(start, end):
    total = 0
    for i in range(start, end):
        total = total + i  # total+=i也可以
        # print(total)
    print(f'{start}到{end - 1}的总数和为:{total}')


total(5, 51)


# 默认值，如定义了默认值,在调用时,如果不写,就按照默认走;如果写,就根据写的走
def total1(start, end, step=1):
    total = 0
    for i in range(start, end, step):
        total = total + i  # total+=i也可以
        # print(total)
    print(f'{start}到{end - 1}的总数和为:{total}')


total1(4, 81)
total1(4, 81, 6)
