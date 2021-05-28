class Person():
    # 格式化：__init__
    def __init__(self):
        self.name = ''
        self.sex = 0
        self.family = {}
        self.nation = ''


jack = Person()
jack.name = '苏斌'
jack.family = {'dad', 'mom', 'sis', 'grandma'}
jack.nation = '汉族'
print(jack.family, jack.name, jack.nation)



