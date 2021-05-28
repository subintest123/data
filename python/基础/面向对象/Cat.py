from python基础.面向对象.Animal import Animal
from python基础.面向对象.Dog import Dog

#继承的目的:少写代码,复用
class Cat(Animal,Dog):
    #子类覆盖了父类的chi方法
    def chi(self):
        print('猫咪吃')


jiafei=Cat()
print(jiafei.name)
print(jiafei.chi())
print(jiafei.shui())
print(jiafei.play())