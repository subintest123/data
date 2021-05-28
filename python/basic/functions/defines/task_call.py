# 调用

from basic.functions.defines.task import Task1, Total, Lists, Task2, Bubbling, Data, Task_lists, task2, task7

# 总和1
Task1(4, 51)
# 总和2
Total(6, 91)
Total(4, 81, 6)
# 整除
Lists(5, 8)
# 九九乘法表
Task2(7, 13)
# 冒泡排序
Bub_lists = [2346, 246, 1343, 23, 4555, 2, 25]
Bubbling(Bub_lists)
# 判断天数
Data(2020, 5, 12)
# 列表生成式
Task_lists(2, 15)
# 判断闰年还是平年
task2(2020)
# 挑水
s = task7(15, 50, 3)
print(f'挑满还需要“{s}”桶')
