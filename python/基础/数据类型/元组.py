#元组 tuple

#1.新建
emp=() #空元组
emp=(7788,'caichang','teacher',200,None,True,'老王') #一维
emp=((1,'张飞','屠夫'),(2,'刘备','卖草鞋'),(3,'关羽','保安'),(4,'孙尚香','大小姐')) #二维


#2.访问
#     0       1          2      3   4     5    6
emp=(7788,'caichang','teacher',200,None,True,'老王')
#     -7     -6         -5     -4  -3     -2   -1

print(emp[2]) #正向访问
print(emp[-5]) #反向访问

emp=((1,'张飞','屠夫'),(2,'刘备','卖草鞋'),(3,'关羽','保安'),(4,'孙尚香','大小姐'))
print(emp[2][1])

#切片(一定要掌握)
emp=(7788,'caichang','teacher',200,None,True,'老王')

print(emp[1:4]) #从1开始切,切到4但不包含4  [1,4)  这个最常用
print(emp[1:-3])
print(emp[-6:4])
print(emp[-6:-3])

print(emp[3:])
print(emp[:3])

#当第一个值确定后,第二个值一定要在第一个值的右边,否则结果切出来是空
print(emp[-4:-6]) # 结果是 (),从左到右


#3.遍历(一个一个取出来)(必会)
#知识:一维一个for,二维2个for,依次类推(必须掌握)

emp=(7788,'caichang','teacher',200,None,True,'老王')
#第一种方案(不好,会炸的 :( )
# print(emp[0])
# print(emp[1])
# print(emp[2])
# ...
# print(emp[6])

#range()

#从1开始到10但不包含10且步长为3
#其中1可以不写,如不写默认是从0开始
#3可以不写,步长默认是1
for i in range(1,10,3):
    print(i)

#第二种方案,采用了range
for i in range(7):
    print(emp[i])

#len() ===lenght的缩写 ,统计个数
print(len(emp))


#最终方案
for i in range(len(emp)):
    print(emp[i])


#思考:如果是2维,怎么处理
emp=((1,'张飞','屠夫'),(2,'刘备','卖草鞋'),(3,'关羽','保安'),(4,'孙尚香','大小姐'))

#答案
for i in range(len(emp)):
    for j in range(len(emp[i])):
        print(emp[i][j])


print(emp[0][0])
print(emp[0][1])
print(emp[0][2])
print(emp[1][0])
print(emp[1][1])
print(emp[1][2])
print(emp[3][0])
print(emp[3][1])
print(emp[3][2])

#如下你喜欢这样写,也可以,只是我们非常不推荐

emp=(7788,'caichang','teacher',200,None,True,'老王')

for i in emp:
    print(i)

emp=((1,'张飞','屠夫'),(2,'刘备','卖草鞋'),(3,'关羽','保安'),(4,'孙尚香','大小姐'))
for i in emp:
    for j in i:
        print(j)

