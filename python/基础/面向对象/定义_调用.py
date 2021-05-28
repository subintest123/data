# 对象
# 定义
class Cat():  # 定义一个Cat类
    name = ''  # Cat的属性
    eye = 2  # 定义Cat类的具体属性

    # 定义Cat的具体方法
    def jiao(self):
        print('喵喵喵.....')

    def zhualaoshu(self):
        print('物理攻击....')


# 调用
huahua = Cat()  # huahua是不是这只猫的具体实例,huahua是Cat的对象
huahua.zhualaoshu()  # 一切都要靠这个对象. 出来 对象.方法
huahua.name = '花花'  # 对象.属性
print(huahua.name)

tom = Cat() #这个动作我们也叫:实例化Cat类
tom.jiao()
tom.zhualaoshu()

#huahua不等于tom,因为是2个不同的实例
