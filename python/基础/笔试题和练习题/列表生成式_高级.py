# 快速的生成出一个满足规则的列表,可跟if,运算不行
lists =[]
for i in range(1,101):
    lists.append(i)
print(lists)

#new_lists=[变量 for的规则 [if判断]]

new_list=[i for i in range(1,11)]
print(new_list)

new_list=[i for i in range(1,101) if i%3==0 and i%5!=0]
print(new_list)

new_list=[i+j for i in range(1,11) for j in range(1,5) if i%3==0 and i%5!=0]
#i 3,6,9
#j 1...4
print(new_list)
