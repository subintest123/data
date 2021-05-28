
# return 返回值
# 我这个函数为什么要用return,不用不行吗?  可以不用也可以用,由场景决定

#这个函数如果是仅仅提供数据供调用者调用后处理的,那么这个函数加return
#当我都把参数写完了,最后审视我这个函数是不是提供服务给别人,如果是,这个函数
#中的数据就return出去
def total(start, end):
    total = 0
    for i in range(start, end):
        total = total + i  # total+=i也可以
        # print(total)
    return total


#调用总原则:
#1.用一个参数去接收这个函数
#2.拿着这个返回的参随便完(根据你的业务具体写代码)
#a调用
t = total(1,50)  # t=1225
print(t)


#b调用
t2 = total(1,101)
if t2>5000:
    print('ok')

# c调用
for i in range(total(1,11)):
    print(i)


#小总结:
#1.我们工作后写东西,可以先写业务
#2.把业务封装成一个函数
#3.审视函数中是否有写死的值,尽量用参数传递,这样写得灵活一点
#4.看看业务是否是提供数据支持,如果是,return出数据出去