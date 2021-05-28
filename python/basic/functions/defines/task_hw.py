# 类

class HomeWork():
    def __init__(self):
        self.start = 5
        self.end = 20
        self._lists = []
        self.__total = 0

    # 总和
    def hw_sum(self):
        for i in range(self.start, self.end):
            self.__total = self.__total + i
        print(f'{self.start}到{self.end - 1}的总数和为:{self.__total}')

    # 整除
    def hw_division(self, have, cannot):
        for i in range(self.start, self.end):
            if i % have == 0 and i % cannot != 0:
                self._lists.append(i)
        return self._lists

    # 九九乘法表
    def hw_multiply(self):
        for i in range(self.start, self.end):
            for j in range(self.start, i + 1):
                print('{}x{}={}\t'.format(j, i, i * j), end='')
            print()

    # 列表生成式
    def hw_lists(self):
        lists = []
        for i in range(self.start, self.end):
            lists.append(i)
        print(lists)

    # 冒泡排序
    def hw_sort(self, Bub_lists):
        for i in range(len(Bub_lists) - 1):
            for j in range(len(Bub_lists) - i - 1):
                if Bub_lists[j] > Bub_lists[j + 1]:
                    Bub_lists[j], Bub_lists[j + 1] = Bub_lists[j + 1], Bub_lists[j]
        return Bub_lists

    # 判断平年闰年
    def hw_judge(self, year):
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            print('闰年')
        else:
            print('平年')

    # 查看天数
    def hw_data(self, year, month, day):
        total_for_months = 0
        months_list_value = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(month - 1):
            total_for_months = months_list_value[i] + total_for_months
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            total = total_for_months + day + 1
        else:
            total = total_for_months + day
        print(f'今天是整年的第{total}天')

    # 挑水
    def task7(self, step=0):
        counts = 0
        for i in range(self.start, self.end, step):
            counts = counts + 1
        return counts


Su = HomeWork()
Su.start = 5
Su.end = 21
# 总和
Su.hw_sum()
# 整除
result = Su.hw_division(5, 8)
print(f'{Su.end - 1}内数为:{result}')
# 九九乘法表
Su.hw_multiply()
# 列表生成式
Su.hw_lists()
# 冒泡排序
Bub_lists = [2346, 246, 1343, 23, 4555, 2, 25]
print(Su.hw_sort(Bub_lists))
# 判断平年闰年
Su.hw_judge(1990)
Su.hw_data(2021, 5, 20)
# 挑水
s = Su.task7(3)
print(f'挑满还需要“{s}”桶')
