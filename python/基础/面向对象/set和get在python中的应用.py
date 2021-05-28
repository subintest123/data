class Animal():
    def __init__(self):
        self.name=''
        self.sex='雄性'
        self.__wife='凤姐'

    def chi(self):
        print('动物吃')

    def shui(self):
        print('动物睡')

    @property
    def getWife(self):
        return self.__wife

    @getWife.setter
    def setWife(self,wife):
        self.__wife=wife


animal = Animal()
print(animal.sex)
print(animal.getWife) #把方法当属性用

animal.setWife='范冰冰' #把方法当属性设
print(animal.getWife)