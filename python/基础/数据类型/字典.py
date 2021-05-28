#字典  dictionary
#在做接口自动化时,接口的返回值几乎全是json格式,这个json和dict很像
emp={
    'empno':7788,
    'ename':'caichang',
    'family':['姐姐','妈妈','老爹'],
    'work':{
        'first':{
            'address':'厦门',
            'time':'2000-01-01'
        },
        'second':{
            'address':'重庆',
            'time':'2010-10-10'
        }
    },
    'age':35,
    'juzhudi':'深圳',
    'laojia':'遵义'
}
print(type(emp))

#取值 通过key取value值
print(emp['juzhudi'])
print(emp['family'])

for i in range(len(emp['family'])):
    print(emp['family'][i])

print(emp['work']['second']['address'])

print(emp.get('family'))
print(emp.get('work').get('second').get('address'))

print(emp.keys())
print(emp.values())

#字典其他的方法请自行学习



