# 封装

# 总和
def Task1(start, end):
    total = 0
    for i in range(start, end):
        total = total + i
    print(f'{start}到{end - 1}的总数和为:{total}')


# Task1(5, 51)

# 总和2
def Total(start, end, step=1):
    total = 0
    for i in range(start, end, step):
        total = total + i
    print(f'{start}到{end - 1}的总数和为:{total}')


# Total(4, 81)
# Total(4, 81, 6)


# 整除
def Lists(start, end):
    lists = []
    for i in range(start, end):
        if i % 3 == 0 and i % 5 != 0:
            lists.append(i)
    print(f'{end - 1}以内能被3整除但不能被5整除的数为:{lists}')


# Lists(1, 81)


# 九九乘法表
def Task2(start, end):
    for i in range(start, end):
        for j in range(1, i + 1):
            print('{}x{}={}\t'.format(j, i, i * j), end='')
        print()


# Task2(8, 12)


# 冒泡排序
def Bubbling(Bub_lists):
    for i in range(len(Bub_lists) - 1):
        for j in range(len(Bub_lists) - i - 1):
            if Bub_lists[j] > Bub_lists[j + 1]:
                Bub_lists[j], Bub_lists[j + 1] = Bub_lists[j + 1], Bub_lists[j]
    return Bub_lists


# Bub_lists = [2346, 246, 1343, 23, 4555, 2, 25]    # 冒泡排序
# print(Bubbling(Bub_lists))


# 判断天数
def Data(year, month, day):
    total_for_months = 0
    months_list_value = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(month - 1):
        total_for_months = months_list_value[i] + total_for_months
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        total = total_for_months + day + 1
    else:
        total = total_for_months + day
    print(f'今天是整年的第{total}天')


# Data(2020,5,12)


# 列表生成式
def Task_lists(start, end):
    lists = []
    for i in range(start, end):
        lists.append(i)
    print(lists)


# Task_lists(2, 15)


# 判断是平年还是闰年
def task2(year):
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        print('闰年')
    else:
        print('平年')


# task2(2020)


# 挑水
def task7(start, end, step=0):
    counts = 0
    for i in range(start, end, step):
        counts = counts + 1
    return counts


# s=task7(15,50,3)
# print(f'挑满还需要“{s}”桶')
