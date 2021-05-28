# 四种方式

def task1():
    total = 0
    for i in range(4, 50, 1):
        total = total + i
    print(total)


task1()


def task2(start, end, step=1):
    total = 0
    for i in range(start, end, step):
        total = total + i
    print(total)


task2(4, 81, 2)


def task3():
    total = 0
    for i in range(6, 71, 1):
        total = total + i
    return total


s = task3()
print(s)


def task4(start, end, step=1):
    total = 0
    for i in range(start, end, step):
        total = total + i
    return total


s2 = task4(2, 41)
print(f'总数和为:{s2}')



