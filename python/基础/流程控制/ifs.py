#if有严格的缩进机制
#input表示输入,

#1.单if
# age=int(input('请输入你的年龄:'))
# if age>18:
#     print('你成年了')
#     print('可以参军了')
# print('hehe')

#2.if...else...
# age=int(input('请输入你的年龄:'))
# if age>18:
#     print('你成年了')
# else:
#     print('未成年!')

#3.if....elif....else....
# age=int(input('请输入你的年龄:'))
# if age>30:
#     print('对不起,太老了,不符合当兵规则')
# elif age>=18:
#     print('可当兵')
# else:
#     print('不能当兵,年级太小')

#4.if....if....if....  查询时就会采用if并行判断
# cate=input()
# brand=input()
# key=input()
#
# if cate is not None:
#     where['cate']=cate
# if brand is not None:
#     where['brand']=brand
# if key is not None:
#     where['key']=key

#5.if嵌套
# age=int(input('请输入你的年龄:'))
# only=False
# if age>30:
#     if only==True:
#         print('对不起,你真当不了兵')
#     else:
#         if age>=18:
#             print('当兵去吧')
#         else:
#             print('太小,当不了兵')

#登录  caichang caichang1  1111

username=input('请输入用户名:')
pwd=input('请输入密码:')
verify=int(input('请输入验证码:'))

# if username=='caichang': # if username!='caichang':
#     #     print('用户名不正确')
#     # if pwd!='caichang1':
#     #     print('密码不正确')
#     # if username=='caichang' and pwd=='caichang1':
#     #     print('登录成功')
#     # else:
#     #     print('登录失败')
#     if pwd=='caichang1':
#         if verify==1111:
#             print('登录成功')
#         else:
#             print('验证码不正确')
#     else:
#         print('密码错误')
# else:
#     print('用户名不正确')

# if verify!=1111:
#     print('验证码不正确')
# else:
#
#     if username == 'caichang' and pwd == 'caichang1':
#         print('登录成功')
#     else:
#         if username != 'caichang':
#             print('用户名不正确')
#         if pwd != 'caichang1':
#             print('密码不正确')
#
#
#
