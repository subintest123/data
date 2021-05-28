class HomeWork():
    def __init__(self):
        self.start = 1
        self.end = 5
        self._lists = []
        self.__total = 0

    '''
    作用:求x...y的和的值
    作者:蔡昶
    时间:2021-05-17
    '''

    def one(self):
        for i in range(self.start, self.end):
            self.__total = self.__total + i  # total+=i也可以
            # print(total)
        print(f'1+2+3+.....+{self.end - 1}的和为:{self.__total}')

    def two(self, have, cannothave):
        for i in range(self.start, self.end):
            if i % have == 0 and i % cannothave != 0:
                self._lists.append(i)
        return self._lists
        # print(f'#{self.end-1}以内能被{have}整除但不能被{cannothave}整除的数为:{self._lists}')

    def three(self):
        for i in range(self.start, self.end):
            for j in range(self.start, i + 1):
                print('{}x{}={}\t'.format(j, i, i * j), end='')
            print()

    def four(self, lists):
        for i in range(len(lists) - 1):  # 1为自身的那个,所以要-1 控制循环次数
            for j in range(len(lists) - i - 1):  # 每次减去已经排好的那个数和自己要迭代的那个数 控制每一个和他的下一个比
                if lists[j] > lists[j + 1]:
                    lists[j], lists[j + 1] = lists[j + 1], lists[j]
        return lists


hw = HomeWork()
hw.start = 1
hw.end = 101
hw.one()
result = hw.two(5, 8)
print(f'#{hw.end - 1}以内数为:{result}')
hw.three()

bubbling_list = [213, 4, 1324, 1324, 1324, 1324, 32]
print(f'冒泡排序后的结果是:{hw.four(bubbling_list)}')

