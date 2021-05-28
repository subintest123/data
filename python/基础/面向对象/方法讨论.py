class Person():
    name='caichang'

    #普通方法
    def eat(self):
        print('人吃......')
    def sleep(self):
        print('人睡......')

    #静态方法,不写self
    @staticmethod
    def play():
        print('呵呵.......')

    #类方法
    @classmethod
    def le(cls):
        print(f'le.......{cls.name}')

caichang =Person() # 申明一个对象去接收这个类,实例化Person类
caichang.eat()
caichang.play()

#静态方法和静态属性一样,可以对象, 也可以 类名.
print(Person.play())

print(caichang.le())

print(Person.le())