class Dog():
    name = ''
    age = ''
    eye = '2'

    def voice(self):
        print('嗷..嗷...嗷呜')

    def skill(self):
        print('看家、拆家')


wangcai = Dog()
wangcai.skill()
wangcai.voice()
wangcai.name = '旺财'
print(wangcai.name)
