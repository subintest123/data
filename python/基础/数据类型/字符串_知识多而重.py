# 1.既可以单引号也可以双引号
name = 'caichang'
name = "凤姐"

#2.字符串看成特殊的一维元组/列表
name = 'caichang'
print(name[1])
for i in range(len(name)):
    print(name[i])

#3.请学习字符串的40多个方法,如果你能都会并且灵活记住,那是高手 (这才是字符串最难的也是你要坚持的)
name='caichang'
print(name.upper())

name='   caichang    '
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

string = 'hello,caichang,nihao,wo ai ni,ni xihuan wo ma?'
print(string.split(','))
new_list=string.split(',')

for i in range(len(new_list)):
    if new_list[i]=='nihao':
        print('ok')

string = 'id=>baidu'
key=string.split('=>')[0]
value=string.split('=>')[1]
print(key)
print(value)



#4.字符串格式化 用方案3,其他2个忘记吧
name='蔡昶'
age=35
juzhudi='深圳岗厦'
status='单身'
print('我的名字叫name,今年age岁,目前在juzhudi,status') #格式化输出

#方案1 java +
print('我的名字叫'+name+',今年'+str(age)+'岁,目前在'+juzhudi+','+status)

#方案2 c %
print('我的名字叫%s,今年%d岁,目前在%s,%s' %(name,age,juzhudi,status))

#方案3 f  python3.6以后才有
print(f'我的名字叫{name},今年{age}岁,目前在{juzhudi},{status}')


#5.保持原样输出 在字符串前面带r,如果有特殊的请用\进行转义
# msg='i'm ok'
# print(msg)

msg="i'm ok"
print(msg)

msg='i\'m ok'
print(msg)

url='http://www.baidu.com/id?24&page=3'
url='http\:\/\/www.baidu.com\/id\?24\&page=3'
url=r'http://www.baidu.com/id?24&page=3'
print(url)



# 总结:
# 1.可单引号和双引号,建议双引号
# 2.r和f的引用
# 3.一堆的属于自己的方法(40+)
