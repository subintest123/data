#冒泡排序

# 预备知识:如何进行2个数的交换
#
# a,b = 5,7
# a,b = 7,5

lists = [3,10,7,16,13]

for i in range(len(lists)-1): #1为自身的那个,所以要-1 控制循环次数
    for j in range(len(lists)-i-1): #每次减去已经排好的那个数和自己要迭代的那个数 控制每一个和他的下一个比
        if lists[j]>lists[j+1]:
            lists[j],lists[j+1]=lists[j+1],lists[j]
print(lists)
