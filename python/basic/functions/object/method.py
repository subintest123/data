class Cat():
    # 普通方法
    def eat(self):
        print('猫粮')

    def drink(self):
        print('牛奶')

    # 静态方法
    @staticmethod
    def play():
        print('猫薄荷')


nick = Cat()
print(nick.eat())
print(nick.drink())
print(nick.play())