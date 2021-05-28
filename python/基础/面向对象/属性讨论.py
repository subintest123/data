

class Person():
    # 静态属性:他既可以对象. 也可以类名.
    mouse=1
    eye=2
    ear=2

    #普通属性:写在初始化方法中且必须通过对象调
    #我们定义在__init__方法(初始化方法)中
    #前提知识:初始化

    def __init__(self,age):
        self.name='' #直接赋予
        self.sex=0
        self.family=[]
        self.weight=3
        self.age=age #这样写才能把参数赋值给属性
    #什么叫self?  最简单的理解:这个类的实例




#caichang是Person类的具体实例,做完这个动作,马上检查是否有初始化方法且初初始化方法是否有必填参
#如果有,马上传入对应的参数,不能直接写(),而应该写 (参数)
caichang=Person(35)
print(caichang.weight)
caichang.name='蔡昶'
print(caichang.name)
caichang.family=['爸爸','妈妈','姐姐']
print(caichang.family)
print(caichang.age)

print(caichang.eye)
print(Person.eye)
