# _和__
# 他们作用在属性和方法上
# _:受保护的,可以调,但不推荐调
# __:私有的,不可以直接调,他的目的是提供出来给本类的其他地方(属性/方法)用
class Person():
    def __init__(self, age):
        self.name = ''  # 直接赋予
        self.__sex = 0  # 私有属性,不允许直接调用,他也是给其他方法用
        self.family = []
        self._weight = 3  # 可以被调,但不推荐直接调,这个属性有其他特殊含义
        self.age = age  # 这样写才能把参数赋值给属性

    def eat(self):
        self.__play()  # 调用时,一定self.
        print('人吃......')

    # 这个方法不要轻易的直接对象掉
    def _sleep(self):
        print(f'你的性别{self.__sex}')  # 调用时self.
        print('人睡......')

    # 私有方法,提供给本类中的其他方法用
    def __play(self):
        name = self._weight
        print('play......')


caichang = Person(35)
caichang.name = '蔡昶'

# print(caichang._weight)
# print(caichang.__sex)
caichang.eat()
caichang._sleep()

# caichang._sleep()
# caichang.__play()
