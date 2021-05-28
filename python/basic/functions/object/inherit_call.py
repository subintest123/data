# 子类
from basic.functions.object.inherit import animals


class mouse(animals):

    def play(self):
        print('米奇')


minnie = mouse()
minnie.play()

# 调用父类中的set和get
minnie.set_sex = '雌性'
print(minnie.get_sex)
minnie.set_age = '18'
print(minnie.get_age)