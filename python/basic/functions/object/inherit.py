# 父类
class animals():

    def __init__(self):
        self.name = ''
        self.__sex = '雄性'
        self.__age = '20'

    def play(self):
        print('米妮')

    def eat(self):
        print('奶酪')

    # get和set需要严格按照顺序（先get，后set）
    @property
    def get_sex(self):
        return self.__sex


    @get_sex.setter
    def set_sex(self, sex):
        self.__sex = sex

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def set_age(self, age):
        self.__age = age


mickey = animals()
mickey.play()
# get获得
print(mickey.get_sex)
# set设置
mickey.set_age = '22'
print(mickey.get_age)